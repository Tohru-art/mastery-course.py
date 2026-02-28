"""
LESSON 4: Code Quality & PEP 8
================================
Readable code is professional code.
Tools: black (auto-formatter), pylint (linter), mypy (type checker)

Install: pip install black pylint mypy
"""

# ══════════════════════════════════════════════════════
# PEP 8 — Python's Style Guide
# ══════════════════════════════════════════════════════
"""
PEP 8 = the official Python style guide. Key rules:

NAMING:
  snake_case        → functions, variables, modules
  CamelCase         → classes
  UPPER_SNAKE_CASE  → constants
  _single_leading   → "private" convention
  __double_leading  → name mangling (rare)

SPACING:
  4 spaces per indent (never tabs)
  2 blank lines between top-level functions/classes
  1 blank line between methods in a class
  Spaces around operators: x = 1 + 2 (not x=1+2)
  No space before colon: d[key] (not d [key])

LINES:
  Max 88 characters per line (Black's default, stricter than PEP8's 79)
  Break long lines with backslash or parentheses

IMPORTS:
  Standard library first, then third-party, then local
  Alphabetical within each group
  One import per line
"""

# ── BAD CODE ──────────────────────────────────────────
# (don't write like this)
def calculateAccuracy(Predictions,GroundTruth):
    c=0
    for i in range(len(Predictions)):
        if Predictions[i]==GroundTruth[i]:c+=1
    return c/len(Predictions)

# ── GOOD CODE ─────────────────────────────────────────
def calculate_accuracy(predictions: list, ground_truth: list) -> float:
    """
    Calculate prediction accuracy.

    Args:
        predictions: Model output labels.
        ground_truth: True labels.

    Returns:
        Accuracy as a float in [0, 1].

    Raises:
        ValueError: If lists have different lengths or are empty.
    """
    if len(predictions) != len(ground_truth):
        raise ValueError("predictions and ground_truth must have equal length")
    if not predictions:
        raise ValueError("Cannot compute accuracy of empty lists")

    correct = sum(p == t for p, t in zip(predictions, ground_truth))
    return correct / len(predictions)


# ══════════════════════════════════════════════════════
# AUTO-FORMATTING WITH BLACK
# ══════════════════════════════════════════════════════
"""
Black reformats your code automatically.
It's opinionated — no configuration needed.

Run on a file:
  black module-01-fundamentals/lessons/01_variables_types.py

Run on entire project:
  black .

Check without modifying:
  black --check .

In VS Code: install "Black Formatter" extension
  → set "Format on Save" to True
  → your code auto-formats every time you save
"""

# ══════════════════════════════════════════════════════
# LINTING WITH PYLINT
# ══════════════════════════════════════════════════════
"""
Pylint analyzes your code for errors and style issues.
It gives a score out of 10.

Run:
  pylint module-01-fundamentals/lessons/

Common warnings:
  C0103: Variable name 'x' doesn't conform to naming convention
  W0611: Unused import
  R0914: Too many local variables
  C0301: Line too long
"""

# ══════════════════════════════════════════════════════
# TYPE CHECKING WITH MYPY
# ══════════════════════════════════════════════════════
"""
Mypy checks your type hints are consistent.

Run:
  mypy module-01-fundamentals/lessons/05_functions.py

Example errors it catches:
  def add(x: int, y: int) -> int:
      return x + y

  result = add("hello", "world")  ← mypy error: str passed where int expected
"""

from typing import List, Dict, Optional, Tuple, Union

# Good type annotations
def process_predictions(
    predictions: List[float],
    labels: List[int],
    threshold: float = 0.5
) -> Tuple[List[int], float]:
    """Convert probabilities to labels and compute accuracy."""
    binary_preds = [1 if p >= threshold else 0 for p in predictions]
    accuracy = calculate_accuracy(binary_preds, labels)
    return binary_preds, accuracy


def load_config(path: str) -> Optional[Dict[str, Union[str, int, float]]]:
    """Load config file. Returns None if file not found."""
    import json, os
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


# ══════════════════════════════════════════════════════
# MEANINGFUL NAMES — the most important quality rule
# ══════════════════════════════════════════════════════
# BAD names:
def fn(d, t):
    r = []
    for i in d:
        if i > t:
            r.append(i)
    return r

# GOOD names:
def filter_above_threshold(data: list, threshold: float) -> list:
    return [value for value in data if value > threshold]

# Variables:
# BAD:  x, tmp, lst, d, arr, n, val
# GOOD: user_scores, training_data, model_config, accuracy_threshold

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use black for auto-formatting — no debates about style
# 2. Use pylint to catch errors and bad practices
# 3. Add type hints — they document your code and catch bugs
# 4. Names should explain WHAT something is, not HOW it's stored
# 5. Clean code is a professional requirement, not a nicety
print("\nModule 9 complete! Now do the exercises.")
