"""
LESSON 5: Abstract Classes & Interfaces
=========================================
Abstract classes define a CONTRACT: "every subclass MUST implement these methods."
This is how libraries like PyTorch and sklearn enforce consistent interfaces.
"""

from abc import ABC, abstractmethod
import math

# ══════════════════════════════════════════════════════
# ABSTRACT BASE CLASS
# ══════════════════════════════════════════════════════
class Shape(ABC):   # ABC = Abstract Base Class
    """
    Abstract class — cannot be instantiated directly.
    Subclasses MUST implement area() and perimeter().
    """

    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape."""
        pass

    # Concrete method — shared by all subclasses
    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


# Can't instantiate abstract class
try:
    s = Shape()
except TypeError as e:
    print(f"Error: {e}")   # Can't instantiate abstract class

# Concrete subclasses MUST implement all abstract methods
class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w, h): self.width, self.height = w, h
    def area(self): return self.width * self.height
    def perimeter(self): return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2  # semi-perimeter
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
    def perimeter(self): return self.a + self.b + self.c

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(shape.describe())

# Polymorphism — all shapes share the same interface
total_area = sum(s.area() for s in shapes)
print(f"\nTotal area: {total_area:.2f}")

# ══════════════════════════════════════════════════════
# AI/ML EXAMPLE: BaseModel Interface (like PyTorch/sklearn)
# ══════════════════════════════════════════════════════
class BaseMLModel(ABC):
    """
    Every ML model in our system MUST implement:
    - fit(X, y): train the model
    - predict(X): make predictions
    - score(X, y): evaluate performance
    """

    @abstractmethod
    def fit(self, X, y):
        """Train the model on features X and labels y."""
        pass

    @abstractmethod
    def predict(self, X):
        """Return predictions for X. Must call fit first."""
        pass

    def score(self, X, y):
        """Default: accuracy score. Subclasses can override."""
        predictions = self.predict(X)
        correct = sum(p == t for p, t in zip(predictions, y))
        return correct / len(y)

    def fit_predict(self, X_train, y_train, X_test):
        """Train then predict — template method pattern."""
        self.fit(X_train, y_train)
        return self.predict(X_test)


class MajorityClassifier(BaseMLModel):
    """Baseline: always predicts the most common class."""
    def __init__(self):
        self._majority = None

    def fit(self, X, y):
        from collections import Counter
        self._majority = Counter(y).most_common(1)[0][0]

    def predict(self, X):
        if self._majority is None:
            raise RuntimeError("Call fit() before predict()")
        return [self._majority] * len(X)


class KNNClassifier(BaseMLModel):
    """Simple K-Nearest Neighbors."""
    def __init__(self, k=3):
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self, X, y):
        self._X_train = X
        self._y_train = y

    def predict(self, X):
        from collections import Counter
        predictions = []
        for x in X:
            distances = [
                (sum((a-b)**2 for a,b in zip(x, xi))**0.5, yi)
                for xi, yi in zip(self._X_train, self._y_train)
            ]
            k_nearest = sorted(distances)[:self.k]
            vote = Counter(yi for _, yi in k_nearest).most_common(1)[0][0]
            predictions.append(vote)
        return predictions


X_train = [[1,1],[1,2],[2,1],[5,5],[5,6],[6,5]]
y_train = [0, 0, 0, 1, 1, 1]
X_test  = [[1.5, 1.5], [5.5, 5.5]]
y_test  = [0, 1]

for model in [MajorityClassifier(), KNNClassifier(k=3)]:
    preds = model.fit_predict(X_train, y_train, X_test)
    acc = model.score(X_test, y_test)
    print(f"\n{type(model).__name__}: preds={preds}, accuracy={acc:.0%}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Abstract classes define a contract — subclasses MUST implement @abstractmethods
# 2. You cannot instantiate an abstract class directly
# 3. Concrete methods in abstract classes are shared by all subclasses (template methods)
# 4. This is exactly how torch.nn.Module and sklearn estimators work
print("\nModule 3 lessons complete! Now do the exercises.")
