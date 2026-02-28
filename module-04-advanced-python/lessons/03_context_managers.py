"""
LESSON 3: Context Managers (the 'with' statement)
===================================================
Context managers handle setup and teardown automatically.
You use them every time you open a file with 'with open(...)'.
"""

from contextlib import contextmanager
import time

# ══════════════════════════════════════════════════════
# WHY CONTEXT MANAGERS?
# ══════════════════════════════════════════════════════
# BAD — file might not get closed if an error occurs
f = open("test.txt", "w")
f.write("hello")
f.close()   # what if an exception happens before this?

# GOOD — file ALWAYS closes, even if exception occurs
with open("test.txt", "w") as f:
    f.write("hello")
# f is automatically closed here

import os; os.remove("test.txt")

# ══════════════════════════════════════════════════════
# BUILDING A CONTEXT MANAGER — class approach
# ══════════════════════════════════════════════════════
class Timer:
    """Measure execution time of a block of code."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self   # the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
print(f"Captured: {t.elapsed:.4f}s")

# ══════════════════════════════════════════════════════
# BUILDING A CONTEXT MANAGER — @contextmanager decorator
# ══════════════════════════════════════════════════════
# Everything before yield = __enter__
# Everything after yield = __exit__

@contextmanager
def timer(label=""):
    start = time.perf_counter()
    try:
        yield   # code in 'with' block runs here
    finally:    # always runs, even on exception
        elapsed = time.perf_counter() - start
        print(f"[{label}] {elapsed:.4f}s")

with timer("sum"):
    result = sum(range(500_000))

@contextmanager
def managed_file(path, mode="r"):
    """Open file, yield it, always close."""
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
        print(f"Closed {path}")

with managed_file("output.txt", "w") as f:
    f.write("Context managers are clean!\n")

with managed_file("output.txt") as f:
    print(f.read())

os.remove("output.txt")

# ══════════════════════════════════════════════════════
# AI/ML USE CASE: Model inference context
# ══════════════════════════════════════════════════════
@contextmanager
def inference_mode(model_name):
    """Simulate setting model to eval mode and back."""
    print(f"[{model_name}] Switching to eval mode")
    try:
        yield
    finally:
        print(f"[{model_name}] Switching back to train mode")

with inference_mode("ResNet-50"):
    print("  Making predictions...")
    # model.eval() would go here in real PyTorch

# ── Suppressing Exceptions ────────────────────────────
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")   # no error raised!
print("Continued after suppressed error")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use 'with' for anything that needs cleanup: files, connections, locks
# 2. __enter__ = setup, __exit__ = teardown (always runs)
# 3. @contextmanager is the easiest way to write a context manager
# 4. Everything before yield = setup; everything after yield = cleanup
# 5. In PyTorch: torch.no_grad() is a context manager!
print("\nDone! Move on to 04_functional_tools.py")
