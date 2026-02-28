"""
MODULE 4 EXERCISES — Advanced Python
======================================
Run: python exercises/exercises_04.py
"""

import functools
import time


# ══════════════════════════════════════════════════════
# DECORATORS
# ══════════════════════════════════════════════════════

def log_calls(func):
    """
    Decorator that prints a log line each time the function is called.
    Format: "[LOG] function_name called with args=(1, 2) kwargs={'x': 3}"
    Return the original result unchanged.
    Use @functools.wraps.
    """
    # YOUR CODE HERE
    pass


def clamp(min_val, max_val):
    """
    Decorator factory. Clamps the return value of a function
    to be between min_val and max_val.

    Example:
        @clamp(0, 100)
        def score():
            return 150
        score()  → 100
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# GENERATORS
# ══════════════════════════════════════════════════════

def fibonacci_gen():
    """
    Infinite generator that yields Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8...
    """
    # YOUR CODE HERE
    pass


def sliding_window(data, window_size):
    """
    Generator that yields tuples of consecutive elements (a sliding window).
    Example: sliding_window([1,2,3,4,5], 3) → (1,2,3), (2,3,4), (3,4,5)
    """
    # YOUR CODE HERE
    pass


def data_pipeline(*transforms):
    """
    Returns a function that applies a sequence of transform functions.
    Each transform is a function that takes a list and returns a list.

    Example:
        normalize = lambda data: [x/max(data) for x in data]
        remove_neg = lambda data: [x for x in data if x >= 0]
        pipeline = data_pipeline(remove_neg, normalize)
        pipeline([-1, 2, 4, 8])  → [0.25, 0.5, 1.0]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# FUNCTIONAL TOOLS
# ══════════════════════════════════════════════════════

def compose(*functions):
    """
    Compose multiple functions right-to-left.
    compose(f, g, h)(x) == f(g(h(x)))

    Example:
        double = lambda x: x * 2
        add1 = lambda x: x + 1
        compose(double, add1)(5) → double(add1(5)) → double(6) → 12
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# CHALLENGE: Memoize Decorator
# ══════════════════════════════════════════════════════

def memoize(func):
    """
    Implement your own memoization decorator (like @lru_cache but manual).
    Cache results in a dict. Same inputs → return cached result.
    Add a .cache attribute to the returned wrapper that exposes the cache dict.

    Example:
        @memoize
        def fib(n):
            if n <= 1: return n
            return fib(n-1) + fib(n-2)
        fib(10)
        print(fib.cache)   # {0: 0, 1: 1, 2: 1, ...}
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# TEST RUNNER
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

    print("\n=== MODULE 4 TESTS ===\n")

    # log_calls
    if log_calls:
        @log_calls
        def add(a, b):
            return a + b
        check("log_calls returns correct value", add(3, 4), 7)
        check("log_calls preserves name", add.__name__, "add")

    # clamp
    if clamp:
        @clamp(0, 100)
        def over_score():
            return 150
        @clamp(0, 100)
        def under_score():
            return -5
        @clamp(0, 100)
        def ok_score():
            return 75
        check("clamp upper", over_score(), 100)
        check("clamp lower", under_score(), 0)
        check("clamp in range", ok_score(), 75)

    # fibonacci_gen
    if fibonacci_gen:
        from itertools import islice
        fibs = list(islice(fibonacci_gen(), 8))
        check("fibonacci_gen first 8", fibs, [0, 1, 1, 2, 3, 5, 8, 13])

    # sliding_window
    if sliding_window:
        windows = list(sliding_window([1, 2, 3, 4, 5], 3))
        check("sliding_window", windows, [(1,2,3), (2,3,4), (3,4,5)])
        check("sliding_window size 1", list(sliding_window([1,2,3], 1)), [(1,), (2,), (3,)])

    # data_pipeline
    if data_pipeline:
        remove_neg = lambda data: [x for x in data if x >= 0]
        normalize = lambda data: [x / max(data) if max(data) > 0 else 0 for x in data]
        pipeline = data_pipeline(remove_neg, normalize)
        result = pipeline([-1, 2, 4, 8])
        check("data_pipeline", result, [0.25, 0.5, 1.0])

    # compose
    if compose:
        double = lambda x: x * 2
        add1 = lambda x: x + 1
        check("compose", compose(double, add1)(5), 12)
        check("compose single", compose(double)(5), 10)

    # memoize
    if memoize:
        call_count = [0]
        @memoize
        def slow_fib(n):
            call_count[0] += 1
            if n <= 1:
                return n
            return slow_fib(n-1) + slow_fib(n-2)
        check("memoize result", slow_fib(10), 55)
        count_first = call_count[0]
        slow_fib(10)  # should use cache
        check("memoize caches", call_count[0], count_first)  # no new calls
        check("memoize has cache attr", hasattr(slow_fib, "cache"), True)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed! Commit your work.")


if __name__ == "__main__":
    run_tests()
