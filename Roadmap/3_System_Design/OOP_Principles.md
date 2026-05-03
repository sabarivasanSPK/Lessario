# **Phase 3: OOP Principles for System Design**

In Round 4, you aren't just solving a problem; you are building a **System**. To pass, your code must be modular, reusable, and easy to read.

---

## **1. The Four Pillars of OOP**

| Pillar | Definition | Why Zoho cares? |
| :--- | :--- | :--- |
| **Encapsulation** | Hide data using `private` and use `getters/setters`. | Protects user data in an ATM system. |
| **Abstraction** | Hide complex details. Use `abstract` classes or `interfaces`. | Hides payment gateway logic from the Main app. |
| **Inheritance** | Reuse code from a parent class. | A `Bus` and `Car` both inherit from `Vehicle`. |
| **Polymorphism** | Methods with same name but different behavior. | `calculateFare()` works differently for `AC` vs `Non-AC`. |

---

## **2. Modular Design: The Secret to Round 4**

**Don't put everything in one class!** Break it down:

1. **Model Classes:** Just store data (e.g., `User`, `Train`, `Ticket`).
2. **Service/Manager Classes:** Handle logic (e.g., `BookingManager`, `AccountManager`).
3. **Main/App Class:** Handles user input and displays the menu.

---

## **3. Using Collections for In-Memory Storage**

Since you can't use databases in Round 4, use Java Collections:

```java
List<User> users = new ArrayList<>();
Map<Integer, Train> trainMap = new HashMap<>();
```

---

## **4. Pro-Tips for System Design**
- **Follow Naming Conventions:** `BookingService` is better than `BService`.
- **Handle Edge Cases:** What if the user enters a negative amount? What if the train is already full?
- **DRY (Don't Repeat Yourself):** If you find yourself writing the same code twice, put it in a method.

---

## **🎯 Exercise for You:**
Design a class structure for a **Library Management System**. 
- What are the entities? (Book, Member, Transaction)
- What are the methods? (issueBook, returnBook, calculateFine)

[Next Step: Project - Railway Reservation System ->](../3_System_Design/Project_Railway_Reservation.md)
