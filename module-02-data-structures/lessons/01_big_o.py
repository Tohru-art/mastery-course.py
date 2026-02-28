"""
LESSON 1: Big O Notation
=========================
Big O describes how an algorithm's performance scales with input size.
It tells you: "If I double my data, how does my runtime change?"
This matters for AI when you're processing millions of data points.
"""

import time

# ── O(1) — Constant Time ──────────────────────────────────────────────────────
# No matter how big the input, it takes the same time.

def get_first(items):
    return items[0]   # always takes 1 step

def lookup_by_key(d, key):
    return d.get(key)  # dict lookup is O(1)

# ── O(n) — Linear Time ────────────────────────────────────────────────────────
# Time grows proportionally with input size.
# Double the input → double the time.

def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:    # touches every element once
        if num > max_val:
            max_val = num
    return max_val

def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# ── O(n²) — Quadratic Time ────────────────────────────────────────────────────
# A loop inside a loop. Slow for large inputs.
# Double the input → 4x the time.

def has_duplicates_slow(items):
    """O(n²) — check every pair"""
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicates_fast(items):
    """O(n) — use a set"""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

# ── O(log n) — Logarithmic Time ───────────────────────────────────────────────
# Input doubles → only 1 more step. Very fast.
# Classic example: binary search

def binary_search(sorted_list, target):
    """Requires a SORTED list. O(log n)"""
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ── O(n log n) — Linearithmic ─────────────────────────────────────────────────
# Common in efficient sorting algorithms (merge sort, timsort).
# Python's built-in sort() is O(n log n).

# ── Comparison Demo ───────────────────────────────────────────────────────────
def time_it(func, *args):
    start = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - start
    return result, elapsed

n = 10_000
test_list = list(range(n))

_, t_slow = time_it(has_duplicates_slow, test_list)
_, t_fast = time_it(has_duplicates_fast, test_list)
print(f"Duplicates check — Slow O(n²): {t_slow:.4f}s | Fast O(n): {t_fast:.6f}s")
print(f"Speedup: {t_slow/t_fast:.0f}x faster")

# ── Big O Cheat Sheet ─────────────────────────────────────────────────────────
"""
O(1)        Constant     — dict lookup, list index access
O(log n)    Logarithmic  — binary search
O(n)        Linear       — single loop, list search
O(n log n)  Linearithmic — merge sort, Python sort()
O(n²)       Quadratic    — nested loops
O(2ⁿ)       Exponential  — recursive fibonacci (bad)

Best to worst: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
"""

# ── Common Python Operation Complexities ─────────────────────────────────────
"""
LIST:
  list[i]          O(1)   — index access
  list.append()    O(1)   — add to end
  list.insert(0,x) O(n)   — insert at beginning (shifts all elements)
  x in list        O(n)   — linear search
  list.sort()      O(n log n)

DICT / SET:
  d[key]           O(1)   — lookup
  key in d         O(1)   — membership check
  d[key] = val     O(1)   — insert/update

→ For fast membership checks, use a SET or DICT, not a LIST
"""

# ── Practical: Don't Lookup in Lists ─────────────────────────────────────────
# BAD (O(n) per check):
valid_labels = ["cat", "dog", "bird", "fish"]  # list
def is_valid_list(label):
    return label in valid_labels  # O(n) every call!

# GOOD (O(1) per check):
valid_labels_set = {"cat", "dog", "bird", "fish"}  # set
def is_valid_set(label):
    return label in valid_labels_set  # O(1) every call!

print("\nDone! Move on to 02_stacks_queues.py")
