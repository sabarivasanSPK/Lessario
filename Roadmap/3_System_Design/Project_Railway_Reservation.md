# **Phase 3: Project - Railway Reservation System**

This is the most common Round 4 problem at Zoho. Mastering this will give you a massive advantage.

---

## **1. The Problem Statement**
Build a console application where users can book/cancel tickets.
- **Constraints:** 
    - Total Seats: 60 (20 Upper, 20 Middle, 20 Lower).
    - RAC (Reservation Against Cancellation) Seats: 18.
    - Waiting List: 10.
- **Rules:**
    - Prefer lower berths for seniors (>60) or children (<5).
    - If a preferred berth is not available, allocate any other available berth.
    - If all berths are full, move to RAC.
    - If RAC is full, move to Waiting List.
    - On cancellation, shift passengers from RAC to Berths and Waiting List to RAC.

---

## **2. Modular Structure**

### **A. Passenger Class**
```java
class Passenger {
    static int idCounter = 1;
    int id, age;
    String name, berthPreference, allottedBerth;
    
    Passenger(String name, int age, String bp) {
        this.id = idCounter++;
        this.name = name;
        this.age = age;
        this.berthPreference = bp;
    }
}
```

### **B. TicketBooker Class (The Logic Center)**
Handles the lists of available seats, booked passengers, RAC list, etc.

### **C. Main App Class**
Menu-driven loop:
1. Book
2. Cancel
3. Print Booked Tickets
4. Print Available Tickets
5. Exit

## **3. The Berth Allocation Algorithm (The Core Logic)**

This is where most candidates fail. You need a systematic way to check for seats.

### **Priority 1: Preference Match**
- If preferred berth (e.g., Lower) is available, book it.
- **Zoho Special Rule:** If the passenger is >60 years old, always prioritize Lower Berth even if they didn't ask for it.

### **Priority 2: Any Available Berth**
- If preference is not available, check all other berths (Lower -> Middle -> Upper).

### **Priority 3: RAC (Reservation Against Cancellation)**
- RAC passengers share a side-lower berth (2 people per berth).
- If all 60 berths are full, check if RAC count < 18.

### **Priority 4: Waiting List**
- If RAC is full, check if Waiting List < 10.

---

## **4. The "Cancel & Shift" Logic**
When a ticket is cancelled:
1. If it was a **Confirmed** ticket:
   - Pick the first person from the **RAC list**.
   - Move them to the newly vacant confirmed seat.
   - Pick the first person from the **Waiting List**.
   - Move them to the newly vacant RAC seat.
2. If it was an **RAC** ticket:
   - Move first Waiting List person to RAC.

---

## **5. In-Memory Data Management**
Use `Map<Integer, Passenger>` to store booked tickets for O(1) lookup during cancellation.
Use `Queue<Integer>` for RAC and Waiting List to ensure Fairness (First-Come, First-Served).

---

## **🎯 Challenge for You:**
Try to implement this system without looking at online solutions. Focus on the **Berth Allocation** logic first.

[Next Step: DBMS & SQL ->](../4_CS_Core/DBMS_SQL.md)
