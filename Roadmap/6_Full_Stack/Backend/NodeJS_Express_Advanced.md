# **Full Stack: Advanced Node.js & Express**

Building a basic server is easy; building a production-ready server requires handling errors, middleware, and data processing.

---

## **1. Custom Middleware**
Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the `next` function in the application’s request-response cycle.

```javascript
const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url} - ${new Date()}`);
  next(); // Don't forget this!
};

app.use(logger);
```

---

## **2. Global Error Handling**
Don't let your app crash on every error. Use a central error handler.

```javascript
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    message: "Something went wrong!",
    error: err.message
  });
});
```

---

## **3. File Uploads (Multer)**
Processing images or documents sent by the user.

```javascript
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

app.post('/profile', upload.single('avatar'), (req, res) => {
  // req.file contains the uploaded file info
  res.send("File uploaded!");
});
```

---

## **4. Environment Variables**
Store your secrets (API keys, DB passwords) in a `.env` file and use the `dotenv` package.
```javascript
require('dotenv').config();
const dbPassword = process.env.DB_PASSWORD;
```

---

## **🎯 Exercise for You:**
Build a **Logging Middleware** that saves every incoming request's method and URL into a local `access.log` file using the Node `fs` (FileSystem) module.
