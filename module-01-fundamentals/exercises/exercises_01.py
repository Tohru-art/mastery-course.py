"""
MODULE 1 EXERCISES — Python Fundamentals
==========================================
Complete every function. Do NOT look at answers until you've tried.
Run your solutions: python exercises/exercises_01.py

When you finish, commit:
  git add .
  git commit -m "Module 1: exercises complete"
"""

# ══════════════════════════════════════════════════════
# SECTION 1: Variables & Types
# ══════════════════════════════════════════════════════

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit. Formula: (C * 9/5) + 32"""
    # YOUR CODE HERE
    pass


def is_valid_age(value):
    """
    Return True if value is a valid age (int between 0 and 150).
    Return False otherwise.
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 2: Strings
# ══════════════════════════════════════════════════════

def clean_username(username):
    """
    Clean a username: strip whitespace, lowercase, replace spaces with underscores.
    Example: "  Alex Smith  " → "alex_smith"
    """
    # YOUR CODE HERE
    pass


def truncate(text, max_length, suffix="..."):
    """
    If text is longer than max_length, truncate it and add suffix.
    Example: truncate("Hello World", 7) → "Hello W..."
    If text is short enough, return it unchanged.
    """
    # YOUR CODE HERE
    pass


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the text (case-insensitive).
    Example: count_vowels("Hello World") → 3
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 3: Loops & Collections
# ══════════════════════════════════════════════════════

def find_max_without_builtin(numbers):
    """
    Find the maximum value in a list WITHOUT using max() or sort().
    Use a loop.
    """
    # YOUR CODE HERE
    pass


def flatten(nested_list):
    """
    Flatten a 2D list into a 1D list.
    Example: flatten([[1, 2], [3, 4], [5]]) → [1, 2, 3, 4, 5]
    """
    # YOUR CODE HERE
    pass


def word_frequency(text):
    """
    Count how many times each word appears in the text.
    Return a dict. Ignore case.
    Example: word_frequency("the cat sat on the mat")
             → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 4: Functions
# ══════════════════════════════════════════════════════

def calculator(a, b, operation="add"):
    """
    Perform a calculation on a and b.
    Supported operations: "add", "subtract", "multiply", "divide"
    For divide: if b is 0, return None.
    For unknown operation: raise ValueError with a clear message.
    """
    # YOUR CODE HERE
    pass


def running_average(numbers):
    """
    Return a list where each element is the average of all numbers up to that point.
    Example: running_average([2, 4, 6]) → [2.0, 3.0, 4.0]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 5: Comprehensions
# ══════════════════════════════════════════════════════

def get_even_squares(n):
    """
    Return a list of squares of even numbers from 0 to n (exclusive).
    Use a list comprehension.
    Example: get_even_squares(10) → [0, 4, 16, 36, 64]
    """
    # YOUR CODE HERE
    pass


def invert_dict(d):
    """
    Swap keys and values in a dictionary.
    Use a dict comprehension.
    Example: invert_dict({"a": 1, "b": 2}) → {1: "a", 2: "b"}
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 6: Error Handling
# ══════════════════════════════════════════════════════

def safe_divide(a, b):
    """
    Divide a by b. If b is 0, raise ValueError with message "Cannot divide by zero".
    If a or b are not numbers, raise TypeError with message "Both arguments must be numbers".
    """
    # YOUR CODE HERE
    pass


def parse_config(config_dict, key, default=None, expected_type=None):
    """
    Safely get a value from a config dict.
    - If key is missing, return default.
    - If expected_type is provided and the value is the wrong type, raise TypeError.

    Example:
        parse_config({"lr": 0.01}, "lr", expected_type=float) → 0.01
        parse_config({"lr": "fast"}, "lr", expected_type=float) → raises TypeError
        parse_config({}, "lr", default=0.001) → 0.001
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# CHALLENGE: AI-Themed Problem
# ══════════════════════════════════════════════════════

def analyze_predictions(predictions):
    """
    Given a list of dicts, each with keys "label" (str) and "confidence" (float),
    return a summary dict with:
      - "total": total number of predictions
      - "high_confidence": count of predictions with confidence >= 0.8
      - "label_counts": dict mapping each label to how many times it appeared
      - "average_confidence": mean confidence across all predictions
      - "most_common_label": the label that appeared most often

    Example input:
        [
            {"label": "cat", "confidence": 0.92},
            {"label": "dog", "confidence": 0.75},
            {"label": "cat", "confidence": 0.88},
        ]
    Example output:
        {
            "total": 3,
            "high_confidence": 2,
            "label_counts": {"cat": 2, "dog": 1},
            "average_confidence": 0.85,
            "most_common_label": "cat"
        }
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# TEST RUNNER — DO NOT MODIFY
# ══════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    def check(name, result, expected):
        nonlocal passed, failed
        if result == expected:
            print(f"  PASS  {name}")
            passed += 1
        else:
            print(f"  FAIL  {name}")
            print(f"         Expected: {expected}")
            print(f"         Got:      {result}")
            failed += 1

    print("\n=== MODULE 1 TESTS ===\n")

    # Variables & Types
    check("celsius_to_fahrenheit(0)", celsius_to_fahrenheit(0), 32.0)
    check("celsius_to_fahrenheit(100)", celsius_to_fahrenheit(100), 212.0)
    check("is_valid_age(25)", is_valid_age(25), True)
    check("is_valid_age(-1)", is_valid_age(-1), False)
    check("is_valid_age('old')", is_valid_age("old"), False)

    # Strings
    check("clean_username('  Alex Smith  ')", clean_username("  Alex Smith  "), "alex_smith")
    check("truncate long", truncate("Hello World", 7), "Hello W...")
    check("truncate short", truncate("Hi", 10), "Hi")
    check("count_vowels", count_vowels("Hello World"), 3)

    # Loops & Collections
    check("find_max_without_builtin", find_max_without_builtin([3, 1, 9, 2, 7]), 9)
    check("flatten", flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
    check("word_frequency", word_frequency("the cat sat on the mat"), {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1})

    # Functions
    check("calculator add", calculator(3, 4), 7)
    check("calculator subtract", calculator(10, 3, "subtract"), 7)
    check("calculator divide by zero", calculator(5, 0, "divide"), None)
    check("running_average", running_average([2, 4, 6]), [2.0, 3.0, 4.0])

    # Comprehensions
    check("get_even_squares", get_even_squares(10), [0, 4, 16, 36, 64])
    check("invert_dict", invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})

    # Error Handling
    try:
        safe_divide(10, 0)
        check("safe_divide raises ValueError", False, True)
    except ValueError:
        check("safe_divide raises ValueError", True, True)

    check("parse_config missing key", parse_config({}, "lr", default=0.001), 0.001)
    check("parse_config found key", parse_config({"lr": 0.01}, "lr"), 0.01)

    # Challenge
    preds = [
        {"label": "cat", "confidence": 0.92},
        {"label": "dog", "confidence": 0.75},
        {"label": "cat", "confidence": 0.88},
    ]
    result = analyze_predictions(preds)
    if result:
        check("analyze total", result.get("total"), 3)
        check("analyze high_confidence", result.get("high_confidence"), 2)
        check("analyze most_common", result.get("most_common_label"), "cat")
        check("analyze avg_conf", round(result.get("average_confidence", 0), 4), round((0.92 + 0.75 + 0.88) / 3, 4))

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed! Commit your work.")
    else:
        print(f"Fix the {failed} failing test(s) and re-run.")


if __name__ == "__main__":
    run_tests()
