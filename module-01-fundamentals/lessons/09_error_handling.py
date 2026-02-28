"""
LESSON 9: Error Handling
=========================
Errors are inevitable. Writing code that handles errors gracefully is what
separates beginner code from production-ready code.
"""

# ── 1. Common Exceptions ──────────────────────────────────────────────────────
# Python has many built-in exception types:
# ValueError      — wrong type of value: int("abc")
# TypeError       — wrong type: "2" + 2
# KeyError        — dict key doesn't exist: d["missing"]
# IndexError      — list index out of range: [1,2][5]
# FileNotFoundError — file doesn't exist
# ZeroDivisionError — dividing by zero
# AttributeError  — object doesn't have that attribute
# ImportError     — can't import a module

# ── 2. try / except ───────────────────────────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ── 3. Catching Multiple Exceptions ──────────────────────────────────────────
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to int")
        return None
    except TypeError:
        print(f"Wrong type: {type(value)}")
        return None

print(safe_convert("42"))     # 42
print(safe_convert("hello"))  # None
print(safe_convert(None))     # None

# ── 4. else and finally ───────────────────────────────────────────────────────
# else  → runs ONLY if no exception was raised
# finally → runs ALWAYS (even if exception happened) — use for cleanup

def load_data(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    else:
        print("File loaded successfully!")
        return data
    finally:
        print("(load_data completed)")  # always runs

load_data("nonexistent.txt")

# ── 5. Catching Any Exception ─────────────────────────────────────────────────
# Use sparingly — catching all exceptions can hide bugs
try:
    x = int("bad")
except Exception as e:
    print(f"Error: {e}")          # shows the error message
    print(f"Type: {type(e).__name__}")  # shows the exception type

# ── 6. Raising Exceptions ─────────────────────────────────────────────────────
def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    if not 0 <= score <= 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    return score

try:
    validate_score(105)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    validate_score("ninety")
except TypeError as e:
    print(f"Type error: {e}")

# ── 7. Custom Exceptions ──────────────────────────────────────────────────────
# For larger projects, create custom exception classes
class ModelNotTrainedError(Exception):
    """Raised when trying to predict with an untrained model."""
    pass

class LowConfidenceError(Exception):
    """Raised when model confidence is too low to make a prediction."""
    def __init__(self, confidence, threshold):
        self.confidence = confidence
        self.threshold = threshold
        super().__init__(
            f"Confidence {confidence:.1%} is below threshold {threshold:.1%}"
        )

def predict(text, is_trained=False, confidence=0.4):
    if not is_trained:
        raise ModelNotTrainedError("Train the model before predicting!")
    if confidence < 0.7:
        raise LowConfidenceError(confidence, 0.7)
    return "positive"

try:
    predict("Hello", is_trained=True, confidence=0.4)
except LowConfidenceError as e:
    print(f"Low confidence: {e.confidence:.1%} (need {e.threshold:.1%})")

# ── 8. Best Practices ─────────────────────────────────────────────────────────
# GOOD: specific exceptions
try:
    value = int(input_str := "bad_value")
except ValueError:
    value = 0

# BAD: catching everything (hides bugs)
# try:
#     ...
# except:    # bare except — never do this
#     pass   # silently ignoring errors is dangerous

# GOOD: fail fast with clear messages
def get_api_key(config: dict, service: str) -> str:
    key = config.get(service)
    if key is None:
        raise KeyError(f"No API key found for service '{service}' in config")
    return key

try:
    config = {"openai": "sk-xxx123"}
    key = get_api_key(config, "anthropic")
except KeyError as e:
    print(f"Config error: {e}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use specific exception types (ValueError, TypeError) not bare except
# 2. Use 'finally' for cleanup (closing files, releasing resources)
# 3. Raise exceptions with clear messages to help debugging
# 4. Create custom exceptions for your application's domain errors
# 5. Never silently swallow exceptions with 'except: pass'
print("\nModule 1 Complete! Ready for exercises.")
