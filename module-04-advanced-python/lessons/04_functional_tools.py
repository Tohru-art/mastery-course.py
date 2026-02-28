"""
LESSON 4: Functional Tools — lambda, map, filter, zip, reduce
===============================================================
Python's functional tools let you write compact data transformations.
You'll see these constantly in data pipelines and ML code.
"""

from functools import reduce

# ══════════════════════════════════════════════════════
# LAMBDA — anonymous single-expression functions
# ══════════════════════════════════════════════════════
# Use for short, throwaway functions (especially as arguments)

double = lambda x: x * 2
add = lambda x, y: x + y

print(double(5))       # 10
print(add(3, 4))       # 7

# Best use: as key= argument
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=lambda w: len(w)))         # by length
print(sorted(words, key=lambda w: w[-1]))          # by last letter

models = [{"name": "A", "acc": 0.92}, {"name": "B", "acc": 0.88}]
best = max(models, key=lambda m: m["acc"])
print(f"Best model: {best['name']}")

# ══════════════════════════════════════════════════════
# map() — apply function to every element
# ══════════════════════════════════════════════════════
# map(function, iterable) → lazy iterator

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("\nmap squared:", squared)

# map with a real function
def normalize(x, total):
    return x / total

scores = [85, 92, 78, 95]
total = sum(scores)
normalized = list(map(lambda s: s/total, scores))
print("normalized:", [f"{n:.2f}" for n in normalized])

# map with multiple iterables (like zip)
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("map sums:", sums)

# NOTE: list comprehensions are usually more readable than map
# map version:  list(map(lambda x: x**2, numbers))
# comprehension: [x**2 for x in numbers]  ← prefer this

# ══════════════════════════════════════════════════════
# filter() — keep elements where function returns True
# ══════════════════════════════════════════════════════
data = [3, -1, 4, -1, 5, -9, 2, 6, -5]
positives = list(filter(lambda x: x > 0, data))
print("\nfilter positives:", positives)

# NOTE: list comprehensions with conditions are usually cleaner
# filter version:      list(filter(lambda x: x > 0, data))
# comprehension:       [x for x in data if x > 0]  ← prefer this

# ══════════════════════════════════════════════════════
# zip() — combine multiple iterables element-by-element
# ══════════════════════════════════════════════════════
names = ["Alice", "Bob", "Carol"]
scores = [92, 85, 78]
grades = ["A", "B", "C"]

# Combine into tuples
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score} ({grade})")

# Create dict from two lists
name_score = dict(zip(names, scores))
print("dict:", name_score)

# Unzip (transpose)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)   # * unpacks the list
print("unzipped:", nums, letters)

# zip stops at shortest iterable
print(list(zip([1,2,3,4], ["a","b"])))   # [(1,'a'), (2,'b')]

# zip_longest from itertools
from itertools import zip_longest
print(list(zip_longest([1,2,3,4], ["a","b"], fillvalue="?")))

# ══════════════════════════════════════════════════════
# reduce() — combine all elements into one value
# ══════════════════════════════════════════════════════
nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print("\nreduce product:", product)   # 120

# Often clearer with a loop or sum/max/min
print("sum:", sum(nums))   # prefer sum() over reduce

# reduce shines for custom accumulations
def deep_merge(d1, d2):
    return {**d1, **d2}

dicts = [{"a": 1}, {"b": 2}, {"c": 3}]
merged = reduce(deep_merge, dicts)
print("merged dicts:", merged)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. lambda: for short throwaway functions (especially key= args)
# 2. map/filter: functional alternatives to comprehensions — use comprehensions when clearer
# 3. zip(): essential for combining parallel lists, creating dicts
# 4. zip(*nested): transpose a 2D structure
# 5. reduce(): for custom accumulations — but sum/max/min are usually better
print("\nDone! Move on to 05_regex.py")
