# GitHub Setup — Push Your Course to GitHub

Follow these steps once to connect this folder to GitHub.

---

## Step 1: Initialize Git

Open a terminal in your `python-mastery-course` folder and run:

```bash
cd /c/Users/willg/python-mastery-course   # or wherever the folder is

git init
git add .
git commit -m "feat: initial course setup — Python Mastery AI110 track"
```

---

## Step 2: Create the GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it: `python-mastery-course`
3. Set it to **Public** (so it becomes your portfolio)
4. **Do NOT** check "Add README" or "Add .gitignore" — we already have those
5. Click **Create repository**

---

## Step 3: Connect and Push

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/python-mastery-course.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 4: Verify

Go to `https://github.com/YOUR_USERNAME/python-mastery-course` — you should see all your files.

---

## Your Daily Workflow From Now On

```bash
# Before working
git pull origin main

# After completing something
git add .
git commit -m "Module X: [what you completed]"
git push origin main
```

---

## Pinning the Repo to Your Profile

1. Go to your GitHub profile page
2. Click **Customize your pins**
3. Pin `python-mastery-course`

This makes it visible to recruiters and interviewers.

---

## GitHub Profile README (Optional but Recommended)

Create a repo named exactly YOUR_USERNAME (same as your GitHub username).
Add a README.md to it — GitHub will display it on your profile.

Example:
```markdown
# Hi, I'm [Your Name]
AI @ CodePath | Python Developer

Currently working through:
- Python fundamentals → AI/ML engineering
- RAG systems, agentic AI, LLM APIs

Projects:
- [Python Mastery Course](link) — structured learning path
```
