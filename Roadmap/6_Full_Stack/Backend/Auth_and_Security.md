# **Full Stack: Authentication & Security**

Security is paramount at Zoho. You are handling customer data, and you must protect it.

---

## **1. JWT (JSON Web Tokens)**
JWT is the standard for stateless authentication in modern web apps.

**How it works:**
1. User logs in.
2. Server validates credentials and sends back a **Signed Token**.
3. User sends that token in the `Authorization` header for all subsequent requests.
4. Server verifies the signature without checking the database.

---

## **2. Secure Password Hashing**
**NEVER** store passwords as plain text. If your database is leaked, everyone's account is compromised.

- **Bcrypt:** Use Bcrypt with a "salt" to hash passwords.
```javascript
const bcrypt = require('bcrypt');
const hash = await bcrypt.hash(myPassword, 10);
```

---

## **3. OWASP Top 10 (Basics)**
Understand these common attacks:
- **SQL Injection:** Escaping user input to prevent malicious queries.
- **XSS (Cross-Site Scripting):** Sanitize data before rendering it in the browser.
- **CSRF:** Use tokens to ensure requests come from your own site.

---

## **4. HTTPS & SSL**
Always use HTTPS to encrypt data in transit. This prevents "Man-in-the-middle" attacks.

---

## **🎯 Exercise for You:**
Implement a simple login route in Node/Express that:
1. Takes an email and password.
2. Compares the hashed password using Bcrypt.
3. If valid, generates a JWT signed with a secret key.
