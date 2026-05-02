# **Full Stack: SQL vs. NoSQL**

Choosing the right database is one of the most important architectural decisions you'll make.

---

## **1. SQL (Relational Databases)**
*Example: MySQL, PostgreSQL, Zoho's Custom SQL.*
- **Structure:** Tables with fixed rows and columns.
- **Schema:** Rigid. You must define it before adding data.
- **Relationships:** Uses "Joins" to connect tables.
- **ACID:** Strict adherence to Atomicity, Consistency, Isolation, and Durability.

**Best for:** Financial systems, e-commerce, or apps where data consistency is critical.

---

## **2. NoSQL (Non-Relational Databases)**
*Example: MongoDB (Document), Redis (Key-Value), Cassandra (Column-family).*
- **Structure:** Flexible documents (like JSON).
- **Schema:** Dynamic. You can add fields on the fly.
- **Relationships:** Usually "Nested" documents or multiple queries.
- **Scalability:** Built to scale horizontally across many servers.

**Best for:** Real-time analytics, content management, or rapidly changing data.

---

## **3. Key Comparison**

| Feature | SQL | NoSQL |
| :--- | :--- | :--- |
| **Scaling** | Vertical (Bigger server) | Horizontal (More servers) |
| **Data Structure** | Structured (Table) | Unstructured (JSON/BSON) |
| **Consistency** | Strong Consistency | Eventual Consistency |
| **Queries** | SQL Language | Varies by DB |

---

## **🎯 Exercise for You:**
1. Design a **SQL Schema** for a Library (Books, Authors, Members).
2. Design a **NoSQL Document** for a Social Media Post (Author info, Content, Tags, Comments).
