# **Phase 7: Mobile Development - Native Android & iOS**

Zoho has some of the most downloaded business apps in the world. Being a mobile developer here means working at a massive scale.

---

## **1. Native Android (Java/Kotlin)**

### **The Foundations**
- 📱 [Kotlin Fundamentals Deep Dive](./Android/Kotlin_Fundamentals.md)
- **Activity & Fragment Lifecycle:** Understanding how apps start and stop.
- **Intent & Navigation:** Moving between screens.
- **RecyclerView:** Handling long lists of data efficiently.

### **Language Choice: Kotlin**
While Zoho uses a lot of Java, **Kotlin** is the modern standard for Android.
- Null Safety.
- Coroutines (for background tasks).
- Extension functions.

---

## **2. Native iOS (Swift)**

### **The Foundations**
- **UIKit vs. SwiftUI:** SwiftUI is the modern way to build UIs declaratively.
- **Auto Layout:** Making UIs look good on all iPhone sizes.
- **View Controllers:** The heart of an iOS app.

### **Language: Swift**
- Optionals and Error Handling.
- Protocols and Delegates (The core design pattern of iOS).
- Closures.

---

## **3. Connecting to the Web**

Mobile apps are useless without data.
- **Retrofit (Android) / URLSession (iOS):** Making API calls.
- **JSON Parsing:** Using GSON or Codable.
- **Local Storage:** SQLite or Room (Android) / CoreData (iOS).

---

## **4. Performance & Battery**

Mobile users hate lag and battery drain.
- **Image Caching:** Use Glide or Picasso.
- **Memory Leaks:** Understanding how to avoid `Context` leaks.

---

## **🚀 Mini-Projects for Practice**
- 📱 [Expense Tracker (Mobile)](./Projects/Expense_Tracker.md)
- ☁️ [Weather Forecast App](./Projects/Weather_Forecast_App.md)

## **🎯 Exercise for You:**
Build a **News App** that fetches the latest headlines from a free API (like NewsAPI) and displays them in a list. When a user clicks an item, show the full article details.

[Next Step: Cross-Platform with Flutter ->](./Flutter.md)
