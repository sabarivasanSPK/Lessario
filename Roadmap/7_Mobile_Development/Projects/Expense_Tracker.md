# **Project: Expense Tracker (Mobile)**

A practical app to track daily spending. This project focuses on **Local Storage** and **CRUD** (Create, Read, Update, Delete) operations.

---

## **1. Requirements**
- **Add Expense:** Input for Amount, Category (Food, Travel, etc.), and Date.
- **List View:** Show all expenses in a scrollable list.
- **Total Balance:** Display the sum of all expenses at the top.
- **Delete:** Swipe to delete an entry.

---

## **2. Tech Stack**
- **Android:** Kotlin + Room Database.
- **iOS:** Swift + CoreData.
- **Cross-Platform:** Flutter + Sqflite or Hive.

---

## **3. Key Concept: Local Database**
You don't want to lose data when the app closes.
- Use a **DAO** (Data Access Object) to handle database queries.
- Use a **ViewModel** to keep the data alive during screen rotations.

---

## **4. Step-by-Step Build**
1. **Model:** Create an `Expense` class with fields for ID, Amount, and Category.
2. **DB:** Set up the local database to store `Expense` objects.
3. **UI:** Build a list using `RecyclerView` (Android) or `ListView` (Flutter).
4. **Input:** Create a "Floating Action Button" that opens a dialog to add an expense.

---

## **🎯 Challenge for You:**
Add a **Pie Chart** to visualize which category you spend the most on.
