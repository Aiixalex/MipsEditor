import re

from Assmbler.Instruction import Instruction



def assemble(input):
    Instructions = []
    output = []
    dict_address = {}
    address = 0x0
    with_label = False
    pos_label = 0
    label = ''

    lines = input.split('\n')
    lines = [l.strip() for l in lines]
    length = len(lines)

    # fulfill the dictionary of address dict_address
    for i in range(length):
        if lines[i] == '':                                         # a blank line
            continue
        if re.search(r'#', lines[i]):                              # if this line has annotation
            pos_annotation = re.search(r'#', lines[i]).span()[0]   # calculate the position of annotation
            if(lines[i][0:pos_annotation].strip() == ''):          # whether there are codes before annotation
                lines[i] = ''
                continue
            lines[i] = lines[i][0:pos_annotation]                  # delete the annotation

        if re.search(r':', lines[i]):                              # if this line has a label
            with_label = True
            pos_label = re.search(r':', lines[i]).span()[0]
            label = lines[i][0:pos_label].strip()
            dict_address[label] = address                          # record the address of this label
            if lines[i][pos_label+1:len(lines[i])].strip() == '':  # if no code after label in this line
                continue
        else:
            with_label = False

        if re.search(r'\.text', lines[i]):                         # pesudo-op '.text'
            dict_address[".text"] = address
        elif re.search(r'\.data', lines[i]):                       # pesudo-op '.data'
            dict_address[".data"] = address

        if not re.search(r'\.', lines[i]):
            address += 4

    # convert instruction to machine code
    for i in range(length):
        if lines[i] == '':                                         # a blank line
            continue

        if re.search(r':', lines[i]):                              # if this line has a label
            with_label = True
            pos_label = re.search(r':', lines[i]).span()[0]
            label = lines[i][0:pos_label].strip()
            if lines[i][pos_label+1:len(lines[i])].strip() == '':  # if no code after label in this line
                continue
        else:
            with_label = False

        if not re.search(r'\.', lines[i]):
            if with_label:
                params = lines[i][pos_label+1:len(lines[i])].split(',')
            else:
                params = lines[i].split(',')
            params = [i.strip() for i in params]
            op, params[0] = params[0].split(' ')                 # convert instruction to op and params
            address += 4
            Instructions.append(Instruction(op, params, dict_address))        # new an object of class Instruction
            output.append(Instructions[i].toMachineCode())     # convert to machine code

    # file stream
    f = open("asm_Result.txt", 'w')
    for line in output:
        f.write(line + '\n')                                   # write into the file
    f.close()
    return
if __name__ == '__main__':
    # bits = open(r'test.txt', 'r+')
    # temp = assemble(bits.read())[0]
    # i = 0
    # print(len(temp)/32)
    # while i < len(temp):
    #     print(hex(int((i+32)/32)) + '  ' + temp[i:i+32])
    #     i = i + 32
    # bits.close()
    assemble('start: add $a0, $s0, $s1\nbeq $s0, $s1, exit\nsll $s0, $s1, 2\nbgez $s0, start\nj start\nexit:')