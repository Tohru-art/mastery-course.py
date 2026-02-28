# Python Mastery — AI @ CodePath Track (AI110)

> **Goal:** Python basics → professional AI engineer, fully aligned with CodePath AI110.
> **Track your progress:** Check off topics as you complete them. Commit after every module.

---

## CodePath AI110 Objectives → Where They're Covered

| AI110 Learning Goal | Module(s) |
|---|---|
| Data structures, algorithms & OOP in AI workflows | Modules 2, 3 |
| Assess, test & improve AI-generated code | Module 7 (lesson 5), Module 9 |
| Build systems with AI components responsibly | Module 10 |
| ML literacy: data representation & model behavior | Modules 5, 7 |
| Professional Git & GitHub workflows | Module 9 (lesson 3) |
| RAG, agentic workflows, fine-tuning, guardrails | **Module 10** |

---

## Your Full Roadmap

```
Module 1  → Python Fundamentals (deepen the basics)
Module 2  → Data Structures & Algorithms
Module 3  → Object-Oriented Programming
Module 4  → Advanced Python
Module 5  → NumPy & Pandas  ← AI Core
Module 6  → Data Visualization
Module 7  → Machine Learning (scikit-learn)
Module 8  → Deep Learning & LLMs
Module 9  → Debugging, Testing & Git Workflow
Module 10 → RAG, Agentic AI & Guardrails  ← AI110 Core
Projects  → Mini-Projects + Capstone
```

---

## Progress Tracker

### Module 1 — Python Fundamentals
- [ ] Variables, Types & Type Casting
- [ ] Strings & String Methods
- [ ] Conditionals & Boolean Logic
- [ ] Loops (for, while, break, continue)
- [ ] Functions, *args, **kwargs, type hints
- [ ] Lists, Tuples, Sets, Dicts
- [ ] List / Dict / Set Comprehensions
- [ ] File I/O (text, JSON, CSV)
- [ ] Error Handling (try/except/raise, custom exceptions)
- [ ] **Exercise Set 1 — all tests pass**

### Module 2 — Data Structures & Algorithms
- [ ] Big O Notation
- [ ] Stacks & Queues
- [ ] Linked Lists
- [ ] Hash Maps (deep dive)
- [ ] Trees & Binary Search Trees
- [ ] Sorting Algorithms
- [ ] Binary Search
- [ ] Recursion & Memoization
- [ ] **Exercise Set 2 — all tests pass**

### Module 3 — Object-Oriented Programming
- [ ] Classes & Objects
- [ ] Inheritance & Polymorphism
- [ ] Magic/Dunder Methods
- [ ] Properties & Encapsulation
- [ ] Abstract Classes
- [ ] **Exercise Set 3 — all tests pass**

### Module 4 — Advanced Python
- [ ] Decorators & functools
- [ ] Generators & Iterators
- [ ] Context Managers
- [ ] Lambda, map, filter, zip
- [ ] Regular Expressions
- [ ] Virtual Environments & Modules
- [ ] **Exercise Set 4 — all tests pass**

### Module 5 — NumPy & Pandas (AI Core)
- [ ] NumPy arrays vs Python lists
- [ ] Array indexing, slicing, reshaping
- [ ] Vectorized operations & broadcasting
- [ ] Pandas DataFrames & Series
- [ ] Loading CSV / JSON data
- [ ] Data cleaning & missing values
- [ ] Filtering, grouping, aggregation
- [ ] Feature engineering
- [ ] **Exercise Set 5 — all tests pass**

### Module 6 — Data Visualization
- [ ] Matplotlib: line, bar, scatter, histogram
- [ ] Subplots & figure customization
- [ ] Seaborn statistical plots
- [ ] Confusion matrix visualization
- [ ] Training curve plots
- [ ] **Exercise Set 6 — all tests pass**

### Module 7 — Machine Learning (scikit-learn)
- [ ] The ML workflow (load → preprocess → split → train → evaluate)
- [ ] Train/test split & cross-validation
- [ ] Linear & Logistic Regression
- [ ] Decision Trees & Random Forests
- [ ] SVM & KNN
- [ ] Clustering (K-Means)
- [ ] Feature engineering & preprocessing
- [ ] Model evaluation: accuracy, F1, ROC-AUC
- [ ] Hyperparameter tuning (GridSearchCV)
- [ ] **Critically evaluating AI-generated ML code**
- [ ] **Exercise Set 7 — all tests pass**

### Module 8 — Deep Learning & LLMs
- [ ] Neural network fundamentals
- [ ] PyTorch tensors & autograd
- [ ] Building & training a neural net
- [ ] LLM API basics (Anthropic, OpenAI)
- [ ] Structured output from LLMs
- [ ] Prompt engineering techniques
- [ ] **Exercise Set 8 — all tests pass**

### Module 9 — Debugging, Testing & Git Workflow
- [ ] Reading tracebacks systematically
- [ ] Debugging strategies (print, pdb, breakpoint)
- [ ] Debugging AI-generated code
- [ ] Writing tests with pytest
- [ ] Parametrized tests & fixtures
- [ ] **Professional Git workflow**
- [ ] Commit message conventions
- [ ] Pull request workflow
- [ ] Code review skills
- [ ] **Exercise Set 9 — all tests pass**

### Module 10 — RAG, Agentic AI & Guardrails (AI110 Core)
- [ ] Embeddings & vector similarity
- [ ] Building a RAG system from scratch
- [ ] ChromaDB vector store
- [ ] Retrieval quality & chunking strategy
- [ ] Agentic loops & tool use
- [ ] Tool definitions & execution
- [ ] Real Anthropic tool use API
- [ ] Fine-tuning concepts & LoRA
- [ ] Input guardrails (injection detection)
- [ ] Output guardrails (sensitive data, format validation)
- [ ] Responsible AI checklist
- [ ] **Exercise Set 10 — all tests pass**

### Projects
- [ ] Mini-Project 1: Data Analyzer (Pandas + Visualization)
- [ ] Mini-Project 2: ML Classifier (scikit-learn, 3+ models)
- [ ] Mini-Project 3: RAG Chatbot (LLM + guardrails)
- [ ] **Capstone: End-to-End AI Application**

---

## Git Workflow — Every Session

```bash
# Start of session
git pull origin main

# After each exercise file
git add module-XX-*/exercises/exercises_XX.py
git commit -m "Module X: exercises complete"

# After each lesson
git commit -m "Module X: finished [topic] lesson"

# End of session
git push origin main
```

**Commit message format:**
```
feat(module-1): complete variables and strings lessons
fix(module-3): correct OOP exercise test for BankAccount
test(module-7): add edge case for empty dataset
```

---

## Quick Setup

```bash
# 1. Clone your repo
git clone https://github.com/YOUR_USERNAME/python-mastery-course.git
cd python-mastery-course

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r setup/requirements.txt

# 4. Set your API key (for Module 8+)
# Windows:
set ANTHROPIC_API_KEY=your-key-here
# Mac/Linux:
export ANTHROPIC_API_KEY=your-key-here
```

---

## Recommended Tools

| Tool | Purpose | Install |
|------|---------|---------|
| VS Code | Main editor | vscode.com |
| Jupyter Lab | Interactive AI/ML work | `pip install jupyterlab` |
| Git + GitHub | Progress tracking | git-scm.com |
| Python 3.11+ | Latest stable | python.org |

---

*Aligned with CodePath AI110 — built for your AI career.*
