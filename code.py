opcodes = {
    'add':  '0110011',
    'sub':  '0110011',
    'addi': '0010011',
    'sw':   '0100011',
    'beq':  '1100011'
}

funct3 = {
    'add':  '000',
    'sub':  '000',
    'addi': '000',
    'sw':   '010',
    'beq':  '000'
}

funct7 = {
    'add':  '0000000',
    'sub':  '0100000'
}

def reg_to_bin(reg):
    reg_num = int(reg[1:]) 
    return format(reg_num, '05b')

# Encode R-type instruction
def encode_r(op, rd, rs1, rs2):
    return funct7[op] + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + reg_to_bin(rd) + opcodes[op]

# Encode I-type instruction
def encode_i(op, rd, rs1, imm):
    imm_bin = format(int(imm) & 0xFFF, '012b')
    return imm_bin + reg_to_bin(rs1) + funct3[op] + reg_to_bin(rd) + opcodes[op]

# Encode S-type instruction
def encode_s(op, rs2, rs1, imm):
    imm_val = int(imm) & 0xFFF
    imm_bin = format(imm_val, '012b')
    imm_high = imm_bin[:7]
    imm_low = imm_bin[7:]
    return imm_high + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + imm_low + opcodes[op]

# Encode B-type instruction
def encode_b(op, rs1, rs2, imm):
    offset = int(imm)
    offset_bin = format(offset & 0x1FFF, '013b')
    return offset_bin[0] + offset_bin[2:8] + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + offset_bin[8:12] + offset_bin[1] + opcodes[op]

# Convert 32-bit binary to hex
def bin_to_hex(bin_str):
    return format(int(bin_str, 2), '08x')

# Convert pseudo-instructions to real ones
def expand_pseudo(op, args):
    if op == 'li':
        return [('addi', args[0], 'x0', args[1])]
    elif op == 'mv':
        return [('addi', args[0], args[1], '0')]
    elif op == 'nop':
        return [('addi', 'x0', 'x0', '0')]
    else:
        return [(op, *args)]

def assemble(assembly):
    result = []

    for line in assembly:
        line = line.split('#')[0].strip()  # remove comments
        if not line:
            continue

        parts = line.replace(',', '').split()
        op = parts[0]
        args = parts[1:]

        instructions = expand_pseudo(op, args)

        for inst in instructions:
            op2 = inst[0]
            args2 = inst[1:]

            if op2 in ['add', 'sub']:
                bin_code = encode_r(op2, args2[0], args2[1], args2[2])
            elif op2 == 'addi':
                bin_code = encode_i(op2, args2[0], args2[1], args2[2])
            elif op2 == 'sw':
                bin_code = encode_s(op2, args2[0], args2[2], args2[1])
            elif op2 == 'beq':
                bin_code = encode_b(op2, args2[0], args2[1], args2[2])
            else:
                bin_code = '0' * 32 

            hex_code = bin_to_hex(bin_code)
            result.append(hex_code)

    return result
    
    program = [
        "li x1, 5",          # -> addi x1, x0, 5
        "li x2, 10",         # -> addi x2, x0, 10
        "add x3, x1, x2",    # -> x3 = x1 + x2
        "mv x4, x3",         # -> addi x4, x3, 0
        "sw x4, 0(x0)",      # -> memory[0] = x4
        "beq x1, x2, 4",     # -> if x1 == x2 jump
        "nop"                # -> addi x0, x0, 0
    ]

    output = assemble(program)

    print("Generated HEX:")
    for line in output:
        print(line)
