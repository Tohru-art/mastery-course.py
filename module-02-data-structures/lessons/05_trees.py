"""
LESSON 5: Trees & Binary Search Trees
=======================================
Trees are everywhere: file systems, HTML/DOM, ML decision trees,
organization charts. Master trees and you can solve many hard problems.
"""

# ══════════════════════════════════════════════════════
# BINARY TREE NODE
# ══════════════════════════════════════════════════════
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# Build a tree:
#        10
#       /  \
#      5    15
#     / \     \
#    3   7    20

root = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15, None, TreeNode(20))
)

# ══════════════════════════════════════════════════════
# TREE TRAVERSALS
# ══════════════════════════════════════════════════════

def inorder(node):
    """Left → Root → Right. Gives SORTED order for BST."""
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def preorder(node):
    """Root → Left → Right. Used for copying/serializing trees."""
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def postorder(node):
    """Left → Right → Root. Used for deletion, calculating subtree values."""
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

print("Inorder:  ", inorder(root))    # [3, 5, 7, 10, 15, 20]
print("Preorder: ", preorder(root))   # [10, 5, 3, 7, 15, 20]
print("Postorder:", postorder(root))  # [3, 7, 5, 20, 15, 10]

# Level-order (BFS) — using a queue
from collections import deque

def level_order(root):
    """Return values level by level."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

print("Level order:", level_order(root))  # [[10], [5, 15], [3, 7, 20]]

# ══════════════════════════════════════════════════════
# COMMON TREE PROBLEMS
# ══════════════════════════════════════════════════════

def tree_height(node):
    """Height = longest path from root to leaf."""
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def tree_sum(node):
    if not node:
        return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print(f"\nHeight: {tree_height(root)}")   # 3
print(f"Sum: {tree_sum(root)}")           # 60
print(f"Nodes: {count_nodes(root)}")      # 6

# ══════════════════════════════════════════════════════
# BINARY SEARCH TREE (BST)
# ══════════════════════════════════════════════════════
# Property: left subtree < node < right subtree
# Search, insert, delete: O(log n) average, O(n) worst

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node   # val == node.val: duplicate, ignore

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def inorder(self):
        return inorder(self.root)

bst = BST()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

print("\nBST inorder (sorted):", bst.inorder())   # [1, 3, 4, 5, 6, 7, 8]
print("Search 4:", bst.search(4))                  # TreeNode(4)
print("Search 9:", bst.search(9))                  # None

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Inorder traversal of BST = sorted order
# 2. Most tree problems use recursion — trust the base case (if not node: ...)
# 3. BFS (level order) uses a queue; DFS (in/pre/postorder) uses recursion
# 4. BST: left < node < right → O(log n) search if balanced
print("\nDone! Move on to 06_sorting.py")
