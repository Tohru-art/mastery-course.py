"""
LESSON 4: Properties & Encapsulation
=======================================
Encapsulation means hiding internal details and controlling access.
@property lets you protect data while keeping a clean interface.
"""

# ══════════════════════════════════════════════════════
# THE PROBLEM WITHOUT PROPERTIES
# ══════════════════════════════════════════════════════
class BadCircle:
    def __init__(self, radius):
        self.radius = radius   # Anyone can set radius = -5 — bad!

c = BadCircle(5)
c.radius = -10   # no protection!
print(c.radius)  # -10 — invalid state!

# ══════════════════════════════════════════════════════
# @property — controlled access
# ══════════════════════════════════════════════════════
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius   # _ means "private by convention"

    @property
    def radius(self):
        """Getter — called when you read circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — called when you write circle.radius = x"""
        if value <= 0:
            raise ValueError(f"Radius must be positive, got {value}")
        self._radius = value

    @radius.deleter
    def radius(self):
        raise AttributeError("Cannot delete radius")

    @property
    def area(self):
        """Computed property — no setter needed (read-only)"""
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2   # goes through the radius setter!


c = Circle(5)
print(c.radius)       # 5  (calls getter)
print(c.area)         # 78.54... (computed)
print(c.diameter)     # 10

c.radius = 10         # calls setter
print(c.area)         # 314.16...

c.diameter = 6        # sets diameter → calls diameter setter → calls radius setter
print(c.radius)       # 3.0

try:
    c.radius = -1     # raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# ══════════════════════════════════════════════════════
# AI/ML USE CASE: Model with validated hyperparameters
# ══════════════════════════════════════════════════════
class NeuralNetConfig:
    def __init__(self, learning_rate=0.001, epochs=50, batch_size=32):
        self.learning_rate = learning_rate   # goes through setter
        self.epochs = epochs
        self.batch_size = batch_size

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if not 0 < value < 1:
            raise ValueError(f"Learning rate must be between 0 and 1, got {value}")
        self._learning_rate = value

    @property
    def epochs(self):
        return self._epochs

    @epochs.setter
    def epochs(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Epochs must be a positive integer, got {value}")
        self._epochs = value

    @property
    def batch_size(self):
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value):
        valid = [16, 32, 64, 128, 256]
        if value not in valid:
            raise ValueError(f"Batch size must be one of {valid}, got {value}")
        self._batch_size = value

    def __repr__(self):
        return (f"NeuralNetConfig(lr={self._learning_rate}, "
                f"epochs={self._epochs}, batch={self._batch_size})")


config = NeuralNetConfig(learning_rate=0.001, epochs=100, batch_size=32)
print("\n", config)

config.learning_rate = 0.0001   # fine
try:
    config.learning_rate = 5.0  # too big
except ValueError as e:
    print(f"Error: {e}")

try:
    config.batch_size = 100     # not a valid batch size
except ValueError as e:
    print(f"Error: {e}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. _ prefix = "private" by convention (not enforced)
# 2. @property turns a method into an attribute — clean interface
# 3. @x.setter validates before setting — prevents invalid state
# 4. Read-only properties: define @property but no @x.setter
# 5. Use properties for: validation, computed values, lazy loading
print("\nDone! Move on to 05_abstract_classes.py")
