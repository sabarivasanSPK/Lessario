# **Mobile: Flutter Widgets Deep Dive**

In Flutter, the UI is a tree of widgets. Understanding which widget to use for which purpose is key to building smooth apps.

---

## **1. Basic Widgets**
- **Text:** Displaying strings with custom styles.
- **Image:** Loading assets from the web or local storage.
- **Icon:** Using pre-built Material or Cupertino icons.

---

## **2. Layout Widgets**
- **Container:** The "Swiss Army Knife." Can have padding, margins, borders, and background colors.
- **Column & Row:** Aligning items vertically or horizontally.
- **Stack:** Layering widgets on top of each other (e.g., text over an image).
- **ListView:** For scrollable lists. **Tip:** Use `ListView.builder` for long lists to save memory.

---

## **3. Interactive Widgets**
- **ElevatedButton:** A standard push button.
- **TextField:** For user input.
- **GestureDetector:** Make any widget clickable or draggable.

---

## **4. The "Everything is a Widget" Philosophy**
Even "Padding" and "Center" are widgets in Flutter. 

```dart
Center(
  child: Padding(
    padding: EdgeInsets.all(20.0),
    child: Text('Hello Zoho'),
  ),
)
```

---

## **🎯 Exercise for You:**
Build a **Contact Card** widget.
1. Use a `Row` to hold a circular profile image and a `Column`.
2. Inside the `Column`, put the contact's name and phone number.
3. Wrap the whole thing in a `Card` widget for a professional look.
