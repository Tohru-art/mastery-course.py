"""
LESSON 2: NumPy Advanced
=========================
Broadcasting, linear algebra, and the operations used daily in ML.
"""

import numpy as np

# ══════════════════════════════════════════════════════
# BROADCASTING
# ══════════════════════════════════════════════════════
"""
Broadcasting lets NumPy operate on arrays of DIFFERENT shapes
without copying data. This is a core concept in all of ML.

Rules:
1. Arrays with different ndim get 1s prepended to shape
2. Arrays with size 1 in a dimension are stretched to match
"""

# Scalar + array
a = np.array([1, 2, 3, 4])
print(a + 10)          # [11 12 13 14] — 10 is broadcast to every element

# Row vector + column vector → matrix
row = np.array([[1, 2, 3]])        # shape (1, 3)
col = np.array([[10], [20], [30]]) # shape (3, 1)
result = row + col
print("\nBroadcast row + col:\n", result)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# Normalize each row of a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
row_mins = matrix.min(axis=1, keepdims=True)   # shape (3,1)
row_maxs = matrix.max(axis=1, keepdims=True)   # shape (3,1)
normalized = (matrix - row_mins) / (row_maxs - row_mins)
print("\nRow-normalized:\n", normalized.round(2))

# ══════════════════════════════════════════════════════
# AXIS — understanding rows vs columns
# ══════════════════════════════════════════════════════
data = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\nSum all:", data.sum())           # 21
print("Sum cols (axis=0):", data.sum(axis=0))  # [5 7 9] — collapse rows
print("Sum rows (axis=1):", data.sum(axis=1))  # [6 15]  — collapse cols
print("Mean per column:", data.mean(axis=0))   # [2.5 3.5 4.5]

# ══════════════════════════════════════════════════════
# LINEAR ALGEBRA (used in ML math)
# ══════════════════════════════════════════════════════
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication — @ operator (Python 3.5+)
print("\nA @ B:\n", A @ B)
print("np.dot(A,B):\n", np.dot(A, B))   # same as @

# Element-wise vs matrix multiplication
print("A * B (element-wise):\n", A * B)

# Transpose
print("A.T:\n", A.T)

# Determinant and inverse
print("\ndet(A):", np.linalg.det(A))
print("inv(A):\n", np.linalg.inv(A).round(2))

# Eigenvalues (used in PCA)
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues:", eigvals)

# ══════════════════════════════════════════════════════
# STACKING & SPLITTING
# ══════════════════════════════════════════════════════
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nnp.stack:", np.stack([a, b]))           # shape (2,3) — new axis
print("np.vstack:", np.vstack([a, b]))           # shape (2,3) — vertical
print("np.hstack:", np.hstack([a, b]))           # shape (6,) — horizontal
print("np.concatenate:", np.concatenate([a, b])) # same as hstack for 1D

# Split
arr = np.arange(12).reshape(3, 4)
parts = np.split(arr, 3, axis=0)   # split into 3 along rows
print("\nSplit result:", [p.tolist() for p in parts])

# ══════════════════════════════════════════════════════
# PRACTICAL: Neural Network Forward Pass
# ══════════════════════════════════════════════════════
np.random.seed(42)

# Simulate a tiny neural network layer: output = relu(X @ W + b)
X = np.random.randn(5, 3)       # 5 samples, 3 features
W = np.random.randn(3, 4)       # 3 input features, 4 output neurons
b = np.zeros(4)                  # bias

# Forward pass
z = X @ W + b                   # (5,3) @ (3,4) + (4,) = (5,4)
output = np.maximum(0, z)       # ReLU activation

print("\nNeural net layer output shape:", output.shape)  # (5, 4)
print("Output:\n", output.round(3))

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Broadcasting: operations auto-expand arrays to compatible shapes
# 2. axis=0 collapses rows (operates down), axis=1 collapses columns
# 3. @ is matrix multiplication; * is element-wise
# 4. keepdims=True preserves dimensions after aggregation (needed for broadcasting)
print("\nDone! Move on to 03_pandas_basics.py")
