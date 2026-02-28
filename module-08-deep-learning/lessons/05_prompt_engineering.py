"""
LESSON 5: Prompt Engineering (Deep Dive)
==========================================
Prompt engineering = getting LLMs to do exactly what you want.
This is a required skill for every AI110 project.
"""

# ══════════════════════════════════════════════════════
# TECHNIQUE 1: ROLE PROMPTING
# ══════════════════════════════════════════════════════

role_prompt = """You are a senior Python engineer with 10 years of experience.
You write clean, efficient, well-documented code.
You always point out potential bugs and suggest best practices.
"""

# Without role:  "What's wrong with this code?"
# With role:     More expert-level, specific feedback

# ══════════════════════════════════════════════════════
# TECHNIQUE 2: CHAIN OF THOUGHT (CoT)
# ══════════════════════════════════════════════════════

cot_prompt = """Analyze this ML code for bugs. Think step by step:
1. First, check for data leakage
2. Then check for correct train/test split
3. Then verify the evaluation metric is appropriate
4. Finally, check for any other issues

Code:
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fit on ALL data
X_train, X_test = train_test_split(X_scaled, test_size=0.2)
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_train, y_train))  # train accuracy
```
"""

# CoT forces the model to reason before answering → more accurate

# ══════════════════════════════════════════════════════
# TECHNIQUE 3: FEW-SHOT EXAMPLES
# ══════════════════════════════════════════════════════

few_shot_prompt = """Classify the sentiment of Python-related tweets.
Labels: POSITIVE, NEGATIVE, NEUTRAL

Examples:
Tweet: "Just learned decorators in Python. Mind = blown!"
Label: POSITIVE

Tweet: "Why does Python's GIL make multithreading so painful?"
Label: NEGATIVE

Tweet: "Python 3.12 was released today."
Label: NEUTRAL

Now classify this tweet:
Tweet: "Finally got my NumPy broadcasting to work after 3 hours..."
Label:"""

# Few-shot examples dramatically improve accuracy on specific tasks

# ══════════════════════════════════════════════════════
# TECHNIQUE 4: STRUCTURED OUTPUT
# ══════════════════════════════════════════════════════

structured_prompt = """Review this Python function and return a JSON response.
Return ONLY valid JSON, no other text.

Schema:
{
  "has_bugs": boolean,
  "bugs": [{"line": int, "description": str, "fix": str}],
  "code_quality": "poor" | "fair" | "good" | "excellent",
  "suggestions": [str]
}

Code:
```python
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
```"""

# ══════════════════════════════════════════════════════
# TECHNIQUE 5: SELF-CONSISTENCY
# ══════════════════════════════════════════════════════

self_consistency_prompt = """Solve this data science problem.
Generate 3 different approaches and then recommend the best one.

Problem: I have a dataset with 10,000 rows and 50 features.
20% of values are missing. I need to prepare it for training a classifier.

Approach 1: ...
Approach 2: ...
Approach 3: ...
Recommendation: ...
"""

# ══════════════════════════════════════════════════════
# BUILDING A PROMPT TEMPLATE SYSTEM
# ══════════════════════════════════════════════════════

class PromptTemplate:
    """Reusable prompt templates with variable substitution."""

    CODE_REVIEW = """You are a senior engineer reviewing code.
Identify bugs, style issues, and improvements.
Be specific with line numbers.

Code to review:
```python
{code}
```

Focus on: {focus_areas}
Return feedback as a structured list."""

    DEBUG_HELP = """I'm getting this error in Python:
Error: {error_message}

In this code:
```python
{code}
```

Please:
1. Explain what caused the error
2. Show the fix
3. Explain how to prevent it in the future"""

    EXPLAIN_CONCEPT = """Explain {concept} to a CodePath AI110 student.
Assume they know Python basics but are new to {concept}.
Include:
- What it is (1-2 sentences)
- Why it matters for AI/ML
- A simple code example
- One common mistake to avoid"""

    @classmethod
    def format(cls, template_name: str, **kwargs) -> str:
        template = getattr(cls, template_name)
        return template.format(**kwargs)


# Usage examples
code_review_prompt = PromptTemplate.format(
    "CODE_REVIEW",
    code="""
def get_accuracy(preds, labels):
    correct = 0
    for p, l in zip(preds, labels):
        if p == l:
            correct += 1
    return correct / len(preds)
""",
    focus_areas="efficiency and edge cases"
)

debug_prompt = PromptTemplate.format(
    "DEBUG_HELP",
    error_message="AttributeError: 'NoneType' object has no attribute 'split'",
    code="result = get_user_input().split(',')"
)

explain_prompt = PromptTemplate.format(
    "EXPLAIN_CONCEPT",
    concept="attention mechanisms in transformers"
)

print("=== Code Review Prompt ===")
print(code_review_prompt)
print("\n=== Debug Prompt ===")
print(debug_prompt)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Role prompting: set expertise level and behavior
# 2. Chain of thought: force step-by-step reasoning
# 3. Few-shot examples: show the model what you want
# 4. Structured output: get JSON/specific format back
# 5. Self-consistency: ask for multiple approaches, pick best
# 6. Use templates: reuse good prompts, swap variables
print("\nModule 8 complete! Now do the exercises.")
