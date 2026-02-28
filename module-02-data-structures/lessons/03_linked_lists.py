"""
LESSON 3: Linked Lists
=======================
A linked list is a chain of nodes, each pointing to the next.
Unlike arrays, nodes aren't stored contiguously in memory.
Common in interviews — also teaches you pointer/reference thinking.
"""

# ══════════════════════════════════════════════════════
# NODE — the building block
# ══════════════════════════════════════════════════════
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None   # points to next node (or None if last)

    def __repr__(self):
        return f"Node({self.val})"


# ══════════════════════════════════════════════════════
# SINGLY LINKED LIST
# ══════════════════════════════════════════════════════
class LinkedList:
    def __init__(self):
        self.head = None   # points to first node
        self.size = 0

    def append(self, val):
        """Add to the end. O(n)"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, val):
        """Add to the front. O(1)"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, val):
        """Delete first occurrence of val. O(n)"""
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def to_list(self):
        """Convert to Python list for display."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        nodes = self.to_list()
        return " → ".join(str(n) for n in nodes) + " → None"


# Demo
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(ll)               # 0 → 1 → 2 → 3 → None
ll.delete(2)
print(ll)               # 0 → 1 → 3 → None
print(f"Size: {len(ll)}")

# ══════════════════════════════════════════════════════
# CLASSIC LINKED LIST PROBLEMS
# ══════════════════════════════════════════════════════

def reverse_linked_list(head):
    """Reverse a linked list in place. O(n) time, O(1) space."""
    prev = None
    current = head
    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse pointer
        prev = current             # move prev forward
        current = next_node        # move current forward
    return prev   # new head

def build_list(values):
    """Helper: build linked list from a Python list."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def to_python_list(head):
    """Helper: convert linked list to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test reverse
head = build_list([1, 2, 3, 4, 5])
print("\nOriginal:", to_python_list(head))
reversed_head = reverse_linked_list(head)
print("Reversed:", to_python_list(reversed_head))

def find_middle(head):
    """Find middle node using fast/slow pointer trick. O(n)."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next         # moves 1 step
        fast = fast.next.next   # moves 2 steps
    return slow   # when fast reaches end, slow is at middle

head = build_list([1, 2, 3, 4, 5])
middle = find_middle(head)
print(f"\nMiddle of [1,2,3,4,5]: {middle.val}")   # 3

head = build_list([1, 2, 3, 4])
middle = find_middle(head)
print(f"Middle of [1,2,3,4]: {middle.val}")       # 3 (second middle)

def has_cycle(head):
    """Detect cycle using Floyd's algorithm. O(n) time, O(1) space."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Create a cycle for testing
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.next = n2; n2.next = n3; n3.next = n4
print(f"\nNo cycle: {has_cycle(n1)}")   # False
n4.next = n2   # create cycle: 4 → 2
print(f"Has cycle: {has_cycle(n1)}")   # True

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Prepend is O(1), append is O(n) — use deque if you need both ends fast
# 2. Fast/slow pointer pattern solves many linked list problems
# 3. Always check for None before accessing .next
# 4. Draw it out! Linked list bugs are usually pointer reassignment errors
print("\nDone! Move on to 04_hash_maps.py")
