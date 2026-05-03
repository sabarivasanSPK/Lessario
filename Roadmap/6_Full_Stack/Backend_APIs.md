# **Phase 6: Full Stack Track - Backend & API Design**

The backend is where the data lives and the business logic happens.

---

## **1. Server-Side Technologies**

### **Node.js (JavaScript on the Server)**
- 📑 [Advanced Node & Express Logic](./Backend/NodeJS_Express_Advanced.md)
- **Express.js:** The standard framework for building APIs in Node.
- **Middleware:** Handling authentication, logging, and errors.
- **Asynchronous Programming:** `async/await` and Promises.

### **Java Spring Boot (The Corporate Giant)**
- **Dependency Injection:** Making code modular and testable.
- **Spring Data JPA:** Talking to databases with ease.
- **Security:** Handling OAuth2 and JWT.

---

## **2. RESTful API Design**

When building APIs, follow these "Golden Rules":
1. **Use HTTP Verbs:** `GET` (Read), `POST` (Create), `PUT` (Update), `DELETE` (Delete).
2. **Statelessness:** Every request should contain all the info needed to process it.
3. **JSON:** The standard format for data exchange.
4. **Status Codes:** `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `500 Server Error`.

---

## **3. Authentication & Authorization**

- 🔐 [Auth & Security Deep Dive](./Backend/Auth_and_Security.md)
- **JWT (JSON Web Tokens):** For stateless authentication.
- **OAuth2:** For "Login with Google/Zoho" features.
- **Hashing Passwords:** Never store passwords in plain text! Use `bcrypt`.

---

## **4. Databases (Advanced)**

- **Redis:** For caching frequently used data.
- **Connection Pooling:** Managing DB connections efficiently.
- **Migrations:** How to update your database schema safely.

---

## **🎯 Exercise for You:**
Create a simple **Book Store API** using Node/Express or Spring Boot.
- `GET /books` - List all books.
- `POST /books` - Add a new book (requires authentication).
- `DELETE /books/:id` - Remove a book.

[Next Step: Mobile Development Track ->](../7_Mobile_Development/Android_iOS.md)
