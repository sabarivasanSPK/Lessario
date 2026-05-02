# **Phase 0: Java Basics & Logic Building**

Now that you know how to store data and make simple decisions, it's time to learn how to make the computer repeat tasks and organize your code.

---

## **1. Loops: The "Repeater"**

Loops allow you to run the same block of code multiple times. This is essential for Zoho's Round 2 (Pattern Printing).

### **A. The `for` Loop** (Best when you know the count)
Use this when you know exactly how many times you want to repeat.
```java
for (int i = 1; i <= 3; i++) {
    System.out.println("Iteration: " + i);
}
```

### **B. The `while` Loop** (Best when you wait for a condition)
Use this when you don't know the count, but you know when to stop.
```java
int count = 3;
while (count > 0) {
    System.out.println("Countdown: " + count);
    count--;
}
```

### **C. The `do-while` Loop** (Runs at least once)
The condition is checked **after** the block runs.
```java
int x = 10;
do {
    System.out.println("This will print once even if x > 5 is false.");
} while (x < 5);
```

---

## **2. Understanding the "Dry Run"**

A "Dry Run" is when you trace the code manually using a table. This is the **#1 skill** needed for Zoho Round 1 (Output Prediction).

### **Example Code:**
```java
int sum = 0;
for (int i = 1; i <= 3; i++) {
    sum = sum + i;
}
```

### **Dry Run Table:**
| Step | `i` | `i <= 3` | `sum` (Old) | `sum = sum + i` | `sum` (New) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Init | - | - | 0 | - | 0 |
| 1st | 1 | True | 0 | `0 + 1` | 1 |
| 2nd | 2 | True | 1 | `1 + 2` | 3 |
| 3rd | 3 | True | 3 | `3 + 3` | 6 |
| 4th | 4 | False | 6 | - | 6 (Exit) |

---

---

## **2. Methods: Organizing Your Code**

Don't write everything in the `main` method. Break your code into reusable "functions" or "methods".

```java
public class Calculator {
    // A method to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int sum = add(10, 20);
        System.out.println("The sum is: " + sum);
    }
}
```

---

## **3. Logical Practice: FizzBuzz**

This is a classic logic building exercise. 

**Task:** Print numbers from 1 to 50. 
- If divisible by 3, print "Fizz".
- If divisible by 5, print "Buzz".
- If divisible by both, print "FizzBuzz".

```java
for (int i = 1; i <= 50; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        System.out.println("FizzBuzz");
    } else if (i % 3 == 0) {
        System.out.println("Fizz");
    } else if (i % 5 == 0) {
        System.out.println("Buzz");
    } else {
        System.out.println(i);
    }
}
```

---

## **4. Why Java?**

Zoho prefers Java (or C/C++) because:
1. **Strong Typing:** Helps catch errors early.
2. **OOP Support:** Essential for Round 4 (Application Development).
3. **In-Memory Speed:** Efficient for complex logic rounds.

---

## **🎯 Exercise for You:**
Write a method `isPrime(int n)` that returns `true` if a number is prime and `false` otherwise. Then, use a loop to print all prime numbers between 1 and 100.

[Next Step: Arrays & Strings (The Meat of Zoho Interviews) ->](../1_DSA/Searching_Sorting.md)
