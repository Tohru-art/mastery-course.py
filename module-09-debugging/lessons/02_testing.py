"""
LESSON 2: Writing Tests with pytest
=====================================
Tests prove your code works. They also prove when it breaks.
In AI110: "Assess, test, and improve AI-generated code using rigorous reasoning."

Install: pip install pytest
Run: pytest lessons/02_testing.py -v
"""

# ══════════════════════════════════════════════════════
# THE FUNCTIONS WE'RE TESTING
# ══════════════════════════════════════════════════════

def normalize(value, min_val, max_val):
    """Normalize value to [0, 1]. Raises ValueError if min==max."""
    if min_val == max_val:
        raise ValueError("min_val and max_val cannot be equal")
    return (value - min_val) / (max_val - min_val)


def classify_sentiment(score):
    """
    Classify a sentiment score into a label.
    score >= 0.6 → "positive"
    score <= 0.4 → "negative"
    else         → "neutral"
    """
    if not 0 <= score <= 1:
        raise ValueError(f"Score must be between 0 and 1, got {score}")
    if score >= 0.6:
        return "positive"
    elif score <= 0.4:
        return "negative"
    return "neutral"


def safe_average(numbers):
    """Return average, or None for empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# ══════════════════════════════════════════════════════
# PYTEST TESTS
# ══════════════════════════════════════════════════════
# pytest finds tests by looking for functions starting with 'test_'

# ── normalize() tests ─────────────────────────────────────────────────────────
def test_normalize_basic():
    assert normalize(5, 0, 10) == 0.5

def test_normalize_min():
    assert normalize(0, 0, 10) == 0.0

def test_normalize_max():
    assert normalize(10, 0, 10) == 1.0

def test_normalize_negative_range():
    result = normalize(-5, -10, 0)
    assert abs(result - 0.5) < 1e-9  # handle floating point

def test_normalize_raises_on_equal_min_max():
    import pytest
    with pytest.raises(ValueError, match="cannot be equal"):
        normalize(5, 3, 3)

# ── classify_sentiment() tests ────────────────────────────────────────────────
def test_sentiment_positive():
    assert classify_sentiment(0.9) == "positive"
    assert classify_sentiment(0.6) == "positive"

def test_sentiment_negative():
    assert classify_sentiment(0.1) == "negative"
    assert classify_sentiment(0.4) == "negative"

def test_sentiment_neutral():
    assert classify_sentiment(0.5) == "neutral"

def test_sentiment_boundaries():
    """Test exact boundary values."""
    assert classify_sentiment(0.6) == "positive"   # exact boundary
    assert classify_sentiment(0.4) == "negative"   # exact boundary

def test_sentiment_invalid_score():
    import pytest
    with pytest.raises(ValueError):
        classify_sentiment(1.5)
    with pytest.raises(ValueError):
        classify_sentiment(-0.1)

# ── safe_average() tests ──────────────────────────────────────────────────────
def test_average_basic():
    assert safe_average([1, 2, 3, 4, 5]) == 3.0

def test_average_single():
    assert safe_average([42]) == 42.0

def test_average_empty_returns_none():
    assert safe_average([]) is None

def test_average_negative_numbers():
    assert safe_average([-2, -4]) == -3.0

# ══════════════════════════════════════════════════════
# PARAMETRIZE — Test Multiple Inputs Cleanly
# ══════════════════════════════════════════════════════
import pytest

@pytest.mark.parametrize("score, expected", [
    (0.9, "positive"),
    (0.6, "positive"),
    (0.5, "neutral"),
    (0.41, "neutral"),
    (0.4, "negative"),
    (0.1, "negative"),
    (0.0, "negative"),
    (1.0, "positive"),
])
def test_sentiment_parametrized(score, expected):
    assert classify_sentiment(score) == expected


# ══════════════════════════════════════════════════════
# FIXTURES — Shared Setup
# ══════════════════════════════════════════════════════

@pytest.fixture
def sample_scores():
    """Reusable test data."""
    return [75, 82, 91, 68, 95, 88, 73]

def test_average_with_fixture(sample_scores):
    avg = safe_average(sample_scores)
    assert avg == pytest.approx(81.71, abs=0.01)


# ══════════════════════════════════════════════════════
# TESTING AI-GENERATED CODE (CodePath AI110)
# ══════════════════════════════════════════════════════
"""
When testing AI-generated code, always test:

1. HAPPY PATH — does it work with normal input?
2. EDGE CASES:
   - Empty input ([], "", None, 0)
   - Single element ([42])
   - All same values ([1, 1, 1])
   - Negative numbers
   - Very large/small numbers
3. ERROR CASES:
   - Invalid types (passing string where int expected)
   - Out-of-range values
   - Division by zero
4. BOUNDARY CONDITIONS:
   - Exact threshold values (score == 0.6, not 0.59 or 0.61)

Testing Template:
  def test_function_scenario():
      # Arrange — set up inputs
      input_data = [1, 2, 3]

      # Act — call the function
      result = my_function(input_data)

      # Assert — check the output
      assert result == expected_value
"""

if __name__ == "__main__":
    print("Run: pytest lessons/02_testing.py -v")
    print("  -v shows each test name")
    print("  --tb=short for shorter tracebacks")
