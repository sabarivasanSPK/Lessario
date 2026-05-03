# **Phase 1: Arrays & Strings**

Arrays and Strings are the bread and butter of Zoho interviews. Almost 80% of Round 2 and Round 3 questions revolve around these two data structures.

---

## **1. Arrays: A Row of Boxes**

An array is a collection of similar data types stored in contiguous memory locations.

### **Initialization**
```java
int[] numbers = {10, 20, 30, 40, 50};
String[] names = new String[5]; // Empty array of size 5
```

### **Common Operations**
- **Traversing:** Looking at every element.
- **Reversing:** Changing `{1, 2, 3}` to `{3, 2, 1}`.
- **Searching:** Finding if a number exists.

---

## **2. Strings: Character Arrays with Superpowers**

In Java, Strings are objects, but you can think of them as an array of characters.

### **Crucial String Methods**
```java
String s = "Zoho Corporation";

s.length();          // 16
s.charAt(0);         // 'Z'
s.substring(0, 4);   // "Zoho"
s.toLowerCase();     // "zoho corporation"
s.indexOf('o');      // 1
```

### **String Immutability**
In Java, Strings cannot be changed. If you modify a string, a new one is created. 
**Solution:** Use `StringBuilder` for heavy modifications to save memory.

```java
StringBuilder sb = new StringBuilder("Zoho");
sb.append(" Corp");
System.out.println(sb.toString()); // "Zoho Corp"
```

---

## **3. Practice Problems (Zoho Style)**

### **A. Find the Maximum in an Array**
```java
int[] arr = {1, 5, 3, 9, 2};
int max = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
}
System.out.println("Max is: " + max);
```

### **B. Check if a String is a Palindrome**
(A palindrome reads the same forwards and backwards, like "radar")
```java
public static boolean isPalindrome(String str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        if (str.charAt(left) != str.charAt(right)) return false;
        left++;
        right--;
    }
    return true;
}
```

---

## **🎯 Exercise for You:**
1. Write a program to rotate an array to the right by `k` steps.
2. Given a string, remove all duplicate characters (e.g., "aabbcc" -> "abc").

[Next Step: Searching & Sorting ->](../1_DSA/Searching_Sorting.md)
