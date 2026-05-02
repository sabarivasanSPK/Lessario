# **Phase 2: Advanced String Manipulation (No Regex!)**

In Zoho interviews, you are often forbidden from using high-level tools like `String.split()` or Regex. They want to see you work with **character arrays** and **ASCII values**.

---

## **1. Working with ASCII Values**
Every character has a numeric value. 
- `'A' - 'Z'` : 65 - 90
- `'a' - 'z'` : 97 - 122
- `'0' - '9'` : 48 - 57

### **Trick: Case Conversion**
To convert 'A' to 'a' without `toLowerCase()`:
```java
char upper = 'A';
char lower = (char) (upper + 32); // 65 + 32 = 97 ('a')
```

---

## **2. The "String Compression" Problem**
**Problem:** Input: "aaabbccd", Output: "a3b2c2d1".

### **Detailed Logic:**
1. Initialize a `StringBuilder`.
2. Loop through the string.
3. Keep a `count` for the current character.
4. If the next character is different, append `char + count` and reset `count`.

```java
public String compress(String s) {
    if (s.length() == 0) return "";
    StringBuilder sb = new StringBuilder();
    int count = 1;
    for (int i = 0; i < s.length(); i++) {
        if (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
            count++;
        } else {
            sb.append(s.charAt(i)).append(count);
            count = 1;
        }
    }
    return sb.toString();
}
```

---

## **3. Substring Search (Manual `indexOf`)**
How do you find if "Zoho" exists in "Welcome to Zoho Corporation" without `contains()`?

### **The Two-Pointer Logic:**
1. Loop through the Main String (`i`).
2. If `Main[i] == Pattern[0]`, start a second loop (`j`).
3. Check if subsequent characters match.
4. If `j` reaches the end of the Pattern, you found it!

---

## **4. String Decoding (The "Expansion" Problem)**
**Problem:** Input: "a3b1c2", Output: "aaabcc".

**Advanced Version:** Input: "3(ab)2(c)", Output: "abababcc".
*Logic:* Use a **Stack** to handle the brackets.

---

## **🎯 Exercise for You:**
1. **Reverse Words in a String:** Input: "I Love Zoho", Output: "Zoho Love I". (Note: Don't use `split()`).
2. **First Non-Repeating Character:** Find the first character that appears only once in a string. (Use a frequency array of size 256).

[Back to Logic Puzzles ->](../2_Zoho_Round_Specific/Logic_Puzzles.md)
