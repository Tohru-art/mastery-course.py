"""
MODULE 9 EXERCISES — Debugging & Testing
==========================================
Run: python exercises/exercises_09.py
     pytest exercises/exercises_09.py -v
"""
import pytest


# ══════════════════════════════════════════════════════
# BUGGY FUNCTIONS — find and fix all bugs
# ══════════════════════════════════════════════════════

def find_duplicates(lst):
    """
    Return a list of items that appear more than once.
    BUG: it returns wrong results. Find and fix.
    """
    seen = []
    duplicates = []
    for item in lst:
        if item in seen:
            seen.append(item)  # BUG: should append to duplicates
        else:
            seen.append(item)
    return duplicates


def safe_get(dictionary, key, default=None):
    """
    Return value for key, or default if missing.
    BUG: raises an exception instead of returning default.
    """
    return dictionary[key]  # BUG: no error handling


def flatten_once(nested):
    """
    Flatten one level of nesting: [[1,2],[3,[4,5]]] → [1,2,3,[4,5]]
    BUG: fully flattens instead of just one level.
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            for sub in item:
                if isinstance(sub, list):
                    for x in sub:          # BUG: goes too deep
                        result.append(x)
                else:
                    result.append(sub)
        else:
            result.append(item)
    return result


# ══════════════════════════════════════════════════════
# PYTEST TESTS — you write these
# ══════════════════════════════════════════════════════

# Test find_duplicates (after fixing it)
def test_find_duplicates_basic():
    """[1,2,2,3,3,3] should return [2,3] (each duplicate once)"""
    result = find_duplicates([1, 2, 2, 3, 3, 3])
    assert sorted(result) == [2, 3]

def test_find_duplicates_no_duplicates():
    # YOUR CODE HERE
    pass

def test_find_duplicates_empty():
    # YOUR CODE HERE
    pass

def test_find_duplicates_all_same():
    # YOUR CODE HERE
    pass


# Test safe_get (after fixing it)
def test_safe_get_existing_key():
    assert safe_get({"a": 1}, "a") == 1

def test_safe_get_missing_key_returns_default():
    # YOUR CODE HERE
    pass

def test_safe_get_custom_default():
    # YOUR CODE HERE
    pass


# Test flatten_once (after fixing it)
def test_flatten_once_basic():
    assert flatten_once([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatten_once_does_not_deep_flatten():
    """[[1], [2, [3]]] should become [1, 2, [3]] — only one level"""
    result = flatten_once([[1], [2, [3]]])
    assert result == [1, 2, [3]]

def test_flatten_once_mixed():
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# CHALLENGE: Write tests for a mystery function
# ══════════════════════════════════════════════════════

def mystery_function(s: str) -> str:
    """
    Read this function carefully and figure out what it does.
    Then write at least 5 pytest tests that fully verify its behavior.
    """
    if not s:
        return ""
    words = s.split()
    result = []
    for word in words:
        if len(word) <= 3:
            result.append(word)
        else:
            result.append(word[0] + word[1:-1][::-1] + word[-1])
    return " ".join(result)

# Write your tests below:
def test_mystery_empty():
    assert mystery_function("") == ""

def test_mystery_short_word():
    # YOUR CODE HERE — words of 3 chars or less should be unchanged
    pass

def test_mystery_longer_word():
    # YOUR CODE HERE — figure out what happens to "hello"
    pass

def test_mystery_sentence():
    # YOUR CODE HERE
    pass

def test_mystery_all_short():
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# MANUAL TEST RUNNER (alternative to pytest)
# ══════════════════════════════════════════════════════
def run_tests():
    print("Run: pytest exercises/exercises_09.py -v")
    print("     for full test output with test names\n")

    print("Quick sanity checks:")
    # After fixing bugs:
    print("find_duplicates([1,2,2,3]):", find_duplicates([1,2,2,3]))
    print("safe_get({}, 'x', 0):", safe_get({}, 'x', 0))
    print("flatten_once([[1],[2,[3]]]):", flatten_once([[1],[2,[3]]]))

if __name__ == "__main__":
    run_tests()
