# **Mobile: Kotlin Fundamentals**

Kotlin is the preferred language for Android development at Zoho. It is expressive, safe, and interoperable with Java.

---

## **1. Null Safety (The Billion Dollar Mistake Fix)**
In Java, `NullPointerException` is a common crash. Kotlin forces you to handle nulls.
```kotlin
var name: String = "Zoho" // Cannot be null
var middleName: String? = null // Can be null

// Safe call
println(middleName?.length) 

// Elvis operator
val len = middleName?.length ?: 0
```

---

## **2. Data Classes**
Used to store data with boilerplate code (toString, equals, hashCode) generated automatically.
```kotlin
data class User(val id: Int, val name: String, val email: String)
```

---

## **3. Coroutines (Async made easy)**
For background tasks like API calls without blocking the UI.
```kotlin
viewModelScope.launch {
    val user = repository.getUser(id) // Suspends here until done
    uiState.value = user // Back on Main thread automatically
}
```

---

## **4. Extension Functions**
Add functionality to existing classes without inheriting from them.
```kotlin
fun String.shout() = this.uppercase() + "!!!"
println("hello".shout()) // HELLO!!!
```

---

## **🎯 Exercise for You:**
Write a Kotlin function that takes a list of integers and returns only the even numbers, sorted in descending order, using functional operators like `.filter()` and `.sortedByDescending()`.
