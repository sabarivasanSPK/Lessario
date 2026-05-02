# **Phase 7: Mobile Development - Flutter (Cross-Platform)**

- 📑 [Detailed Flutter Widgets Guide](./CrossPlatform/Flutter_Widgets_Detailed.md)

Flutter is Google's UI toolkit for building beautiful, natively compiled applications for mobile, web, and desktop from a single codebase. Zoho uses Flutter for many of its modern applications.

---

## **1. The Dart Language**

Before Flutter, you must know **Dart**.
- **Statically Typed:** Like Java/C++.
- **Asynchronous:** `Future` and `Stream`.
- **Everything is an Object.**

---

## **2. Widgets, Widgets, Widgets**

In Flutter, the UI is built entirely out of Widgets.
- **StatelessWidget:** For UI that doesn't change (e.g., a static label).
- **StatefulWidget:** For interactive UI (e.g., a counter or form).
- **Layout Widgets:** `Row`, `Column`, `Stack`, `Container`.

---

## **3. State Management**

This is the most debated topic in Flutter.
- **Provider:** The recommended approach for beginners.
- **Bloc (Business Logic Component):** For large, complex applications.
- **Riverpod:** A modern, more robust version of Provider.

---

## **4. Why Zoho uses Flutter?**
- **Speed:** One codebase for both Android and iOS.
- **Design:** Easy to implement Zoho's custom design language.
- **Performance:** Compiles to ARM machine code, so it's fast.

---

## **🎯 Exercise for You:**
Build a **Currency Converter** app.
1. Fetch exchange rates from an API.
2. Use a `TextField` for input.
3. Update the converted value in real-time as the user types.

[Next Step: AI Engineering Track ->](../8_AI_Engineering/ML_Fundamentals.md)
