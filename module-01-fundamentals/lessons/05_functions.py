"""
LESSON 5: Functions & Scope
============================
Functions are how you organize code, avoid repetition, and build reusable tools.
In AI work you'll write functions constantly.
"""

# ── 1. Basic Function ─────────────────────────────────────────────────────────
def greet(name):
    return f"Hello, {name}!"

print(greet("Alex"))

# ── 2. Default Parameters ─────────────────────────────────────────────────────
def power(base, exponent=2):    # exponent defaults to 2
    return base ** exponent

print(power(3))       # 9  (uses default exponent=2)
print(power(3, 3))    # 27
print(power(2, 10))   # 1024

# ── 3. Keyword Arguments ──────────────────────────────────────────────────────
def describe_model(name, accuracy, parameters):
    print(f"Model: {name}")
    print(f"Accuracy: {accuracy:.1%}")
    print(f"Parameters: {parameters:,}")

# Call with keyword args — order doesn't matter
describe_model(accuracy=0.943, name="GPT-4", parameters=170_000_000_000)

# ── 4. *args — Variable Number of Arguments ──────────────────────────────────
def add(*numbers):
    return sum(numbers)

print(add(1, 2))          # 3
print(add(1, 2, 3, 4))    # 10
print(add(5, 10, 15, 20)) # 50

# ── 5. **kwargs — Variable Keyword Arguments ─────────────────────────────────
def print_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Alex", major="AI", year=2)

# ── 6. Return Multiple Values ─────────────────────────────────────────────────
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")

# ── 7. Scope — Local vs Global ────────────────────────────────────────────────
total = 100   # global variable

def add_to_total(amount):
    # total = total + amount  # ERROR! Can't modify global without 'global' keyword
    return total + amount     # reading is fine

print(add_to_total(50))  # 150

# Use global keyword (use sparingly — prefer returning values)
counter = 0
def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter: {counter}")  # 2

# ── 8. Docstrings — Document your functions ────────────────────────────────────
def calculate_accuracy(correct, total):
    """
    Calculate prediction accuracy.

    Args:
        correct (int): Number of correct predictions.
        total (int): Total number of predictions.

    Returns:
        float: Accuracy as a decimal between 0 and 1.

    Example:
        >>> calculate_accuracy(90, 100)
        0.9
    """
    if total == 0:
        return 0.0
    return correct / total

acc = calculate_accuracy(87, 100)
print(f"Accuracy: {acc:.1%}")
help(calculate_accuracy)  # prints the docstring

# ── 9. Type Hints (Modern Python) ─────────────────────────────────────────────
# These don't enforce types but make code more readable
def predict(text: str, threshold: float = 0.5) -> dict:
    """Returns a fake prediction result."""
    return {
        "label": "positive",
        "score": 0.87,
        "input": text
    }

result = predict("This movie was amazing!")
print(result)

# ── 10. Pure Functions (Best Practice) ───────────────────────────────────────
# A pure function: same inputs always return same output, no side effects
# This is important in ML — your preprocessing functions should be pure

def normalize(value: float, min_val: float, max_val: float) -> float:
    """Normalize a value to [0, 1] range."""
    return (value - min_val) / (max_val - min_val)

print(normalize(75, 0, 100))   # 0.75

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use default parameters for optional arguments
# 2. Use *args and **kwargs for flexible function signatures
# 3. Return multiple values as tuples — unpack on the other side
# 4. Write docstrings for every non-trivial function
# 5. Add type hints — they make code self-documenting
# 6. Aim for pure functions — easier to test and debug
print("\nDone! Move on to 06_collections.py")
