# 🛠️ Minimal RISC-V Assembler (Python)

This project is a human-friendly, lightweight RISC-V assembler written in Python. It translates basic RISC-V assembly code into hexadecimal machine instructions, making it easier to simulate custom pipelines or embedded projects.

---

## ✨ Features
- ✅ Supports **R-type**, **I-type**, **S-type**, and **B-type** instructions
- 🎭 Handles **pseudo-instructions** like `li`, `mv`, and `nop`
- 🏷️ Resolves **labels** for jumps and branches via two-pass parsing
- 🧠 Clean modular code (tokenizer, encoder, label resolver, writer)
- 📤 Outputs clean `.hex` file (32-bit hex per line)

---

## 📂 Project Structure
```
minimal_riscv_assembler/
├── assembler.py
├── pseudo.py
├── encoder.py
├── tokenizer.py
├── labels.py
├── test_programs/
│   ├── test1.asm
│   └── test2.asm
└── output.hex
```

---

## 🔄 How It Works
1. **Tokenization**: Parses the assembly line-by-line
2. **First Pass**: Records label positions (for `beq`, jumps)
3. **Pseudo Expansion**: Converts things like `li x1, 10` → `addi x1, x0, 10`
4. **Second Pass**: Encodes final binary instruction
5. **Write Out**: Exports clean hex format to `output.hex`

---

## ▶️ Example Input (Assembly)
```asm
li x1, 10
mv x2, x1
add x3, x1, x2
```

## 💾 Output (.hex)
```txt
00a00093
00100113
002081b3
```

---

## 📘 Learning Outcomes
- Hands-on RISC-V instruction formats
- Label resolution logic and address offsets
- Instruction encoding and file generation

---

## 🚀 Future Scope
- Add support for U-type, J-type
- Handle real `.data`, `.text` segments
- GUI or web interface for educational use

---

## 📁 Test Cases
See the separate file: [`RISC-V_Assembler_Tests.txt`](../RISC-V_Assembler_Tests.txt)

---

## 🧑‍💻 Author
Made for CPU & Embedded learners who want to build their own toolchain from scratch.

