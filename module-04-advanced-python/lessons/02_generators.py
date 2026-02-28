"""
LESSON 2: Generators & Iterators
==================================
Generators produce values one at a time — critical for large datasets.
Instead of loading 1 million rows into memory, stream them one by one.
This is how PyTorch DataLoaders work internally.
"""

import sys

# ── 1. The Problem with Lists ─────────────────────────────────────────────────
# Loading all data at once uses a LOT of memory

def all_squares_list(n):
    return [i**2 for i in range(n)]  # builds entire list in memory

def all_squares_gen(n):
    for i in range(n):
        yield i**2   # 'yield' makes this a generator

# Memory comparison
list_version = all_squares_list(1000)
gen_version = all_squares_gen(1000)

print(f"List memory: {sys.getsizeof(list_version):,} bytes")
print(f"Generator memory: {sys.getsizeof(gen_version)} bytes")  # tiny!

# Generators are lazy — they compute values only when asked
for square in gen_version:
    pass  # iterates through all without storing

# ── 2. yield keyword ─────────────────────────────────────────────────────────
def countdown(n):
    print("Starting countdown!")
    while n > 0:
        yield n   # pauses here, returns n, resumes on next()
        n -= 1
    print("Done!")

gen = countdown(3)
print(next(gen))  # "Starting countdown!" then 3
print(next(gen))  # 2
print(next(gen))  # 1
# next(gen) would raise StopIteration

# Simpler: just iterate
for num in countdown(5):
    print(num, end=" ")
print()

# ── 3. Generator Expressions ──────────────────────────────────────────────────
# Like list comprehensions but lazy
squares_gen = (x**2 for x in range(10))   # () not []
print(list(squares_gen))   # force evaluation

# Chain without loading everything
total = sum(x**2 for x in range(1_000_000))  # no list created!
print(f"Sum of squares: {total}")

# ── 4. yield from (Delegate to sub-generator) ────────────────────────────────
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # delegate recursively
        else:
            yield item

print(list(flatten([1, [2, [3, [4, 5]]]])))  # [1, 2, 3, 4, 5]

# ── 5. Practical: Data Batch Generator ────────────────────────────────────────
# This is how ML training batches work!

def batch_generator(data, batch_size):
    """Yield data in batches. Memory efficient."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

dataset = list(range(100))  # 100 samples
for batch in batch_generator(dataset, batch_size=10):
    # In real ML: you'd process each batch here
    pass  # process batch

print(f"Batches: {list(batch_generator(list(range(10)), 3))}")

# ── 6. Infinite Generator ────────────────────────────────────────────────────
def counter(start=0, step=1):
    """Infinite counter — generates values forever."""
    n = start
    while True:
        yield n
        n += step

# Take only the first 5 values
from itertools import islice
first_five = list(islice(counter(0, 2), 5))
print(first_five)   # [0, 2, 4, 6, 8]

# ── 7. Custom Iterator (Using __iter__ and __next__) ─────────────────────────
class FileLineIterator:
    """Iterate over lines of a file lazily."""
    def __init__(self, lines):
        self._lines = lines
        self._index = 0

    def __iter__(self):
        return self   # the iterator IS the iterable here

    def __next__(self):
        if self._index >= len(self._lines):
            raise StopIteration
        line = self._lines[self._index]
        self._index += 1
        return line.strip()


lines = ["  hello\n", "  world\n", "  python\n"]
for line in FileLineIterator(lines):
    print(line)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Generators use 'yield' instead of 'return'
# 2. They are lazy — values computed only when needed
# 3. Use for large datasets that don't fit in memory
# 4. Generator expressions: (expr for x in iterable) — lazy version of list comp
# 5. yield from delegates to another generator/iterable
print("\nDone! Move on to 03_context_managers.py")
