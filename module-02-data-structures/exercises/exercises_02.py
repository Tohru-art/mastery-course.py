"""
MODULE 2 EXERCISES — Data Structures & Algorithms
===================================================
Complete all functions. Run with: python exercises/exercises_02.py
Commit when all tests pass.
"""

from collections import deque


# ══════════════════════════════════════════════════════
# STACKS & QUEUES
# ══════════════════════════════════════════════════════

def is_balanced(s):
    """
    Check if a string of brackets is balanced.
    Valid pairs: () [] {}
    Example:
      is_balanced("({[]})") → True
      is_balanced("([)]") → False
      is_balanced("{[}") → False
    Hint: Use a stack (list).
    """
    # YOUR CODE HERE
    pass


def reverse_string_with_stack(s):
    """
    Reverse a string using a stack (list).
    Don't use s[::-1] directly.
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# HASH MAPS
# ══════════════════════════════════════════════════════

def two_sum(nums, target):
    """
    Given a list of numbers and a target, return the indices of the two numbers
    that add up to target. Assume exactly one solution exists.
    Use a hash map for O(n) solution.
    Example: two_sum([2, 7, 11, 15], 9) → [0, 1]
    """
    # YOUR CODE HERE
    pass


def group_anagrams(words):
    """
    Group words that are anagrams of each other.
    Return a list of groups (each group is a list of words).
    Example: group_anagrams(["eat","tea","tan","ate","nat","bat"])
             → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    (order within groups or between groups doesn't matter)
    Hint: Sort each word's letters to use as a key.
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SORTING
# ══════════════════════════════════════════════════════

def merge_sort(arr):
    """
    Implement merge sort. Returns a new sorted list.
    Time: O(n log n). Don't use Python's built-in sort.
    """
    # YOUR CODE HERE
    pass


def sort_by_frequency(numbers):
    """
    Sort numbers by how frequently they appear (most frequent first).
    For ties, sort by value ascending.
    Example: sort_by_frequency([1,1,2,2,2,3]) → [2, 2, 2, 1, 1, 3]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# BINARY SEARCH
# ══════════════════════════════════════════════════════

def binary_search(arr, target):
    """
    Implement iterative binary search on a sorted list.
    Return the index of target, or -1 if not found.
    """
    # YOUR CODE HERE
    pass


def find_first_bad_version(n, is_bad):
    """
    Given n versions [1..n] and a function is_bad(version) that returns True
    if the version is bad, find the first bad version.
    All versions after the first bad one are also bad.
    Use binary search — O(log n).
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# RECURSION
# ══════════════════════════════════════════════════════

def power(base, exp):
    """
    Calculate base^exp recursively. exp is a non-negative integer.
    Bonus: can you do it in O(log n) using fast exponentiation?
    """
    # YOUR CODE HERE
    pass


def flatten_nested(nested):
    """
    Flatten a deeply nested list of any depth.
    Example: flatten_nested([1, [2, [3, [4]], 5]]) → [1, 2, 3, 4, 5]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# CHALLENGE: LRU Cache (HashMap + Doubly Linked List)
# ══════════════════════════════════════════════════════

class LRUCache:
    """
    Implement a Least Recently Used (LRU) cache.

    - get(key): Return value if key exists, else return -1. Mark as recently used.
    - put(key, value): Insert or update. If at capacity, evict the least recently used.

    Both operations must be O(1).

    Hint: Use a dict + collections.OrderedDict, or a dict + doubly linked list.
    """

    def __init__(self, capacity: int):
        # YOUR CODE HERE
        pass

    def get(self, key: int) -> int:
        # YOUR CODE HERE
        pass

    def put(self, key: int, value: int) -> None:
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

    print("\n=== MODULE 2 TESTS ===\n")

    check("is_balanced ({[]})", is_balanced("({[]})"), True)
    check("is_balanced ([)]", is_balanced("([)]"), False)
    check("is_balanced empty", is_balanced(""), True)

    check("reverse_string", reverse_string_with_stack("hello"), "olleh")

    check("two_sum", sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])
    check("two_sum 2", sorted(two_sum([3, 2, 4], 6)), [1, 2])

    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    if groups:
        groups_sorted = [sorted(g) for g in groups]
        check("group_anagrams count", len(groups), 3)
        check("group_anagrams eat/tea/ate", sorted(["eat","tea","ate"]) in groups_sorted, True)

    check("merge_sort", merge_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
    check("merge_sort already sorted", merge_sort([1, 2, 3]), [1, 2, 3])

    check("sort_by_frequency", sort_by_frequency([1,1,2,2,2,3]), [2,2,2,1,1,3])

    check("binary_search found", binary_search([1,3,5,7,9], 7), 3)
    check("binary_search not found", binary_search([1,3,5,7,9], 6), -1)

    versions = [False, False, True, True, True]
    is_bad = lambda v: versions[v - 1]
    check("first_bad_version", find_first_bad_version(5, is_bad), 3)

    check("power(2, 10)", power(2, 10), 1024)
    check("power(3, 0)", power(3, 0), 1)
    check("flatten_nested", flatten_nested([1, [2, [3, [4]], 5]]), [1, 2, 3, 4, 5])

    # LRU Cache
    cache = LRUCache(2)
    if cache:
        cache.put(1, 1)
        cache.put(2, 2)
        check("LRU get(1)", cache.get(1), 1)
        cache.put(3, 3)  # evicts key 2
        check("LRU get(2) after evict", cache.get(2), -1)
        check("LRU get(3)", cache.get(3), 3)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed! Commit your work.")


if __name__ == "__main__":
    run_tests()
