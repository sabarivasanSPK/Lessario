# **Phase 10: Version Control - Git Basics**

Version control is like a "Time Machine" for your code. It allows you to save versions of your project and go back to them if something breaks.

---

## **1. Initial Setup**
Before you start, you need to tell Git who you are.
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## **2. The Basic Workflow**

### **Step 1: Initialize**
Create a new Git repository in your project folder.
```bash
git init
```

### **Step 2: Track Changes (Staging)**
Tell Git which files you want to include in the next "Save."
```bash
git add filename.js   # Add a specific file
git add .             # Add ALL files in the current folder
```

### **Step 3: Save (Commit)**
Create a permanent snapshot of the staged changes.
```bash
git commit -m "Add a descriptive message here"
```

---

## **3. Checking Status**
You can always see what’s happening in your repository with these commands:
- `git status`: See which files are modified or staged.
- `git log`: See a history of all your past commits.

---

## **4. Connecting to GitHub (Remote)**
To save your code online, you need to link your local folder to a GitHub repository.
```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

---

## **🎯 Exercise for You:**
1. Create a new folder called `Git_Test`.
2. Inside it, create a file called `hello.txt`.
3. Initialize Git, add the file, and make your first commit with the message "Initial commit".
4. Change the text in `hello.txt` and make a second commit. Use `git log` to see both versions!

[Next Step: Branching & Merging ->](./Branching_and_Merging.md)
