# **Phase 2: Pattern Printing (Zoho Specialist)**

Zoho Round 2 is famous for pattern printing. They don't just want the code; they want to see if you can visualize logic using nested loops.

---

## **1. The Golden Rule of Patterns**

Every pattern consists of:
1. **Outer Loop:** Controls the **Rows** (`i`).
2. **Inner Loop 1:** Controls the **Spaces** (if any).
3. **Inner Loop 2:** Controls the **Columns/Numbers/Stars** (`j`).

---

## **2. Standard Patterns**

### **A. Right-Angled Triangle**
```
*
**
***
****
```
```java
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print("*");
    }
    System.out.println();
}
```

### **B. Pyramid Pattern**
```
   *
  ***
 *****
```
```java
int n = 3;
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n - i; j++) System.out.print(" "); // Spaces
    for (int j = 1; j <= (2 * i - 1); j++) System.out.print("*"); // Stars
    System.out.println();
}
```

---

## **3. Advanced Patterns (Frequent Zoho Questions)**

### **The X-Pattern** (Diagonal)
Given a string like "PROGRAM", print it in an X shape.
```
P     M
 R   A 
  O R  
   G   
  O R  
 R   A 
P     M
```

### **The Spiral Matrix**
Print numbers 1 to N^2 in a spiral fashion in a square matrix.

---

## **4. Pro-Tips for Round 2**
- **Use Graph Paper Mental Model:** Imagine your output on a grid. Find the relation between the row index `i` and column index `j`.
- **Don't Hardcode:** Ensure your logic works for any input `n`.
- **Handle Even/Odd:** Some patterns change slightly if `n` is even vs. odd.

---

## **🎯 Exercise for You:**
1. Print a **Diamond Pattern** of stars.
2. Given `n=5`, print:
```
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
```

[Next Step: Logic & Mathematical Puzzles ->](../2_Zoho_Round_Specific/Logic_Puzzles.md)
