"""
LESSON 2: Inheritance & Polymorphism
======================================
Inheritance lets a class reuse code from another class.
Polymorphism means different classes can share the same interface.
In AI: BaseModel → CNNModel, RNNModel, TransformerModel
"""

# ── 1. Basic Inheritance ──────────────────────────────────────────────────────
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):              # Dog inherits from Animal
    def __init__(self, name):
        super().__init__(name, "Woof")   # call parent's __init__
        self.tricks = []

    def learn_trick(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            return f"{self.name} knows: {', '.join(self.tricks)}"
        return f"{self.name} knows no tricks yet"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def speak(self):            # Override parent method
        return f"{self.name} says... Meow (gracefully)"


rex = Dog("Rex")
rex.learn_trick("sit")
rex.learn_trick("shake")
print(rex.speak())
print(rex.show_tricks())

cat = Cat("Whiskers")
print(cat.speak())   # uses overridden version

# ── 2. Polymorphism ───────────────────────────────────────────────────────────
# Different objects, same interface
animals = [Dog("Rex"), Cat("Whiskers"), Animal("Parrot", "Polly wants a cracker")]

for animal in animals:
    print(animal.speak())   # each uses their own speak()

# ── 3. AI/ML Inheritance Example ─────────────────────────────────────────────
class BaseModel:
    """Base class for all ML models."""

    def __init__(self, name, version="1.0"):
        self.name = name
        self.version = version
        self.is_trained = False
        self._training_history = []

    def train(self, data):
        raise NotImplementedError("Subclasses must implement train()")

    def predict(self, input_data):
        if not self.is_trained:
            raise RuntimeError(f"{self.name} must be trained before predicting")
        raise NotImplementedError("Subclasses must implement predict()")

    def log_epoch(self, epoch, loss, accuracy):
        self._training_history.append({
            "epoch": epoch, "loss": loss, "accuracy": accuracy
        })

    def best_accuracy(self):
        if not self._training_history:
            return None
        return max(e["accuracy"] for e in self._training_history)

    def __repr__(self):
        status = "trained" if self.is_trained else "untrained"
        return f"{self.__class__.__name__}(name={self.name!r}, status={status})"


class LinearClassifier(BaseModel):
    def __init__(self, name, learning_rate=0.01):
        super().__init__(name)
        self.learning_rate = learning_rate
        self.weights = None

    def train(self, data):
        print(f"Training {self.name} with lr={self.learning_rate}...")
        # Simulate training
        for epoch in range(1, 4):
            loss = 1.0 / epoch
            accuracy = 0.6 + 0.1 * epoch
            self.log_epoch(epoch, loss, accuracy)
            print(f"  Epoch {epoch}: loss={loss:.3f}, accuracy={accuracy:.1%}")
        self.is_trained = True
        self.weights = [0.1, 0.3, -0.2]  # fake weights

    def predict(self, input_data):
        super().predict(input_data)  # checks is_trained
        return "positive" if sum(input_data) > 0 else "negative"


class TreeClassifier(BaseModel):
    def __init__(self, name, max_depth=5):
        super().__init__(name)
        self.max_depth = max_depth

    def train(self, data):
        print(f"Training {self.name} decision tree (depth={self.max_depth})...")
        self.is_trained = True

    def predict(self, input_data):
        super().predict(input_data)
        return "positive"


# Polymorphism in action
models = [
    LinearClassifier("LogReg", learning_rate=0.001),
    TreeClassifier("DecisionTree", max_depth=10),
]

for model in models:
    model.train([])           # same interface, different behavior
    print(repr(model))

# ── 4. isinstance() and type() ────────────────────────────────────────────────
clf = LinearClassifier("test")
print(isinstance(clf, LinearClassifier))   # True
print(isinstance(clf, BaseModel))          # True — it's a subclass!
print(isinstance(clf, TreeClassifier))     # False

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. super().__init__() calls the parent class's constructor
# 2. Override methods to customize behavior in subclasses
# 3. Polymorphism: treat different objects the same way via shared interface
# 4. isinstance() checks if object is instance of a class OR its subclasses
print("\nDone! Move on to 03_magic_methods.py")
