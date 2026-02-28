"""
LESSON 1: Decorators
=====================
A decorator wraps a function to add behavior without modifying its source.
You'll see @staticmethod, @property, @lru_cache, and @app.route everywhere.
Learning to write your own decorators = next level Python.
"""

import time
import functools

# ── 1. What is a Decorator? ───────────────────────────────────────────────────
# A decorator is just a function that takes a function and returns a new function.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alex")
# Same as: say_hello = my_decorator(say_hello)

# ── 2. functools.wraps — Preserve Metadata ────────────────────────────────────
# Without @wraps, the wrapped function loses its name/docstring
def better_decorator(func):
    @functools.wraps(func)   # ALWAYS use this
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ── 3. Timing Decorator (Real Use Case) ──────────────────────────────────────
def timer(func):
    """Measure and print how long a function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)

# ── 4. Retry Decorator ────────────────────────────────────────────────────────
def retry(max_attempts=3, exceptions=(Exception,)):
    """Retry a function if it raises an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"  Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

import random
random.seed(42)

@retry(max_attempts=3)
def flaky_api_call():
    """Simulates an unreliable API call."""
    if random.random() < 0.6:
        raise ConnectionError("Network timeout")
    return "Success!"

try:
    result = flaky_api_call()
    print(result)
except ConnectionError:
    print("All retries failed")

# ── 5. Cache Decorator ────────────────────────────────────────────────────────
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n):
    """Cached fibonacci — result is stored for each unique input."""
    if n <= 1:
        return n
    return expensive_computation(n-1) + expensive_computation(n-2)

print(expensive_computation(40))  # fast on repeated calls

# ── 6. Validation Decorator ───────────────────────────────────────────────────
def validate_positive(func):
    """Ensure all numeric arguments are positive."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"All arguments must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def area(width, height):
    return width * height

print(area(5, 3))   # 15
try:
    area(-1, 3)
except ValueError as e:
    print(e)

# ── 7. Class Decorators — @property (you've seen this) ─────────────────────
class Circle:
    def __init__(self, radius):
        self._radius = radius  # _radius = "private" by convention

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.area)      # access like an attribute, not a method
c.radius = 10      # calls the setter
print(c.radius)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. A decorator wraps a function to add behavior before/after/around it
# 2. Always use @functools.wraps(func) inside your decorator
# 3. Common built-in decorators: @property, @staticmethod, @classmethod, @lru_cache
# 4. Decorators with arguments need an extra wrapper layer
print("\nDone! Move on to 02_generators.py")
