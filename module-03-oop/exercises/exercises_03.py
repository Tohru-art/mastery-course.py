"""
MODULE 3 EXERCISES — OOP
=========================
Complete all classes. Run: python exercises/exercises_03.py
"""


# ══════════════════════════════════════════════════════
# EXERCISE 1: Bank Account
# ══════════════════════════════════════════════════════

class BankAccount:
    """
    Model a bank account with:
    - owner (str)
    - balance (float, starts at 0)
    - transaction_history (list of dicts)

    Methods:
    - deposit(amount): Add amount. Raise ValueError if amount <= 0.
    - withdraw(amount): Subtract amount. Raise ValueError if amount <= 0.
                        Raise ValueError if insufficient funds.
    - get_balance(): Return current balance.
    - get_history(): Return list of all transactions.

    Each transaction should be logged as:
      {"type": "deposit"/"withdrawal", "amount": ..., "balance_after": ...}

    Also implement __str__ to return: "BankAccount(owner='Alice', balance=$100.00)"
    """

    def __init__(self, owner):
        # YOUR CODE HERE
        pass

    def deposit(self, amount):
        # YOUR CODE HERE
        pass

    def withdraw(self, amount):
        # YOUR CODE HERE
        pass

    def get_balance(self):
        # YOUR CODE HERE
        pass

    def get_history(self):
        # YOUR CODE HERE
        pass

    def __str__(self):
        # YOUR CODE HERE
        pass


# ══════════════════════════════════════════════════════
# EXERCISE 2: Shape Hierarchy
# ══════════════════════════════════════════════════════

import math

class Shape:
    """
    Base class for shapes.
    Has abstract methods: area() and perimeter()
    Has concrete method: describe() → "Circle with area 78.54"
    Also implement __gt__ to compare shapes by area.
    """

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.__class__.__name__} with area {self.area():.2f}"

    def __gt__(self, other):
        # YOUR CODE HERE (compare by area)
        pass


class Circle(Shape):
    """Circle with a given radius."""
    def __init__(self, radius):
        # YOUR CODE HERE
        pass

    def area(self):
        # YOUR CODE HERE
        pass

    def perimeter(self):
        # YOUR CODE HERE
        pass


class Rectangle(Shape):
    """Rectangle with width and height."""
    def __init__(self, width, height):
        # YOUR CODE HERE
        pass

    def area(self):
        # YOUR CODE HERE
        pass

    def perimeter(self):
        # YOUR CODE HERE
        pass


class Square(Rectangle):
    """Square is a Rectangle where width == height. Only takes side."""
    def __init__(self, side):
        # YOUR CODE HERE (call Rectangle's __init__)
        pass


# ══════════════════════════════════════════════════════
# EXERCISE 3: Dataset Class (AI-themed)
# ══════════════════════════════════════════════════════

class Dataset:
    """
    A simple ML dataset container.

    Attributes:
    - name (str)
    - samples (list of dicts, each has "features" and "label")

    Methods:
    - add_sample(features, label): Append a sample.
    - size(): Return number of samples.
    - labels(): Return a list of all labels.
    - label_distribution(): Return dict {label: count}.
    - split(ratio=0.8): Return (train_dataset, test_dataset) where train has
                         ratio*size samples and test has the rest.
                         New datasets should have names: "name_train" and "name_test".
    - __len__: Return size of dataset.
    - __repr__: Return "Dataset(name='iris', size=150)"
    - __iter__: Allow iterating over samples.
    """

    def __init__(self, name):
        # YOUR CODE HERE
        pass

    def add_sample(self, features, label):
        # YOUR CODE HERE
        pass

    def size(self):
        # YOUR CODE HERE
        pass

    def labels(self):
        # YOUR CODE HERE
        pass

    def label_distribution(self):
        # YOUR CODE HERE
        pass

    def split(self, ratio=0.8):
        # YOUR CODE HERE
        pass

    def __len__(self):
        # YOUR CODE HERE
        pass

    def __repr__(self):
        # YOUR CODE HERE
        pass

    def __iter__(self):
        # YOUR CODE HERE
        pass


# ══════════════════════════════════════════════════════
# TEST RUNNER
# ══════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    def check(name, result, expected):
        nonlocal passed, failed
        if result == expected:
            print(f"  PASS  {name}")
            passed += 1
        else:
            print(f"  FAIL  {name}")
            print(f"         Expected: {expected}")
            print(f"         Got:      {result}")
            failed += 1

    print("\n=== MODULE 3 TESTS ===\n")

    # Bank Account
    acct = BankAccount("Alice")
    acct.deposit(500)
    acct.deposit(200)
    acct.withdraw(100)
    check("balance", acct.get_balance(), 600.0)
    check("history length", len(acct.get_history()), 3)
    check("str", str(acct), "BankAccount(owner='Alice', balance=$600.00)")

    try:
        acct.withdraw(10000)
        check("insufficient funds raises", False, True)
    except ValueError:
        check("insufficient funds raises", True, True)

    # Shapes
    c = Circle(5)
    r = Rectangle(4, 6)
    s = Square(3)

    check("circle area", round(c.area(), 4), round(math.pi * 25, 4))
    check("circle perimeter", round(c.perimeter(), 4), round(2 * math.pi * 5, 4))
    check("rect area", r.area(), 24)
    check("rect perimeter", r.perimeter(), 20)
    check("square area", s.area(), 9)
    check("circle > rect", c > r, True)   # 78.5 > 24

    # Dataset
    ds = Dataset("iris")
    for i in range(10):
        ds.add_sample([i, i*2], "cat" if i < 6 else "dog")

    check("dataset size", ds.size(), 10)
    check("dataset len", len(ds), 10)
    check("dataset repr", repr(ds), "Dataset(name='iris', size=10)")
    check("label dist", ds.label_distribution(), {"cat": 6, "dog": 4})

    train, test = ds.split(0.8)
    check("train size", train.size(), 8)
    check("test size", test.size(), 2)
    check("train name", train.name, "iris_train")

    # Test __iter__
    count = sum(1 for _ in ds)
    check("dataset iterable", count, 10)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed! Commit your work.")


if __name__ == "__main__":
    run_tests()
