
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
