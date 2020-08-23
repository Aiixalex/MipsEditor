from Assmbler.registers_asm import registers_asm
from Assmbler.instructions_asm import r_type_asm, i_type_asm, j_type_asm


class Instruction:
    def __init__(self, op = None, params = None, dict_address = None):
        self.op = op.lower()
        self.dict_address = dict_address
        self.rd, self.rs, self.rt, self.immediate = 0, 0, 0, 0

        # if instruction is r-type
        if self.op in r_type_asm.keys():
            # read params of this instruction from the dictionary
            param_type = r_type_asm[self.op][-1]
            # convert the param to registers or immediate numbers
            for type, param_str in zip(param_type, params):
                if type == "rd":
                    self.rd = registers_asm[param_str]
                if type == "rs":
                    self.rs = registers_asm[param_str]
                if type == "rt":
                    self.rt = registers_asm[param_str]
                if type == "sa":
                    self.immediate = int(param_str)

        # if instruction is i-type
        elif self.op in i_type_asm.keys():
            # read params of this instruction from the dictionary
            param_type = i_type_asm[self.op][-1]
            # convert the param to registers or immediate numbers
            for type, param_str in zip(param_type, params):
                if type == "rs":
                    self.rs = registers_asm[param_str]
                if type == "rt":
                    self.rt = registers_asm[param_str]
                if type == "immediate":
                    self.immediate = int(param_str)
                if type == "offset":
                    self.label = param_str
                if type == "offset(base)":                                                           # e.g. 4($s0)
                    self.rs = registers_asm[param_str[param_str.find("(") + 1: param_str.find(")")]] # e.g. $s0
                    self.immediate = int(param_str[0 : param_str.find("(")])                         # e.g. 4

        elif self.op in j_type_asm.keys():                            # if instruction is j_type
            self.label = params[0]


    def toMachineCode(self):
        machine_code = 0
        if self.op in r_type_asm:
            machine_code |= (self.rs<< 21)
            machine_code |= (self.rt<< 16)
            machine_code |= (self.rd << 11)
            machine_code |= (self.immediate << 6)
            machine_code |= (r_type_asm[self.op][1])
        if self.op in i_type_asm:
            machine_code |= (i_type_asm[self.op][0] << 26)
            machine_code |= (self.rs << 21)
            machine_code |= (self.rt << 16)
            if (i_type_asm[self.op][-1] == ["rs", "offset"]):         # if op == "bgez", "bgtz", "blez", "bltz"
                machine_code |= (i_type_asm[self.op][1] << 16)
            if (i_type_asm[self.op][-1] == ["rt", "immediate"]):      # if op == "lui"
                machine_code |= (i_type_asm[self.op][1] << 21)
            if self.label:
                machine_code |= self.dict_address[self.label]
            else:
                machine_code |= self.immediate

        if self.op in j_type_asm:
            machine_code |= (j_type_asm[self.op][0] << 26)
            machine_code |= self.dict_address[self.label]

        # output format: 32-bit binary number
        return "{0:0=32b}".format(machine_code)