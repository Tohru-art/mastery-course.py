"""
LESSON 4: Hash Maps (Python Dicts — Deep Dive)
================================================
Python's dict IS a hash map. O(1) average for get, set, delete.
One of the most important data structures for writing fast code.
"""

# ══════════════════════════════════════════════════════
# HOW HASH MAPS WORK (concept)
# ══════════════════════════════════════════════════════
"""
A hash map stores key-value pairs using a hash function:
  1. hash(key) → an integer
  2. integer % table_size → a bucket index
  3. Store value in that bucket

This is why lookup is O(1) — you jump directly to the bucket.

Python's dict handles collisions automatically with open addressing.
"""

# ══════════════════════════════════════════════════════
# DICT OPERATIONS — REVIEW + DEEP DIVE
# ══════════════════════════════════════════════════════
from collections import defaultdict, Counter, OrderedDict

# All O(1): get, set, delete, membership check
d = {}
d["name"] = "Alice"        # set
print(d["name"])           # get — raises KeyError if missing
print(d.get("age", 0))     # safe get with default
print("name" in d)         # membership — O(1)!
del d["name"]              # delete

# dict.setdefault — set only if key doesn't exist
d.setdefault("score", 0)
d.setdefault("score", 100)  # won't overwrite
print(d["score"])           # 0

# ══════════════════════════════════════════════════════
# defaultdict — dict with automatic default values
# ══════════════════════════════════════════════════════
# Saves you from checking 'if key in dict' first

# Grouping items by category
words = ["apple", "ant", "bat", "bear", "cat", "crow", "ape"]
by_letter = defaultdict(list)   # default value is an empty list
for word in words:
    by_letter[word[0]].append(word)   # no KeyError!

print("\nGrouped by first letter:")
for letter, group in sorted(by_letter.items()):
    print(f"  {letter}: {group}")

# Counting without Counter
count = defaultdict(int)   # default value is 0
for word in words:
    count[word[0]] += 1    # no KeyError!
print("\nCounts:", dict(count))

# ══════════════════════════════════════════════════════
# Counter — count occurrences fast
# ══════════════════════════════════════════════════════
text = "the quick brown fox jumps over the lazy dog"
word_count = Counter(text.split())
print("\nMost common words:", word_count.most_common(3))
print("Count of 'the':", word_count["the"])
print("Count of 'xyz':", word_count["xyz"])  # 0, no KeyError

# Counter arithmetic
c1 = Counter("aabbc")
c2 = Counter("bccdd")
print("\nc1 + c2:", c1 + c2)
print("c1 - c2:", c1 - c2)
print("c1 & c2 (intersection):", c1 & c2)

# ══════════════════════════════════════════════════════
# PATTERNS: when to use a hash map
# ══════════════════════════════════════════════════════

# Pattern 1: Two Sum — find pair that adds to target
def two_sum(nums, target):
    """O(n) using hash map instead of O(n²) nested loops."""
    seen = {}   # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:   # O(1) lookup!
            return [seen[complement], i]
        seen[num] = i
    return []

print("\nTwo Sum:", two_sum([2, 7, 11, 15], 9))   # [0, 1]

# Pattern 2: Frequency map
def most_frequent(items):
    freq = Counter(items)
    return freq.most_common(1)[0][0]

print("Most frequent:", most_frequent([1, 2, 2, 3, 3, 3]))  # 3

# Pattern 3: Cache / Memoization
def fib_with_cache(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_with_cache(n-1, cache) + fib_with_cache(n-2, cache)
    return cache[n]

# Pattern 4: Grouping by property
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Carol", "grade": "A"},
    {"name": "Dave", "grade": "B"},
]
by_grade = defaultdict(list)
for s in students:
    by_grade[s["grade"]].append(s["name"])
print("\nBy grade:", dict(by_grade))

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. dict: O(1) get/set/delete/membership — use it to speed up algorithms
# 2. defaultdict: eliminates 'if key not in dict' boilerplate
# 3. Counter: frequency counting made easy
# 4. The "Two Sum" hash map pattern appears in many interview problems
# 5. NEVER iterate a list to check membership — use a set or dict
print("\nDone! Move on to 05_trees.py")
