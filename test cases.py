program = [
    "li x1, 5",          # => addi x1, x0, 5
    "li x2, 10",         # => addi x2, x0, 10
    "add x3, x1, x2",    # => x3 = x1 + x2
    "mv x4, x3",         # => addi x4, x3, 0
    "sw x4, 0(x0)",      # => mem[0] = x4
    "beq x1, x2, 4",     # => if x1 == x2, jump forward
    "nop"                # => addi x0, x0, 0
]

output = assemble(program)

print("Hex Output:")
for hex_code in output:
    print(hex_code)

# 00500093  # addi x1, x0, 5
# 00a00113  # addi x2, x0, 10
# 002081b3  # add x3, x1, x2
# 00018213  # addi x4, x3, 0
# 00402023  # sw x4, 0(x0)
# 00210263  # beq x1, x2, 4
# 00000013  # nop
