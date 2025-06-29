# 🧪 Test Cases — Minimal RISC-V Assembler

# Test Case 1: Basic R-type and I-type
# Expected output:
# addi x1, x0, 5      --> 00500093
# add x2, x1, x1      --> 00110133
# nop                 --> 00000013

li x1, 5
add x2, x1, x1
nop


# Test Case 2: Mixed pseudo-instructions
# Expected output:
# li x3, 10           --> 00a00113
# mv x4, x3           --> 00300293

li x3, 10
mv x4, x3


# Test Case 3: Label usage and branching
# Expected output:
# Loop:
#   addi x5, x0, 1    --> 00100293
#   beq x5, x0, Loop  --> should resolve to relative offset (depends on label addr)

Loop:
  addi x5, x0, 1
  beq x5, x0, Loop


# Test Case 4: S-type store
# Expected output:
# addi x6, x0, 20     --> 01400313
# sw x6, 0(x0)        --> 00602023

addi x6, x0, 20
sw x6, 0(x0)




# Test Cases (Expected Outputs in Comments)

li x1, 10        # => addi x1, x0, 10
mv x2, x1        # => addi x2, x1, 0
nop              # => add x0, x0, x0
add x3, x1, x2   # => x3 = x1 + x2
