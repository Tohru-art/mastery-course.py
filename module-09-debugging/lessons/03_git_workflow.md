# Professional Git Workflow

> CodePath AI110 Goal: "Use professional Git and GitHub workflows to collaborate, document, and contribute to codebases."

---

## The Core Workflow You'll Use Every Day

```
main branch  ──────────────────────────────────────────────→
                   │                           ↑
                   └── feature/your-feature ──┘
                       (do all work here)   (merge via PR)
```

---

## Daily Commands

### Starting a New Feature
```bash
# 1. Make sure main is up to date
git checkout main
git pull origin main

# 2. Create a feature branch
git checkout -b feature/add-rag-pipeline

# 3. Do your work, then commit often
git add module-10-rag-agentic-ai/lessons/01_rag.py
git commit -m "Add RAG pipeline with ChromaDB integration"
```

### Committing (Do This After Every Exercise)
```bash
git status                              # see what changed
git diff                                # see exact changes
git add <specific-file>                 # stage specific file
git add .                               # stage all changes
git commit -m "Module 3: OOP exercises complete"
git push origin feature/your-branch
```

### Keeping Your Branch Up to Date
```bash
git checkout main
git pull origin main
git checkout feature/your-branch
git rebase main                        # replay your commits on top of latest main
```

---

## Commit Message Convention

Use this format — it's what professional teams use:

```
type(scope): short description (max 72 chars)

Optional longer explanation if needed.
```

**Types:**
- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation only
- `test`: adding tests
- `refactor`: code restructure, no behavior change
- `chore`: tooling, dependencies

**Examples:**
```
feat(rag): add semantic search with ChromaDB
fix(module-5): correct pandas groupby exercise test case
test(module-1): add edge case for empty string input
docs(readme): update setup instructions for Windows
```

---

## Pull Request Workflow

```bash
# Push your branch
git push origin feature/add-rag-pipeline

# Create a PR on GitHub
# Title: "feat(module-10): Add RAG pipeline lesson and exercises"
# Description: What you changed, why, and how to test it
```

**Good PR description template:**
```markdown
## What
Added lesson and exercises for RAG (Retrieval-Augmented Generation).

## Why
Module 10 needs to cover RAG as it's in the CodePath AI110 curriculum.

## How to Test
1. pip install chromadb sentence-transformers
2. python module-10-rag-agentic-ai/lessons/01_rag.py
3. python module-10-rag-agentic-ai/exercises/exercises_10.py
```

---

## Code Review Skills

When reviewing someone else's code (or AI-generated code):

**Ask yourself:**
- Does it actually solve the problem?
- Is it readable? Can I understand it without comments?
- Are there edge cases it doesn't handle?
- Are there security issues?
- Is it efficient enough?
- Does it have tests?

**Leave constructive comments:**
```
# Bad comment:
"This is wrong."

# Good comment:
"This will throw a KeyError if 'user_id' isn't in the dict.
Consider using .get('user_id') with a default value."
```

---

## Important Git Safety Rules

```bash
# NEVER do these on main/shared branches:
git push --force             # overwrites remote history
git reset --hard HEAD~3      # deletes commits
git rebase main (on main)    # rewrites shared history

# Always check before destructive operations:
git status                   # what's changed?
git log --oneline -10        # recent commits
git diff HEAD~1              # what's in the last commit?
```

---

## This Course's Git Habit

**Every single session:**
```bash
# Start
git pull origin main

# After completing each exercise
git add module-XX-*/exercises/exercises_XX.py
git commit -m "Module X: exercises complete — all tests pass"

# After completing a lesson
git add module-XX-*/lessons/
git commit -m "Module X: finished [lesson topic] lesson"

# End of session
git push origin main
```

Your GitHub contribution graph is your portfolio. **Commit every day.**
