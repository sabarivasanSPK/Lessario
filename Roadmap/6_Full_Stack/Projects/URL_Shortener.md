# **Project: URL Shortener (Full Stack)**

In this project, you will build a service that takes a long URL and generates a short, clickable link.

---

## **1. Requirements**
- **User Input:** A text box to paste a long URL.
- **Shortening Logic:** Generate a unique 6-character code for each URL.
- **Redirection:** When someone visits `your-app.com/CODE`, they are redirected to the original long URL.
- **Database:** Store the mapping of `Short Code -> Long URL`.

---

## **2. Tech Stack**
- **Frontend:** React or HTML/JS.
- **Backend:** Node.js + Express.
- **Database:** MongoDB or PostgreSQL.

---

## **3. Key Logic: The Shortener**
You can use a library like `nanoid` or create your own logic:
```javascript
const shortid = require('shortid');
const code = shortid.generate(); // e.g., "7e8d35"
```

---

## **4. Step-by-Step Build**
1. **API:** Create a `POST /shorten` route that saves the URL and code.
2. **Redirect:** Create a `GET /:code` route that finds the long URL in the DB and uses `res.redirect()`.
3. **Frontend:** Build a simple form to send the URL to your API and display the result.

---

## **🎯 Challenge for You:**
Add a **Counter** to track how many times each short link has been clicked.
