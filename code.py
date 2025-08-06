# Basic instruction patterns
opcodes = {
    'add':  '0110011',
    'sub':  '0110011',
    'addi': '0010011',
    'sw':   '0100011',
    'beq':  '1100011'
}

funct3 = {
    'add':  '000', 'sub':  '000', 'addi': '000',
    'sw':   '010', 'beq':  '000'
}

funct7 = {
    'add':  '0000000',
    'sub':  '0100000'
}

# Turn register like "x5" into 5-bit binary like "00101"
def reg_to_bin(reg):
    num = int(reg[1:])  # remove 'x'
    return format(num, '05b')

# R-type: add, sub
def encode_r(op, rd, rs1, rs2):
    return funct7[op] + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + reg_to_bin(rd) + opcodes[op]

# I-type: addi
def encode_i(op, rd, rs1, imm):
    imm_bin = format(int(imm) & 0xFFF, '012b')
    return imm_bin + reg_to_bin(rs1) + funct3[op] + reg_to_bin(rd) + opcodes[op]

# S-type: sw
def encode_s(op, rs2, rs1, imm):
    imm_bin = format(int(imm) & 0xFFF, '012b')
    return imm_bin[:7] + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + imm_bin[7:] + opcodes[op]

# B-type: beq
def encode_b(op, rs1, rs2, imm):
    imm_bin = format(int(imm) & 0x1FFF, '013b')
    # imm bits rearranged as per RISC-V spec
    return imm_bin[0] + imm_bin[2:8] + reg_to_bin(rs2) + reg_to_bin(rs1) + funct3[op] + imm_bin[8:12] + imm_bin[1] + opcodes[op]

# Binary to Hex
def bin_to_hex(binary):
    return format(int(binary, 2), '08x')

# Handle pseudo instructions like li, mv, nop
def expand_pseudo(op, args):
    if op == 'li':   return [('addi', args[0], 'x0', args[1])]
    if op == 'mv':   return [('addi', args[0], args[1], '0')]
    if op == 'nop':  return [('addi', 'x0', 'x0', '0')]
    return [(op, *args)]  # normal instruction

# The main function
def assemble(asm_lines):
    hex_output = []

    for line in asm_lines:
        line = line.split('#')[0].strip()  # remove comments
        if not line: continue

        parts = line.replace(',', '').split()
        op = parts[0]
        args = parts[1:]

        expanded = expand_pseudo(op, args)

        for inst in expanded:
            op2, *args2 = inst

            if op2 in ['add', 'sub']:
                binary = encode_r(op2, *args2)
            elif op2 == 'addi':
                binary = encode_i(op2, *args2)
            elif op2 == 'sw':
                binary = encode_s(op2, args2[0], args2[2], args2[1])  # sw x4, 0(x0)
            elif op2 == 'beq':
                binary = encode_b(op2, *args2)
            else:
                binary = '0' * 32  # fallback

            hex_output.append(bin_to_hex(binary))

    return hex_output

