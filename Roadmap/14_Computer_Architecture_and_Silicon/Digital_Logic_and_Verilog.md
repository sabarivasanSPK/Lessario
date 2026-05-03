# **Phase 14: Silicon - Digital Logic & Verilog**

Before you can build an AI chip, you must understand how computers calculate using only **Electricity (1s and 0s)**.

---

## **1. The Logic Gates**
Everything in your computer is built from these 3 gates:
- **AND:** Returns 1 if both inputs are 1.
- **OR:** Returns 1 if at least one input is 1.
- **NOT:** Flips a 1 to a 0 and vice versa.

By combining these, you create **Adders** (for math), **Flip-Flops** (for memory), and **Multiplexers** (for routing data).

---

## **2. Verilog: Programming Hardware**
Verilog looks like C, but it behaves differently. In software, code runs line-by-line. In hardware, everything happens **at the same time** (in parallel).

### **A Simple 4-bit Adder in Verilog**
```verilog
module adder (
    input [3:0] a,
    input [3:0] b,
    output [4:0] sum
);
    assign sum = a + b;
endmodule
```

---

## **3. FPGA: The Developer's Playground**
You don't need to spend $100M to build your first chip. You can use an **FPGA** (Field Programmable Gate Array).
- It is a chip that can "re-wire" itself to become any hardware you design in Verilog.
- **Recommended Beginner Board:** **TinyFPGA** or **Basys 3**.

---

## **4. RISC-V: The Open Future**
RISC-V is an open-source Instruction Set Architecture (ISA). It is the "Linux of Hardware." 
- Because it is open, you can design a chip that uses RISC-V without paying millions in royalties to ARM or Intel.

---

## **🎯 Exercise for You:**
1. Download **Logisim-evolution** (Open Source).
2. Build a "Full Adder" using only AND, OR, and XOR gates.
3. Verify that it correctly adds two bits and a carry.

[Next Step: AI Accelerator Architecture ->](./AI_Accelerator_Architecture.md)
