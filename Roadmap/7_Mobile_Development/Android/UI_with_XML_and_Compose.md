# **Mobile: Android UI (XML vs. Compose)**

Android UI development is currently in a transition phase. You need to know both!

---

## **1. Traditional XML Layouts**
The "Old" way. You define UI in XML files and link them to Java/Kotlin code.
- **View Hierarchy:** A tree of UI elements (Button, TextView, etc.).
- **ConstraintLayout:** The most powerful way to align elements without nesting too many views.

---

## **2. Jetpack Compose**
The "New" way. You build UI entirely in Kotlin code using functions.
- **Declarative:** You describe **what** the UI should look like, not **how** to change it.
- **State-driven:** When data changes, the UI automatically "recomposes."

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!", color = Color.Blue)
}
```

---

## **3. Comparison**

| Feature | XML | Jetpack Compose |
| :--- | :--- | :--- |
| **Language** | XML + Kotlin/Java | Pure Kotlin |
| **Preview** | Static Layout Editor | Live Interactive Preview |
| **Boilerplate** | High (`findViewById`) | Low |

---

## **🎯 Exercise for You:**
1. Build a **Login Screen** in XML using `ConstraintLayout`.
2. Build the **same screen** in Jetpack Compose using `Column`, `TextField`, and `Button`.
