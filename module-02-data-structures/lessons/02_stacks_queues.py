"""
LESSON 2: Stacks & Queues
==========================
Two of the most fundamental data structures.
Stacks: LIFO (Last In, First Out) — like a stack of plates
Queues: FIFO (First In, First Out) — like a line at a store
"""

from collections import deque

# ══════════════════════════════════════════════════════
# STACK — Last In, First Out (LIFO)
# ══════════════════════════════════════════════════════
# Use cases: undo/redo, function call stack, bracket matching, DFS

# Python list works great as a stack
stack = []
stack.append(1)   # push
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Pop:", stack.pop())    # 3 — last in, first out
print("Pop:", stack.pop())    # 2
print("Peek:", stack[-1])     # 1 — look without removing

# ── Real Use Case: Balanced Brackets ──────────────────
def is_balanced(s):
    """Check if brackets are balanced using a stack."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("([)]"))     # False

# ── Real Use Case: Undo System ────────────────────────
class TextEditor:
    def __init__(self):
        self.text = ""
        self._history = []   # stack of previous states

    def type(self, chars):
        self._history.append(self.text)   # save state
        self.text += chars

    def undo(self):
        if self._history:
            self.text = self._history.pop()  # restore previous state

editor = TextEditor()
editor.type("Hello")
editor.type(" World")
print(editor.text)   # "Hello World"
editor.undo()
print(editor.text)   # "Hello"
editor.undo()
print(editor.text)   # ""

# ══════════════════════════════════════════════════════
# QUEUE — First In, First Out (FIFO)
# ══════════════════════════════════════════════════════
# Use cases: BFS, task queues, print spooler, request handling

# Use deque (double-ended queue) — O(1) on both ends
# list.pop(0) is O(n) — never use it as a queue!
queue = deque()
queue.append("task_1")    # enqueue
queue.append("task_2")
queue.append("task_3")
print("\nQueue:", queue)
print("Dequeue:", queue.popleft())   # "task_1" — first in, first out
print("Dequeue:", queue.popleft())   # "task_2"

# ── Real Use Case: Task Queue ─────────────────────────
class TaskQueue:
    """Simple task processor using a queue."""
    def __init__(self):
        self._queue = deque()

    def add_task(self, task):
        self._queue.append(task)
        print(f"  Added: {task}")

    def process_next(self):
        if self._queue:
            task = self._queue.popleft()
            print(f"  Processing: {task}")
            return task
        print("  No tasks in queue")
        return None

    @property
    def size(self):
        return len(self._queue)

print("\nTask Queue Demo:")
tq = TaskQueue()
tq.add_task("Train model")
tq.add_task("Evaluate model")
tq.add_task("Generate report")
tq.process_next()
tq.process_next()
print(f"  Remaining: {tq.size}")

# ══════════════════════════════════════════════════════
# DEQUE — Double-Ended Queue
# ══════════════════════════════════════════════════════
# Can append/pop from BOTH ends in O(1)
dq = deque([1, 2, 3])
dq.appendleft(0)    # add to front
dq.append(4)        # add to back
print("\nDeque:", dq)
print("Popleft:", dq.popleft())   # 0
print("Pop:", dq.pop())           # 4

# Sliding window max — deque keeps candidates in order
def sliding_window_max(nums, k):
    """Return max in each window of size k. O(n) using deque."""
    result = []
    dq = deque()   # stores indices, front = index of max
    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()   # remove out-of-window indices
        while dq and nums[dq[-1]] < num:
            dq.pop()       # remove smaller elements
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# STACK: list — use .append() and .pop()
# QUEUE: deque — use .append() and .popleft()
# NEVER use list.pop(0) for queues — it's O(n)!
print("\nDone! Move on to 03_linked_lists.py")
