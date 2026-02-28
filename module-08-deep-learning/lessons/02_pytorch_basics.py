"""
LESSON 2: PyTorch Basics
=========================
PyTorch is the #1 deep learning framework for research and production.
Install: pip install torch

This lesson covers tensors — PyTorch's equivalent of NumPy arrays,
but they can run on GPU and support automatic differentiation.
"""

import torch
import numpy as np

print(f"PyTorch version: {torch.__version__}")
print(f"GPU available: {torch.cuda.is_available()}")

# ══════════════════════════════════════════════════════
# TENSORS — multi-dimensional arrays
# ══════════════════════════════════════════════════════

# Create tensors
t1 = torch.tensor([1.0, 2.0, 3.0])
t2 = torch.zeros(3, 4)
t3 = torch.ones(2, 3)
t4 = torch.rand(3, 3)        # uniform [0,1)
t5 = torch.randn(3, 3)       # standard normal
t6 = torch.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
t7 = torch.eye(4)            # identity matrix

print("\nRandom tensor:\n", t4)
print("Shape:", t4.shape)
print("Dtype:", t4.dtype)
print("Device:", t4.device)   # cpu or cuda:0

# From/to NumPy
np_array = np.array([1.0, 2.0, 3.0])
tensor_from_np = torch.from_numpy(np_array)
back_to_np = tensor_from_np.numpy()

# ══════════════════════════════════════════════════════
# TENSOR OPERATIONS
# ══════════════════════════════════════════════════════
a = torch.tensor([[1., 2.], [3., 4.]])
b = torch.tensor([[5., 6.], [7., 8.]])

print("\na + b:\n", a + b)
print("a * b (element-wise):\n", a * b)
print("a @ b (matrix mul):\n", a @ b)
print("a.T (transpose):\n", a.T)

# Math operations
print("mean:", a.mean())
print("sum:", a.sum())
print("sum per row:", a.sum(dim=1))     # dim=1 = across columns

# Reshape
flat = torch.arange(12.)
matrix = flat.reshape(3, 4)
print("\nReshaped:\n", matrix)
print("Unsqueeze:", flat.unsqueeze(0).shape)    # (1, 12) — add dim
print("Squeeze:", flat.unsqueeze(0).squeeze().shape)  # (12,) — remove dim

# ══════════════════════════════════════════════════════
# AUTOGRAD — automatic differentiation
# ══════════════════════════════════════════════════════
"""
This is what makes PyTorch special.
When requires_grad=True, PyTorch tracks all operations
and can compute gradients automatically via .backward().
"""

x = torch.tensor(3.0, requires_grad=True)
y = x ** 2 + 2 * x + 1   # y = x² + 2x + 1

y.backward()   # compute dy/dx
print(f"\ny = x² + 2x + 1 at x=3: y={y.item():.1f}")
print(f"dy/dx = 2x + 2 at x=3: {x.grad.item():.1f}")  # should be 8

# Matrix gradients
W = torch.randn(3, 2, requires_grad=True)
x = torch.randn(2, 1)
out = (W @ x).sum()
out.backward()
print("\nGradient w.r.t. W:", W.grad.shape)  # same shape as W

# torch.no_grad() — disable gradient tracking for inference
with torch.no_grad():
    y_inference = W @ x   # no gradients tracked — faster!
print("Inference (no grad):", y_inference.shape)

# ══════════════════════════════════════════════════════
# DEVICE MANAGEMENT — CPU vs GPU
# ══════════════════════════════════════════════════════
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\nUsing device: {device}")

# Move tensors to device
t = torch.randn(3, 3).to(device)
# For real GPU training, all tensors AND model must be on same device

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Tensors are like NumPy arrays but support GPU and autograd
# 2. requires_grad=True enables automatic differentiation
# 3. .backward() computes gradients; .grad holds the gradient
# 4. torch.no_grad(): use during inference to skip gradient computation
# 5. .to(device) moves tensor to CPU or GPU
print("\nDone! Move on to 03_training.py")
