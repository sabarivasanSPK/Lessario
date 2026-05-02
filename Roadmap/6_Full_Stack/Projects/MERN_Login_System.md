# **Project: MERN Login System**

This is the "Gold Standard" project for any MERN developer. You will build a system that allows users to register and log in securely.

---

## **1. What You Will Learn**
- Password hashing with **Bcrypt**.
- Stateless authentication with **JWT (JSON Web Tokens)**.
- Securely storing tokens in the browser (**LocalStorage**).
- Protecting "Private Routes" in React.

---

## **2. The Backend (Node/Express)**

### **Step 1: User Model**
Create a schema that hashes the password before saving.
```javascript
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const UserSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

UserSchema.pre('save', async function(next) {
    if (!this.isModified('password')) return next();
    this.password = await bcrypt.hash(this.password, 10);
});
```

### **Step 2: Auth Controller**
Implement a `POST /login` route that returns a JWT.
```javascript
const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
res.json({ token, user: { email: user.email } });
```

---

## **3. The Frontend (React)**

### **Step 3: Login Form**
A simple form that sends data to your API using Axios.
```jsx
const handleLogin = async (e) => {
    e.preventDefault();
    const res = await axios.post('/api/login', { email, password });
    localStorage.setItem('token', res.data.token);
    // Redirect to Dashboard
};
```

### **Step 4: Private Routes**
Check if a token exists in `localStorage` before showing a page.
```jsx
const ProtectedRoute = ({ children }) => {
    const token = localStorage.getItem('token');
    return token ? children : <Navigate to="/login" />;
};
```

---

## **4. Step-by-Step Build Order**
1. **Setup:** Create a new folder, init `npm`, and install `express`, `mongoose`, `cors`, `jsonwebtoken`, `bcryptjs`.
2. **Database:** Connect to MongoDB Atlas.
3. **Register:** Create a route to save a new user.
4. **Login:** Create a route to verify the user and send a JWT.
5. **UI:** Build the Login and Dashboard screens in React.
6. **Connect:** Use Axios to link the UI to your API.

---

## **🎯 Challenge for You:**
Implement a **"Logout"** button that clears the token from `localStorage` and redirects the user to the Login page.
