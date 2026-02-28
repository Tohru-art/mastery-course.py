"""
LESSON 8: Recursion
====================
A function that calls itself. Many elegant algorithms — tree traversal,
divide-and-conquer, backtracking — are naturally recursive.
"""

import sys
sys.setrecursionlimit(1000)  # Python's default, shown for awareness

# ── 1. The Structure of Recursion ─────────────────────────────────────────────
# Every recursive function needs:
#   1. BASE CASE  — when to stop
#   2. RECURSIVE CASE — call itself with a smaller input

def countdown(n):
    if n <= 0:           # base case
        print("Go!")
        return
    print(n)
    countdown(n - 1)     # recursive case — smaller input

countdown(5)

# ── 2. Factorial ──────────────────────────────────────────────────────────────
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)  # n! = n × (n-1)!

print(factorial(5))   # 120

# ── 3. Fibonacci (Naive — Exponential Time) ───────────────────────────────────
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# This is O(2^n) — very slow for large n!
print(fib_naive(10))  # 55

# ── 4. Fibonacci with Memoization ─────────────────────────────────────────────
# Cache results to avoid recomputing — turns O(2^n) into O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))  # fast!

# ── 5. Binary Search (Recursive) ──────────────────────────────────────────────
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1   # base case: not found
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # base case: found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7))   # 3 (index)

# ── 6. Flatten Nested List ────────────────────────────────────────────────────
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))  # recurse on nested lists
        else:
            result.append(item)
    return result

messy = [1, [2, 3], [4, [5, [6]]]]
print(flatten(messy))  # [1, 2, 3, 4, 5, 6]

# ── 7. Tree Traversal (Preview of Module 2 trees) ────────────────────────────
# Recursion is natural for trees

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_sum(node):
    """Sum all values in a binary tree"""
    if node is None:
        return 0   # base case: empty node
    return node.val + tree_sum(node.left) + tree_sum(node.right)

#       10
#      /  \
#     5    15
#    / \
#   3   7
tree = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15))

print(tree_sum(tree))  # 40

# ── 8. When to Use Recursion ──────────────────────────────────────────────────
"""
USE RECURSION when:
  - The problem naturally breaks into smaller sub-problems
  - Working with trees, graphs, nested structures
  - Divide and conquer algorithms (merge sort, quick sort)
  - Backtracking (maze solving, sudoku)

PREFER ITERATION when:
  - Simple loops are cleaner
  - Deep recursion (risk of stack overflow)
  - Performance is critical (function call overhead)

PYTHON TIP: Python has a recursion limit (~1000 calls deep).
For deep recursion, use iteration + a manual stack instead.
"""

# Iterative fibonacci (better for Python):
def fib_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(fib_iter(50))  # same result, no recursion limit risk

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Always have a base case — or you get infinite recursion
# 2. Use @lru_cache for memoization when same inputs repeat
# 3. Recursion is natural for trees, graphs, nested data
# 4. Python has a ~1000 call recursion limit — know when to use iteration
print("\nModule 2 lessons complete! Now do the exercises.")
