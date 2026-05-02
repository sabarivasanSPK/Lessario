# **MERN: Integrating Frontend & Backend**

This is where the magic happens. We connect our React UI to our Express API.

---

## **1. CORS (Cross-Origin Resource Sharing)**
By default, a browser won't let your React app (on port 3000) talk to your Node app (on port 5000). You must enable CORS on the server.

```javascript
const cors = require('cors');
app.use(cors());
```

---

## **2. Fetching Data with Axios**
Axios is a popular library for making HTTP requests in React.

```jsx
import axios from 'axios';

const fetchTasks = async () => {
    const response = await axios.get('http://localhost:5000/api/tasks');
    setTasks(response.data);
};
```

---

## **3. The "Full Cycle" Example (Add Task)**
1. **React:** User types a task and clicks "Add".
2. **React:** `axios.post('/api/tasks', { title: "New Task" })` is called.
3. **Node:** `app.post('/api/tasks', ...)` receives the data and saves it to MongoDB.
4. **Node:** Sends back the saved task as JSON.
5. **React:** Receives the new task and updates the state (UI refreshes).

---

## **4. Environment Variables in MERN**
- **Server:** Use `.env` for MongoDB URI and Secret Keys.
- **Client:** Use `.env` to store the Base URL of your API (e.g., `REACT_APP_API_URL`).

---

## **🎯 Exercise for You:**
Build a **MERN Task List**.
1. Set up a Node/Express backend that serves a list of tasks from MongoDB.
2. Build a React frontend that fetches those tasks and displays them in a list.
3. Add a button in React that sends a `DELETE` request to the backend to remove a task.
