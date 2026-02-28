"""
LESSON 1: NumPy Basics
=======================
NumPy = Numerical Python. The backbone of all AI/ML computation.
PyTorch and TensorFlow tensors are built on NumPy concepts.

Install: pip install numpy
"""

import numpy as np

# ── 1. Why NumPy Instead of Lists? ───────────────────────────────────────────
# NumPy arrays are:
#   - Stored in contiguous memory (faster access)
#   - Operate on entire arrays at once (vectorized — no Python loops)
#   - 10-100x faster than Python lists for math

# Compare: multiply every element by 2
python_list = list(range(1_000_000))
numpy_array = np.arange(1_000_000)

import time
t0 = time.perf_counter()
result_list = [x * 2 for x in python_list]
t1 = time.perf_counter()
result_numpy = numpy_array * 2
t2 = time.perf_counter()

print(f"List: {t1-t0:.4f}s")
print(f"NumPy: {t2-t1:.6f}s")
print(f"NumPy is ~{(t1-t0)/(t2-t1):.0f}x faster")

# ── 2. Creating Arrays ────────────────────────────────────────────────────────
# From a list
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))          # <class 'numpy.ndarray'>
print(a.dtype)          # int64 (or int32 on Windows)

# Common creation functions
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones = np.ones((3, 3))           # 3x3 matrix of 1s
eye = np.eye(3)                  # 3x3 identity matrix
rng = np.arange(0, 10, 2)        # like range: [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced points: [0, 0.25, 0.5, 0.75, 1]

print("\nones:\n", ones)
print("linspace:", linspace)

# Random arrays (important for ML initialization!)
np.random.seed(42)                        # for reproducibility
rand_uniform = np.random.rand(3, 3)       # uniform [0, 1)
rand_normal = np.random.randn(3, 3)       # standard normal (mean=0, std=1)
rand_int = np.random.randint(0, 10, (3, 3))  # random ints

# ── 3. Array Properties ───────────────────────────────────────────────────────
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nMatrix:")
print(matrix)
print(f"Shape: {matrix.shape}")    # (3, 3) — rows, cols
print(f"Ndim: {matrix.ndim}")      # 2 — number of dimensions
print(f"Size: {matrix.size}")      # 9 — total elements
print(f"Dtype: {matrix.dtype}")    # int64

# ── 4. Indexing & Slicing ─────────────────────────────────────────────────────
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]
print(arr[::2])    # [10 30 50] (every other)

# 2D indexing
print(matrix[0])         # first row: [1 2 3]
print(matrix[0, 2])      # row 0, col 2: 3
print(matrix[:, 1])      # all rows, col 1: [2 5 8]
print(matrix[1:, :2])    # rows 1+, cols 0-1

# ── 5. Math Operations (Vectorized) ──────────────────────────────────────────
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)        # [11 22 33 44]
print(a * b)        # [10 40 90 160]
print(a ** 2)       # [1 4 9 16]
print(np.sqrt(a))   # [1. 1.41 1.73 2.]

# Math on every element
print(a * 5)        # [5 10 15 20]
print(a + 100)      # [101 102 103 104]

# Aggregate functions
data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"\nMean: {data.mean():.2f}")
print(f"Std: {data.std():.2f}")
print(f"Min: {data.min()}, Max: {data.max()}")
print(f"Sum: {data.sum()}")
print(f"Argmax: {data.argmax()}")  # index of max value

# ── 6. Boolean Indexing (Critical for data filtering) ────────────────────────
scores = np.array([72, 88, 55, 91, 63, 95, 48])

mask = scores >= 80
print("\nPassing scores mask:", mask)
print("Passing scores:", scores[mask])           # filter using mask
print("Count passing:", mask.sum())              # True counts as 1
print("Percentage passing:", mask.mean() * 100) # mean of bool = fraction

# ── 7. Reshape & Transpose ────────────────────────────────────────────────────
flat = np.arange(12)      # [0 1 2 ... 11]
matrix = flat.reshape(3, 4)  # 3 rows, 4 cols
print("\nReshaped:\n", matrix)
print("Transposed:\n", matrix.T)  # swap rows/cols

# -1 lets NumPy figure out the dimension automatically
reshaped = flat.reshape(4, -1)  # 4 rows, NumPy figures out 3 cols
print("Auto-reshape:\n", reshaped)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. NumPy arrays are faster than Python lists for math
# 2. Operations apply to the whole array — no loops needed
# 3. Boolean indexing is essential for filtering data
# 4. .shape, .dtype, .ndim tell you about your array
# 5. Always set np.random.seed() for reproducibility
print("\nDone! Move on to 02_numpy_advanced.py")
