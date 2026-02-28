"""
LESSON 6: Sorting Algorithms
==============================
Understanding sorting teaches you divide-and-conquer thinking.
Python's built-in sort() is excellent — but you need to know WHY.
"""

import time

# ══════════════════════════════════════════════════════
# BUBBLE SORT — O(n²) — educational only
# ══════════════════════════════════════════════════════
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ══════════════════════════════════════════════════════
# MERGE SORT — O(n log n) — important to understand
# ══════════════════════════════════════════════════════
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ══════════════════════════════════════════════════════
# QUICK SORT — O(n log n) avg, O(n²) worst
# ══════════════════════════════════════════════════════
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ══════════════════════════════════════════════════════
# TEST AND COMPARE
# ══════════════════════════════════════════════════════
import random
random.seed(42)
data = random.sample(range(1000), 20)

print("Original:", data)
print("Bubble:  ", bubble_sort(data))
print("Merge:   ", merge_sort(data))
print("Quick:   ", quick_sort(data))
print("Built-in:", sorted(data))

# Speed comparison
big = random.sample(range(100_000), 10_000)

t0 = time.perf_counter()
merge_sort(big)
t1 = time.perf_counter()
sorted(big)
t2 = time.perf_counter()

print(f"\nMerge sort: {t1-t0:.4f}s")
print(f"Built-in:   {t2-t1:.6f}s  ← Python's sort (Timsort) is much faster")

# ══════════════════════════════════════════════════════
# PYTHON'S BUILT-IN SORT — Master These
# ══════════════════════════════════════════════════════
students = [
    {"name": "Alice", "gpa": 3.8, "age": 22},
    {"name": "Bob",   "gpa": 3.5, "age": 25},
    {"name": "Carol", "gpa": 3.9, "age": 21},
    {"name": "Dave",  "gpa": 3.5, "age": 23},
]

# Sort by single key
by_gpa = sorted(students, key=lambda s: s["gpa"], reverse=True)
print("\nBy GPA (desc):", [s["name"] for s in by_gpa])

# Sort by multiple keys: primary=gpa desc, secondary=age asc
from operator import itemgetter
by_gpa_age = sorted(students, key=lambda s: (-s["gpa"], s["age"]))
print("By GPA desc, Age asc:", [(s["name"], s["gpa"], s["age"]) for s in by_gpa_age])

# Sort strings case-insensitively
words = ["Banana", "apple", "Cherry", "date"]
print("Case-insensitive:", sorted(words, key=str.lower))

# Sort by length then alphabetically
print("By length:", sorted(words, key=lambda w: (len(w), w.lower())))

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use Python's sorted() / list.sort() — they're O(n log n) and highly optimized
# 2. Merge sort: understand the divide-and-conquer pattern
# 3. key= parameter is powerful — sort by any attribute
# 4. Use tuples as keys for multi-key sorting: key=lambda x: (x.primary, x.secondary)
# 5. Reverse with reverse=True or negate numeric keys: key=lambda x: -x.value
print("\nDone! Move on to 07_binary_search.py")
