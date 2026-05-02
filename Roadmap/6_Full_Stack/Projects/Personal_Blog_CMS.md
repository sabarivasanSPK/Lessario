# **Project: Personal Blog CMS (Full Stack)**

Create a Content Management System (CMS) where you can write, edit, and delete blog posts, and users can read them.

---

## **1. Requirements**
- **Admin Panel:** A secure area to write new posts (Title, Body, Tags).
- **Public Feed:** A homepage that lists all blog posts in chronological order.
- **Single Post View:** Click a title to read the full post.
- **Rich Text:** (Bonus) Use a library like `Quill` or `Draft.js` for styling text.

---

## **2. Tech Stack**
- **Frontend:** React or Vue.
- **Backend:** Node.js + Express.
- **Database:** MongoDB (Great for flexible blog content).

---

## **3. Key Concept: CRUD Operations**
This project is the ultimate test of CRUD:
- **C**reate: `POST /api/posts`
- **R**ead: `GET /api/posts` and `GET /api/posts/:id`
- **U**pdate: `PUT /api/posts/:id`
- **D**elete: `DELETE /api/posts/:id`

---

## **4. Step-by-Step Build**
1. **Model:** Define a `BlogPost` schema.
2. **API:** Build the 4 CRUD routes.
3. **Frontend Admin:** Build a form to submit new posts.
4. **Frontend Feed:** Use `.map()` to display a list of cards for each post.

---

## **🎯 Challenge for You:**
Add a **Comments** section at the bottom of each post so users can leave feedback.
