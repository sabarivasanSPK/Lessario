# **Full Stack: Advanced JavaScript (ES6+)**

JavaScript is the engine of the frontend. To build modern apps, you need to move beyond `var` and `function`.

---

## **1. Let, Const, and Scope**
- `let`: Block-scoped, reassignable.
- `const`: Block-scoped, constant (reference cannot change).
- **Rule:** Use `const` by default, `let` only if you need to reassign.

---

## **2. Arrow Functions**
A shorter syntax for writing functions that also handles the `this` keyword more intuitively.
```javascript
const add = (a, b) => a + b;

const sayHello = name => {
    console.log(`Hello, ${name}!`);
};
```

---

## **3. Destructuring & Spread Operator**
```javascript
// Destructuring
const user = { name: "Zoho", age: 25 };
const { name, age } = user;

// Spread
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]
```

---

## **4. Async/Await (Handling Data)**
The modern way to handle asynchronous operations like API calls.
```javascript
const fetchData = async () => {
    try {
        const response = await fetch('https://api.zoho.com/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
};
```

---

## **🎯 Exercise for You:**
Write a function that takes an array of employee objects, filters those with a salary > 50000, and returns a new array of their names using `.filter()` and `.map()`.
