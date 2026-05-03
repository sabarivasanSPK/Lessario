# **MERN: MongoDB & Mongoose**

MongoDB is a **NoSQL Document Database**. Instead of tables and rows, it stores data in flexible, JSON-like documents.

---

## **1. MongoDB Atlas (The Cloud)**
We recommend using **MongoDB Atlas** so you don't have to install a database locally on your i3 laptop (saving RAM!).
- Sign up for a free "M0" cluster.
- Get your **Connection String** (e.g., `mongodb+srv://user:pass@cluster.mongodb.net/myDB`).

---

## **2. Mongoose (The Bridge)**
Mongoose is an **ODM** (Object Data Modeling) library for Node.js. It provides a straight-forward, schema-based solution to model your application data.

### **Defining a Schema**
```javascript
const mongoose = require('mongoose');

const TaskSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: String,
    completed: { type: Boolean, default: false },
    createdAt: { type: Date, default: Date.now }
});

const Task = mongoose.model('Task', TaskSchema);
module.exports = Task;
```

---

## **3. Basic Operations**
```javascript
// Connect to DB
mongoose.connect(process.env.MONGO_URI);

// Create a new task
const newTask = new Task({ title: "Learn MERN" });
await newTask.save();
```

---

## **🎯 Exercise for You:**
1. Create a MongoDB Atlas account.
2. Define a `User` schema with fields for `username`, `email`, and `password`.
3. Try to connect to your Atlas cluster using a simple Node.js script.

[Next Step: Backend with Express ->](./Backend_Express_Node.md)
