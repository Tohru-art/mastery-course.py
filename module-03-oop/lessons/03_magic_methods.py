"""
LESSON 3: Magic / Dunder Methods
==================================
Double underscore methods (__init__, __str__, etc.) let your classes
behave like built-in Python types. These make your code feel natural.
"""

# ══════════════════════════════════════════════════════
# THE MOST IMPORTANT DUNDERS
# ══════════════════════════════════════════════════════
class Vector:
    """2D vector that behaves like a built-in type."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Official string — shown in REPL, used for debugging."""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """Human-friendly string — used by print()."""
        return f"({self.x}, {self.y})"

    def __len__(self):
        """len(v) — makes your object work with len()."""
        return 2

    def __add__(self, other):
        """v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """scalar * v (reversed operand)"""
        return self.__mul__(scalar)

    def __eq__(self, other):
        """v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        """abs(v) — magnitude"""
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):
        """bool(v) — False if zero vector"""
        return self.x != 0 or self.y != 0

    def __iter__(self):
        """for val in v — makes it iterable"""
        yield self.x
        yield self.y

    def __getitem__(self, index):
        """v[0], v[1] — makes it subscriptable"""
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError("Vector index out of range")


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(repr(v1))       # Vector(3, 4)
print(str(v1))        # (3, 4)
print(v1 + v2)        # (4, 6)
print(v1 - v2)        # (2, 2)
print(v1 * 3)         # (9, 12)
print(2 * v1)         # (6, 8)
print(abs(v1))        # 5.0 (Pythagorean theorem)
print(v1 == v2)       # False
print(list(v1))       # [3, 4]
print(v1[0], v1[1])   # 3 4

# ══════════════════════════════════════════════════════
# CONTAINER METHODS
# ══════════════════════════════════════════════════════
class NumberSet:
    """Custom container that mimics a set."""

    def __init__(self, *values):
        self._data = set(values)

    def __contains__(self, item):
        """item in s"""
        return item in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"NumberSet({sorted(self._data)})"


ns = NumberSet(1, 2, 3, 4, 5)
print("\n3 in ns:", 3 in ns)       # True
print("9 in ns:", 9 in ns)        # False
print("len:", len(ns))             # 5
print("iter:", sorted(ns))        # [1, 2, 3, 4, 5]

# ══════════════════════════════════════════════════════
# COMPARISON METHODS
# ══════════════════════════════════════════════════════
from functools import total_ordering

@total_ordering   # only need __eq__ and one comparison → gets the rest free
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __repr__(self):
        return f"Student({self.name!r}, {self.gpa})"

students = [Student("Bob", 3.5), Student("Alice", 3.8), Student("Carol", 3.2)]
print("\nSorted:", sorted(students))  # sorted by gpa
print("Max:", max(students))

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# __repr__: for debugging (shown in REPL)
# __str__: for display (shown by print)
# __add__/__sub__/__mul__: arithmetic operators
# __eq__/__lt__: comparison (use @total_ordering to get all comparisons)
# __len__/__contains__/__iter__: make your object a container
print("\nDone! Move on to 04_properties.py")
