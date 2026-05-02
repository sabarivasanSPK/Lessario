# **Full Stack: React.js Deep Dive**

React is a library for building user interfaces. It's based on **Components**—small, reusable pieces of UI.

---

## **1. Components & Props**
Every piece of UI in React is a component.
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

---

## **2. State & Hooks**
State is "data that changes over time." Hooks are functions that let you "hook into" React state.

### **useState**
```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Clicked {count} times
    </button>
  );
}
```

### **useEffect**
Used for "side effects" like fetching data or setting up a subscription.
```jsx
useEffect(() => {
  fetchData();
}, []); // Empty array means "run once on mount"
```

---

## **3. The Virtual DOM**
React doesn't update the whole page when something changes. It creates a "Virtual DOM" (a copy), compares it with the real one, and only updates the parts that changed. This is why React is so fast.

---

## **4. Conditional Rendering**
```jsx
{isLoggedIn ? <LogoutButton /> : <LoginButton />}
```

---

## **🎯 Exercise for You:**
Build a **Searchable Product List**.
1. Create a list of Zoho products.
2. Add a search bar.
3. As the user types, the list should filter to show only matching products.
