from Dissembler.instructions_dis import r_type_dis, i_type_dis, j_type_dis
from Dissembler.registers_dis import registers_dis


def dissemble(input):
    output = []
    label_num = 0
    label_address = []

    lines = input.split('\n')
    lines = [l.strip() for l in lines]
    length = len(lines)
    for i in range(length):
        if lines[i] == '':
            continue
        instruction = ''
        opcode = int(lines[i][0:6], 2)

        # if r-type
        if opcode == 0:
            funct = int(lines[i][26:32], 2)
            if funct in r_type_dis.keys():
                # the first part of instruction: op
                instruction += r_type_dis[funct][0]
                param_type = r_type_dis[funct][-1]
                for j in range(len(param_type)):
                    param = ''
                    if param_type[j] == 'rd':
                        param = registers_dis[int(lines[i][16:21], 2)]
                    elif param_type[j] == 'rs':
                        param = registers_dis[int(lines[i][6:11], 2)]
                    elif param_type[j] == 'rt':
                        param = registers_dis[int(lines[i][11:16], 2)]
                    elif param_type[j] == 'sa':
                        param = str(int(lines[i][21:26], 2))
                    instruction += ' ' + param

                    # if it's not the last param of this instruction
                    if j != len(param_type)-1:
                        instruction += ','

        # if i-type
        elif opcode in i_type_dis.keys():
            op = ''
            params = []
            if isinstance(i_type_dis[opcode], list) == True:
                for t in i_type_dis[opcode]:             # instruction with the same opcode
                    if int(lines[i][11:16], 2) == t[1]:  # the 11-15 bits differs op of instructions that has the same opcode
                        op = t[0]
                        params = t[-1]
            elif isinstance(i_type_dis[opcode], tuple) == True: # instructions whose opcode is unique
                op = i_type_dis[opcode][0]
                params = i_type_dis[opcode][-1]
            instruction += op
            for j in range(len(params)) :
                param = ''
                if params[j] == 'rs' :
                    param = registers_dis[int(lines[i][6:11], 2)]
                elif params[j] == 'rt' :
                    param = registers_dis[int(lines[i][11:16], 2)]
                elif params[j] == 'offset' :
                    if int(lines[i][16:32], 2) not in label_address:
                        param = 'label_%d' % label_num
                        label_address.append(int(lines[i][16:32], 2))
                        label_num += 1
                    else:
                        param = 'label_%d' % label_address.index(int(lines[i][16:32], 2))
                elif params[j] == 'immediate':
                    param = str(int(lines[i][16:32], 2))
                elif params[j] == 'offset(base)':
                    param = '%d(' % int(lines[i][16:32], 2) + registers_dis[int(lines[i][6:11], 2)] + ')'

                instruction += ' ' + param
                if j != len(params) - 1 :
                    instruction += ','

        elif opcode in j_type_dis.keys():
            instruction += j_type_dis[opcode] + ' '
            if int(lines[i][16 :32], 2) not in label_address :
                instruction += 'label_%d' % label_num
                label_address.append(int(lines[i][16 :32], 2))
                label_num += 1
            else:
                instruction += 'label_%d' % label_address.index(int(lines[i][16 :32], 2))

        output.append(instruction)

    if len(output)*4 in label_address:
        output.append('')
    for i in range(len(output)):
        if i*4 in label_address:
            output[i] = 'label_%d: ' % label_address.index(i*4) + output[i]
        else:
            output[i] = '         ' + output[i]

    f = open("dis_Result.txt", 'w')
    for line in output :
        f.write(line + '\n')  # write into the file
    f.close()
    return

if __name__ == '__main__':
    dissemble('00000010000100010010000000100000\n00010010000100010000000000010100\n00000000000100011000000010000000\n00000110000000010000000000000000\n00001000000000000000000000000000')