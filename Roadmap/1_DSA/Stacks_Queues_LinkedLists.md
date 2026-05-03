# **Phase 1: Stacks, Queues & Linked Lists**

When arrays aren't enough, we use dynamic data structures. Zoho often asks you to implement these from scratch without using the built-in `java.util` classes.

---

## **1. Linked Lists: The Chain**

Unlike arrays, elements (nodes) are stored anywhere in memory. Each node points to the next one.

### **Node Structure**
```java
class Node {
    int data;
    Node next;
    Node(int d) { data = d; next = null; }
}
```

### **Common Zoho Question: Reverse a Linked List**
```java
public Node reverse(Node head) {
    Node prev = null, current = head, next = null;
    while (current != null) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
```

---

## **2. Stacks: LIFO (Last-In, First-Out)**

Think of a stack of plates. You add to the top and take from the top.
- **Operations:** `push()`, `pop()`, `peek()`.

### **Zoho Question: Balanced Parentheses**
Check if `((()))` is balanced. Use a stack to push `(` and pop when you see `)`.

---

## **3. Queues: FIFO (First-In, First-Out)**

Think of a line at a ticket counter. The first person in is the first person out.
- **Operations:** `enqueue()`, `dequeue()`.

---

## **4. Why these matter for Zoho?**

In **Round 4 (Application Development)**, you might need to manage a "Waiting List" for a train or a "History" of transactions.
- **Waiting List** -> Queue
- **Undo Operation** -> Stack
- **Dynamic List of Users** -> Linked List

---

## **🎯 Exercise for You:**
1. Implement a **Queue** using two **Stacks**.
2. Write a function to find the **middle element** of a linked list in a single pass.

[Next Step: Zoho Round 2 Specialist (Pattern Printing) ->](../2_Zoho_Round_Specific/Pattern_Printing.md)
