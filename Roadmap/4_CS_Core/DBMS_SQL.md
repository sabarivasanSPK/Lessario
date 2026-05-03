# **Phase 4: DBMS & SQL**

Even if you code in Java, Zoho expects you to understand how data is stored persistently.

---

## **1. Core DBMS Concepts**

- **ACID Properties:** Atomicity, Consistency, Isolation, Durability.
- **Normalization:** 1NF, 2NF, 3NF (Goal: Reduce redundancy).
- **Keys:** 
    - **Primary Key:** Unique identifier for a row.
    - **Foreign Key:** Link between two tables.
    - **Composite Key:** Combination of two or more columns as a primary key.

---

## **2. SQL Mastery**

You should be able to write queries for the following:

### **A. Joins (Very Important)**
- **Inner Join:** Common records in both tables.
- **Left Join:** All from left table + matches from right.

### **B. Aggregate Functions**
- `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`.
- Use `GROUP BY` to categorize results.

### **C. Example Query**
Find the second highest salary from an Employee table:
```sql
SELECT MAX(Salary) 
FROM Employee 
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
```

---

## **3. NoSQL vs SQL**
Understand when to use a Relational DB (like MySQL) vs a Document DB (like MongoDB). (Hint: Zoho uses their own custom DBs for many products, so core logic is what matters!).

---

## **🎯 Exercise for You:**
Write a query to find all employees who joined in the last 6 months and have a salary greater than the average salary of their department.

[Next Step: OS & Networking ->](../4_CS_Core/OS_Networking.md)
