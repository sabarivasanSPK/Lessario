# **Phase 10: Version Control - GitHub Workflow**

GitHub is the "Social Network" for code. It adds collaboration features on top of Git.

---

## **1. Pull Requests (PRs)**
A Pull Request is a way to say: *"I have finished this feature, please review it and merge it into the main project."*

**The Workflow:**
1. **Push** your branch to GitHub: `git push origin feature-name`.
2. Go to GitHub.com and click **"New Pull Request."**
3. Add a description of what you changed.
4. Wait for a "Code Review" from a teammate.

---

## **2. Forking and Cloning**
- **Forking:** Creating a copy of someone else's project on your own GitHub account.
- **Cloning:** Downloading a repository (yours or a fork) to your local laptop.
```bash
git clone https://github.com/username/repository.git
```

---

## **3. Issues and Project Boards**
GitHub allows you to track bugs and tasks using **Issues**.
- You can assign an issue to yourself.
- When you commit code that fixes an issue, you can say `"Fixes #12"` in your commit message to close it automatically.

---

## **4. GitHub Actions (CI/CD)**
GitHub can automatically run tests or deploy your app every time you push code. This is called **Continuous Integration**.

---

## **🎯 Exercise for You:**
1. Find an open-source project on GitHub.
2. **Fork** it to your account.
3. **Clone** it to your laptop.
4. Explore the code and try to find where the "Main" entry point of the app is.

[Next Step: Git Best Practices ->](./Best_Practices.md)
