r_type_dis = {
    0b100000 : ("add", ["rd", "rs", "rt"]),
    0b100001 : ("addu", ["rd", "rs", "rt"]),
    0b100100 : ("and", ["rd", "rs", "rt"]),
    0b001101 : ("break", []),
    0b011010 : ("div", ["rd", "rs", "rt"]),
    0b011011 : ("divu", ["rs", "rt"]),
    0b001001 : ("jalr", ["rd", "rs"]),
    0b001000 : ("jr", ["rs"]),
    0b010000 : ("mfhi", ["rd"]),
    0b010010 : ("mflo", ["rd"]),
    0b010001 : ("mthi", ["rs"]),
    0b010011 : ("mtlo", ["rs"]),
    0b011000 : ("mult", ["rs", "rt"]),
    0b011001 : ("multu", ["rs", "rt"]),
    0b100111 : ("nor", ["rd", "rs", "rt"]),
    0b100101 : ("or", ["rd", "rs", "rt"]),
    0b000000 : ("sll", ["rd", "rt", "sa"]),
    0b000100 : ("sllv", ["rd", "rt", "rs"]),
    0b101010 : ("slt", ["rd", "rs", "rt"]),
    0b101011 : ("sltu", ["rd", "rs", "rt"]),
    0b000011 : ("sra", ["rd", "rt", "sa"]),
    0b000111 : ("srav", ["rd", "rt", "rs"]),
    0b000010 : ("srl", ["rd", "rt", "sa"]),
    0b000110 : ("srlv", ["rd", "rt", "rs"]),
    0b100010 : ("sub", ["rd", "rs", "rt"]),
    0b100011 : ("subu", ["rd", "rs", "rt"]),
    0b001100 : ("syscall", []),
    0b100110 : ("xor", ["rd", "rs", "rt"]),
}

i_type_dis = {
    0b001000 : ("addi", ["rt", "rs", "immediate"]),
    0b001001 : ("addiu", ["rt", "rs", "immediate"]),
    0b001100 : ("andi", ["rt", "rs", "immediate"]),
    0b000100 : ("beq", ["rs", "rt", "offset"]),
    0b000001 : [("bgez", 0b00001, ["rs", "offset"]), ("bltz", 0b00000, ["rs", "offset"])],
    0b000111 : ("bgtz", 0b00000, ["rs", "offset"]),
    0b000110 : ("blez", 0b00000, ["rs", "offset"]),
    0b000101 : ("bne", ["rs", "rt", "offset"]),
    0b100000 : ("lb", ["rt", "offset(base)"]),
    0b100100 : ("lbu", ["rt", "offset(base)"]),
    0b100001 : ("lh", ["rt", "offset(base)"]),
    0b100101 : ("lhu", ["rt", "offset(base)"]),
    0b001111 : ("lui", 0b00000, ["rt", "immediate"]),
    0b100011 : ("lw", ["rt", "offset(base)"]),
    0b001101 : ("ori", ["rt", "rs", "immediate"]),
    0b101000 : ("sb", ["rt", "offset(base)"]),
    0b111000 : ("sc", ["rt", "offset(base)"]),
    0b001010 : ("slti", ["rt", "rs", "immediate"]),
    0b001011 : ("sltiu", ["rt", "rs", "immediate"]),
    0b101001 : ("sh", ["rt", "offset(base)"]),
    0b101011 : ("sw", ["rt", "offset(base)"]),
    0b001110 : ("xori", ["rt", "rs", "immediate"]),
}

j_type_dis = {
    0b000010: 'j',
    0b000011: 'jal'
}