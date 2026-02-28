"""
LESSON 7: Binary Search
========================
Binary search is O(log n) — cuts the search space in half each step.
REQUIRES a sorted input. One of the most commonly tested algorithms.
"""

# ══════════════════════════════════════════════════════
# CLASSIC BINARY SEARCH
# ══════════════════════════════════════════════════════
def binary_search(arr, target):
    """Find target in sorted array. Returns index or -1."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2   # avoid overflow vs (left+right)/2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1    # target is in RIGHT half
        else:
            right = mid - 1   # target is in LEFT half
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 10))   # -1

# ══════════════════════════════════════════════════════
# FIND FIRST / LAST OCCURRENCE
# ══════════════════════════════════════════════════════
def find_first(arr, target):
    """Find leftmost index of target in sorted array."""
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid         # found, but keep searching LEFT
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_last(arr, target):
    """Find rightmost index of target in sorted array."""
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid         # found, but keep searching RIGHT
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

arr = [1, 2, 2, 2, 3, 4]
print(f"\nfind_first([1,2,2,2,3,4], 2): {find_first(arr, 2)}")  # 1
print(f"find_last([1,2,2,2,3,4], 2):  {find_last(arr, 2)}")    # 3

# ══════════════════════════════════════════════════════
# SEARCH ON ANSWER (Binary Search on a range)
# ══════════════════════════════════════════════════════
# When you can binary search on the ANSWER, not on an array

def can_fit(pages, students, max_pages):
    """Can we split 'pages' among 'students' with at most max_pages each?"""
    students_needed = 1
    current = 0
    for p in pages:
        if current + p > max_pages:
            students_needed += 1
            current = p
        else:
            current += p
    return students_needed <= students

def min_pages(pages, students):
    """
    Split books (pages list) among students so the max pages
    any student reads is minimized.
    """
    left = max(pages)          # minimum possible answer
    right = sum(pages)         # maximum possible answer
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_fit(pages, students, mid):
            result = mid       # feasible, try smaller
            right = mid - 1
        else:
            left = mid + 1     # not feasible, need more pages
    return result

print(f"\nMin pages (3 students): {min_pages([10, 20, 30, 40], 3)}")  # 60

# ══════════════════════════════════════════════════════
# Python's bisect module
# ══════════════════════════════════════════════════════
import bisect

sorted_list = [1, 3, 5, 7, 9]
# bisect_left: index where target would be inserted (left of duplicates)
print(f"\nbisect_left for 5: {bisect.bisect_left(sorted_list, 5)}")   # 2
print(f"bisect_right for 5: {bisect.bisect_right(sorted_list, 5)}")  # 3

# Insert while maintaining sorted order
bisect.insort(sorted_list, 4)
print(f"After insort(4): {sorted_list}")   # [1, 3, 4, 5, 7, 9]

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Binary search template: left=0, right=len-1, mid=(left+right)//2
# 2. When arr[mid] < target → search right (left = mid+1)
# 3. When arr[mid] > target → search left (right = mid-1)
# 4. Use bisect module for maintaining sorted lists
# 5. "Binary search on answer" pattern: binary search on a value range, not array
print("\nDone! Move on to 08_recursion.py")
