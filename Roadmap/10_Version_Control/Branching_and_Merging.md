# **Phase 10: Version Control - Branching & Merging**

In a real job (like at Zoho), you never work directly on the `main` code. You create a "Branch" (a copy), do your work, and then "Merge" it back.

---

## **1. What is a Branch?**
Imagine you are building a Login system while your friend is building a Profile page. You both create separate branches so your code doesn't mix until it's ready.

### **Create and Switch to a Branch**
```bash
git checkout -b feature-login
```

### **Switch Back to Main**
```bash
git checkout main
```

---

## **2. Merging Changes**
Once your feature is finished, you merge it into the main branch.
1. Switch to `main`.
2. Merge the feature branch.
```bash
git checkout main
git merge feature-login
```

---

## **3. Handling Merge Conflicts**
Sometimes, two people change the same line in the same file. Git won't know which one to keep and will ask you to fix a "Conflict."

**How to fix it:**
1. Open the conflicted file in VS Code.
2. You will see markers like `<<<<<<< HEAD` and `>>>>>>> feature-login`.
3. Choose the code you want to keep and delete the markers.
4. `git add .` and `git commit` to finish the merge.

---

## **🎯 Exercise for You:**
1. Create a branch called `test-branch`.
2. Add a line of code in that branch and commit it.
3. Switch back to `main` and try to merge `test-branch`.
4. Delete the branch after merging: `git branch -d test-branch`.

[Next Step: GitHub Workflow ->](./GitHub_Workflow.md)
