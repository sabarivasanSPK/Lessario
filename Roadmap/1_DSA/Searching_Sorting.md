# **Phase 1: Searching & Sorting**

Searching and Sorting are foundational. While you might use built-in methods in real life, Zoho expects you to know how they work "under the hood."

---

## **1. Searching Algorithms**

### **Linear Search**
Check every element one by one.
- **Time Complexity:** O(N) - Linear time.
- **Space Complexity:** O(1) - No extra space.
- **Use case:** Unsorted data, small arrays.

### **Binary Search (The Gold Standard)**
Works only on **sorted** data. It cuts the search space in half each time.
- **Time Complexity:** O(log N) - Extremely fast! (Searching 1 billion elements takes only 30 steps).
- **Space Complexity:** O(1) for iterative, O(log N) for recursive.

```java
public static int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

---

## **2. Sorting Algorithms**

### **A. Selection Sort** (Simple but slow)
Find the smallest element in the unsorted part and swap it to the front.
- **Time:** O(N²) in all cases.
- **Space:** O(1).
- **Step-by-step:** `{5, 2, 8, 1}` -> `{1, 2, 8, 5}` -> `{1, 2, 8, 5}` -> `{1, 2, 5, 8}`.

### **B. Merge Sort** (Fast and reliable)
Uses "Divide and Conquer." It splits the array into two, sorts them, and merges them back.
- **Time:** O(N log N) in all cases.
- **Space:** O(N) - Needs extra space for merging.
- **The "Divide" Step:** Split array in the middle until size = 1.
- **The "Merge" Step:** Take two sorted lists and combine them into one sorted list.

> [!IMPORTANT]
> **Stable vs Unstable:** Merge Sort is **Stable** (preserves order of equal elements). Selection Sort is **Unstable**. Zoho interviewers often ask this!

---

## **3. Zoho Special: Custom Sorting**

Zoho often asks you to sort based on special criteria.

**Example:** Sort an array based on the frequency of elements. If frequencies are equal, sort by the number itself.
- Input: `{2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}`
- Output: `{3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}`

---

## **🎯 Exercise for You:**
1. Implement **Bubble Sort** and explain why it is inefficient for large datasets.
2. Given a sorted array that has been rotated (e.g., `{4, 5, 6, 7, 0, 1, 2}`), find the index of a target element using Binary Search.

[Next Step: Stacks, Queues, and Linked Lists ->](../1_DSA/Stacks_Queues_LinkedLists.md)
