# Capstone: End-to-End AI Application

> **Skills used:** Everything — Python, DS&A, OOP, NumPy/Pandas, ML, Deep Learning, RAG, Agentic AI, Guardrails
> **Estimated time:** 1-2 weeks
> **This is your portfolio piece**

## Goal
Build a complete, production-quality AI application that demonstrates everything you've learned.

## Choose Your Project

### Option A: AI Study Assistant
A RAG-powered assistant that:
- Loads your course notes and documents
- Answers questions about the material
- Generates practice questions
- Tracks what topics you're weak on
- Uses agentic workflows to search the web for supplemental info

### Option B: Code Review Bot
An AI agent that:
- Takes a GitHub PR URL
- Fetches the code changes
- Reviews for bugs, style issues, security problems
- Suggests specific improvements
- Has guardrails to ensure constructive feedback

### Option C: ML Model Monitor
A system that:
- Trains an ML model on a dataset of your choice
- Monitors prediction quality over time
- Detects data drift
- Uses an LLM to generate a plain-English report of model health
- Sends alerts when performance degrades

### Option D: Your Own Idea
Requirements:
- Uses Python (of course)
- Has a data component (ML, data analysis, or RAG)
- Uses an LLM API
- Has proper error handling and guardrails
- Is properly tested (at least 10 tests)
- Has a clear README with setup instructions

---

## Capstone Requirements (All Options)

### Code Quality
- [ ] Organized into modules (no 500-line single files)
- [ ] All functions have docstrings
- [ ] Type hints throughout
- [ ] No hardcoded secrets (use environment variables)
- [ ] .gitignore properly configured

### Testing
- [ ] At least 10 pytest tests
- [ ] Tests cover happy path, edge cases, and error cases
- [ ] All tests pass: `pytest tests/ -v`

### Git/GitHub
- [ ] Proper commit history (one feature per commit)
- [ ] Commit messages follow convention
- [ ] README with: what it is, how to install, how to run, examples

### Documentation
- [ ] README explains the problem and solution
- [ ] Architecture diagram or explanation
- [ ] Example usage (with screenshots or output)
- [ ] Known limitations

---

## Deliverables

1. **GitHub Repository** — public, with full commit history
2. **Demo** — either a video walkthrough or live demo
3. **Reflection** — 1-page markdown: what you learned, what was hard, what you'd improve

---

## Commit Convention for Capstone
```bash
git commit -m "feat: initial project structure"
git commit -m "feat(rag): implement document indexing with ChromaDB"
git commit -m "feat(api): add LLM integration with guardrails"
git commit -m "test: add pytest suite for RAG retrieval"
git commit -m "docs: complete README with setup and examples"
```

---

*Complete your capstone and you're ready for real AI engineering roles.*
