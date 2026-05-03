# **Phase 0: Programming Fundamentals**

Welcome to the absolute beginning. If you've never written a line of code, this is where you start. Programming is simply giving a set of instructions to a computer to solve a problem.

---

## **1. Variables: The Boxes of Programming**

Imagine a variable as a labeled box. You can put data inside it and use it later by referring to the label.

### **Example (Java):**
```java
int age = 25; // A box labeled 'age' containing the number 25
String name = "Zoho Developer"; // A box labeled 'name' containing text
```

### **Deep Dive: Memory Allocation**
When you write `int age = 25;`, two things happen:
1. **Declaration:** The computer reserves a small piece of RAM (4 bytes for an `int`).
2. **Initialization:** The value `25` is stored in that specific memory address.

> [!TIP]
> Think of RAM as a massive hotel. Every room has a **number** (Memory Address). Variables are just **nicknames** for those room numbers so you don't have to remember `0x7ffeefbff5c8`.

---

## **2. Data Types: What's in the Box?**

Computers need to know what kind of data you are storing to allocate the right amount of memory.

| Type | Name | Purpose | Example |
| :--- | :--- | :--- | :--- |
| **int** | Integer | Whole numbers | `10`, `-5`, `2024` |
| **double** | Double | Decimal numbers | `10.5`, `3.14159` |
| **char** | Character | Single letters/symbols | `'A'`, `'@'`, `'7'` |
| **boolean** | Boolean | True or False | `true`, `false` |
| **String** | String | Text | `"Hello Zoho"` |

---

## **3. Operators: Doing Math and Logic**

### **Arithmetic Operators**
- `+` (Add), `-` (Subtract), `*` (Multiply), `/` (Divide)
- `%` (Modulo): Gives the **remainder**. Very useful for finding even/odd numbers (`n % 2 == 0`).

### **Unary Operators**
- `i++` (Post-increment): Use current value, then add 1.
- `++i` (Pre-increment): Add 1, then use new value.
- `i--` / `--i` (Decrement).

### **Bitwise Operators (Advanced - Common in Round 1)**
Computers don't see `5`, they see `101` (binary).
- `&` (AND): 1 if both bits are 1.
- `|` (OR): 1 if either bit is 1.
- `^` (XOR): 1 if bits are different.
- `<<` (Left Shift): Multiplies by 2.
- `>>` (Right Shift): Divides by 2.

### **Comparison Operators**
- `==` (Equal to), `!=` (Not equal to)
- `>` (Greater than), `<` (Less than)

---

## **4. Control Flow: The Decision Maker**

Your code isn't always linear. Sometimes it needs to make choices.

### **If-Else Statement**
```java
int score = 85;

if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else {
    System.out.println("Grade: C");
}
```

---

## **5. Input and Output (I/O)**

To make programs interactive, you need to talk to the user.

### **Java Example:**
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter your name: ");
        String name = sc.nextLine();
        
        System.out.println("Hello " + name + "! Welcome to Zoho Prep.");
    }
}
```

---

## **6. Common Pitfalls (The "Gotchas")**

Avoid these common beginner mistakes that often show up in Zoho's Round 1:

### **A. Integer Division**
```java
int result = 5 / 2; 
System.out.println(result); // Output: 2 (NOT 2.5!)
```
*Fix:* Use `5.0 / 2` or `(double) 5 / 2`.

### **B. Comparing Strings**
```java
String s1 = "hello";
String s2 = "hello";
if (s1 == s2) { ... } // May work sometimes, but is UNRELIABLE
```
*Fix:* Always use `s1.equals(s2)` for comparing text. `==` compares memory addresses, not the actual text.

### **C. The Semicolon Trap**
```java
if (score > 90); // <--- THIS SEMICOLON KILLS THE LOGIC
{
    System.out.println("You passed!");
}
```
*Effect:* The "You passed!" will print NO MATTER WHAT the score is, because the `if` ends at the semicolon.

---

## **🎯 Exercise for You:**
Write a program that takes two numbers as input from the user and prints their sum, difference, and product. **Bonus:** Explain why `int x = 2147483647 + 1;` results in a negative number.

[Next Step: Mastering Loops and Logic ->](../0_Fundamentals/Java_Basics.md)
