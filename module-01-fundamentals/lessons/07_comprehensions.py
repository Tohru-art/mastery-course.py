"""
LESSON 7: List, Dict & Set Comprehensions
==========================================
Comprehensions are one of the most Pythonic features.
They replace verbose for-loops with clean one-liners.
You'll use these constantly in data processing.
"""

# ── 1. List Comprehension ─────────────────────────────────────────────────────
# Syntax: [expression for item in iterable]
# Syntax: [expression for item in iterable if condition]

# Old way (verbose):
squares_old = []
for n in range(10):
    squares_old.append(n ** 2)

# Pythonic way (comprehension):
squares = [n ** 2 for n in range(10)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a condition (filter):
even_squares = [n ** 2 for n in range(10) if n % 2 == 0]
print(even_squares)   # [0, 4, 16, 36, 64]

# Practical: process a list of strings
words = ["hello", "WORLD", "  python  ", "AI"]
cleaned = [word.strip().lower() for word in words]
print(cleaned)   # ['hello', 'world', 'python', 'ai']

# ── 2. Dict Comprehension ─────────────────────────────────────────────────────
# Syntax: {key_expr: value_expr for item in iterable}

models = ["ResNet", "BERT", "GPT-4", "Whisper"]
accuracies = [0.94, 0.91, 0.97, 0.95]

# Zip two lists into a dict
model_scores = {model: score for model, score in zip(models, accuracies)}
print(model_scores)

# Filter: only high-accuracy models
top_models = {k: v for k, v in model_scores.items() if v >= 0.94}
print(top_models)

# Transform: convert scores to percentages
pct_scores = {k: f"{v:.0%}" for k, v in model_scores.items()}
print(pct_scores)

# ── 3. Set Comprehension ──────────────────────────────────────────────────────
raw_data = ["Dog", "cat", "DOG", "Bird", "CAT"]
unique_animals = {word.lower() for word in raw_data}
print(unique_animals)   # {'dog', 'cat', 'bird'}

# ── 4. Conditional Expression (Ternary) in Comprehension ─────────────────────
# Syntax: [value_if_true if condition else value_if_false for item in iterable]
scores = [72, 88, 55, 91, 63, 95, 48]
grades = ["Pass" if s >= 65 else "Fail" for s in scores]
print(grades)   # ['Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Fail']

# ── 5. Nested Comprehensions ──────────────────────────────────────────────────
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a 2D grid
grid = [(r, c) for r in range(3) for c in range(3)]
print(grid)

# ── 6. Generator Expressions (Memory-Efficient) ───────────────────────────────
# Same syntax as list comprehension but with () instead of []
# Doesn't build the whole list in memory — processes one at a time
# Use when dealing with large datasets!

# This would load ALL 1 million items into memory:
# big_list = [i * 2 for i in range(1_000_000)]

# This uses barely any memory:
big_gen = (i * 2 for i in range(1_000_000))
print(sum(big_gen))  # sums all values without storing them

# ── 7. Practical: Data Preprocessing (AI use case) ────────────────────────────
# Imagine you have raw survey responses
raw_responses = [
    "  I love Python! ",
    "AI is AMAZING",
    "",
    "  machine learning rocks",
    "   ",
    "Deep learning is hard but worth it"
]

# Clean and filter in one line
valid_responses = [r.strip().lower() for r in raw_responses if r.strip()]
print(valid_responses)

# Count word lengths
word_lengths = {word: len(word) for word in ["neural", "network", "transformer", "attention"]}
print(word_lengths)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. [expr for item in iterable] → list comprehension
# 2. {k: v for ...} → dict comprehension
# 3. {expr for ...} → set comprehension
# 4. (expr for ...) → generator (memory efficient for large data)
# 5. Add if condition at the end to filter
# 6. Use ternary (x if cond else y) inside for transform-not-filter
print("\nDone! Move on to 08_file_io.py")
