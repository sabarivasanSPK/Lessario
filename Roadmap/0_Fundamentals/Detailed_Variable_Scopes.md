# **Phase 0: Variable Scopes & Memory (Detailed)**

In Zoho's Round 1, you will often see code like: "What is the output of this static block?" To answer, you must understand where variables "live" and when they "die."

---

## **1. Local Variables**
Variables declared inside a method or a block `{ }`.
- **Scope:** Only accessible inside that block.
- **Lifetime:** Born when block starts, destroyed when block ends.
- **Initialization:** Must be initialized before use! (Common Round 1 trick).

```java
public void myMethod() {
    int x = 10; // Local variable
    System.out.println(x);
}
// System.out.println(x); // ERROR! x doesn't exist here.
```

---

## **2. Instance Variables (Global to the Class)**
Variables declared inside a class but outside any method.
- **Scope:** Accessible by all methods in the class.
- **Lifetime:** Lives as long as the **Object** lives in the Heap memory.
- **Initialization:** Automatically initialized to default values (0, null, false).

```java
class Student {
    String name; // Instance variable (Default: null)
    int age;     // Instance variable (Default: 0)
}
```

---

## **3. Static Variables (Class Variables)**
Variables declared with the `static` keyword.
- **Scope:** Shared by ALL objects of that class.
- **Lifetime:** Born when class is loaded, dies when program ends.
- **Memory:** Stored in the **Method Area** (not Heap).

```java
class ZohoEmployee {
    static String company = "Zoho"; // Shared by everyone
    String name; // Unique to each employee
}
```

---

## **4. The "Static Block" Mystery**
Zoho loves to ask about the order of execution.

```java
class Test {
    static {
        System.out.println("1. Static Block runs first (once)");
    }
    
    {
        System.out.println("2. Instance Block runs second (on object creation)");
    }
    
    Test() {
        System.out.println("3. Constructor runs last");
    }
    
    public static void main(String[] args) {
        new Test();
    }
}
```

---

## **5. Shadowing (Common Interview Trap)**
What happens if a local variable has the same name as an instance variable?

```java
class Demo {
    int x = 10;
    
    void printX() {
        int x = 20; // Local variable 'shadows' the instance variable
        System.out.println(x); // Prints 20
        System.out.println(this.x); // Prints 10 (using 'this' keyword)
    }
}
```

---

## **🎯 Exercise for You:**
Predict the output:
```java
class Counter {
    static int count = 0;
    Counter() {
        count++;
        System.out.println(count);
    }
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
    }
}
```
(Hint: Static variables are shared!)

[Back to Basic Concepts ->](../0_Fundamentals/Basic_Concepts.md)
