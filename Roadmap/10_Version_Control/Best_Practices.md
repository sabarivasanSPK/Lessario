# **Phase 10: Version Control - Best Practices**

Professional developers follow certain rules to keep their Git history clean and readable.

---

## **1. Atomic Commits**
A commit should represent **one** logical change. 
- ❌ **Bad:** `git commit -m "Fixed login, updated CSS, and added a button"`
- ✅ **Good:** Two separate commits. One for the login fix and one for the UI changes.

---

## **2. Clear Commit Messages**
Follow the **Imperative Mood** (as if you are giving a command).
- ❌ **Bad:** `"I fixed the bug"` or `"fixed bug"`
- ✅ **Good:** `"Fix login crash on empty password field"`

---

## **3. The `.gitignore` File**
You should **NEVER** upload certain files to GitHub, such as:
- **`node_modules/`**: They are too big and can be reinstalled.
- **`.env`**: These contain your secret passwords and API keys.
- **Compiled binaries**: (e.g., `.exe`, `.class` files).

Create a file named `.gitignore` in your root folder and list these files inside it.

---

## **4. Commit Early, Commit Often**
Don't wait until the end of the day to commit. Every time you finish a small part of a feature that works, commit it! This gives you more "Save Points" to go back to if you make a mistake later.

---

## **🎯 Exercise for You:**
1. Create a `.gitignore` file for a Node.js project. It should ignore `node_modules` and `.env`.
2. Practice writing 3 "Atomic" commits for a small task (e.g., adding a new field to a form).
