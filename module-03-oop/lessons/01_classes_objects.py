"""
LESSON 1: Classes & Objects
=============================
A class is a blueprint. An object is an instance of that blueprint.
In AI: your Dataset, Model, Trainer are all classes.
"""

# ── 1. Defining a Class ───────────────────────────────────────────────────────
class Dog:
    # Class attribute — shared by ALL instances
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, age):
        # Instance attributes — unique to each object
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"


# Creating objects (instances)
rex = Dog("Rex", "German Shepherd", 3)
buddy = Dog("Buddy", "Labrador", 5)

print(rex.bark())
print(buddy.describe())
print(Dog.species)      # access class attribute via class
print(rex.species)      # also accessible via instance

# ── 2. AI/ML Example: A Model Config Class ────────────────────────────────────
class ModelConfig:
    """Stores hyperparameters for a machine learning model."""

    # Default hyperparameters (class attributes)
    DEFAULT_LR = 0.001
    DEFAULT_EPOCHS = 50

    def __init__(self, model_name, learning_rate=None, epochs=None, batch_size=32):
        self.model_name = model_name
        self.learning_rate = learning_rate or self.DEFAULT_LR
        self.epochs = epochs or self.DEFAULT_EPOCHS
        self.batch_size = batch_size
        self.metrics = []

    def add_metric(self, name, value):
        self.metrics.append({"name": name, "value": value, "epoch": len(self.metrics) + 1})

    def best_metric(self, metric_name):
        relevant = [m["value"] for m in self.metrics if m["name"] == metric_name]
        return max(relevant) if relevant else None

    def summary(self):
        print(f"Model: {self.model_name}")
        print(f"  Learning Rate: {self.learning_rate}")
        print(f"  Epochs: {self.epochs}")
        print(f"  Batch Size: {self.batch_size}")


config = ModelConfig("ResNet-50", learning_rate=0.0001, epochs=100)
config.add_metric("accuracy", 0.82)
config.add_metric("accuracy", 0.89)
config.add_metric("accuracy", 0.94)
config.summary()
print(f"Best accuracy: {config.best_metric('accuracy')}")

# ── 3. Class Methods & Static Methods ────────────────────────────────────────
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor — create from Fahrenheit"""
        return cls((fahrenheit - 32) * 5/9)

    @staticmethod
    def is_freezing(celsius):
        """Utility — doesn't need self or cls"""
        return celsius <= 0

    def __repr__(self):
        return f"Temperature({self.celsius}°C / {self.fahrenheit}°F)"


t1 = Temperature(100)
t2 = Temperature.from_fahrenheit(32)   # classmethod
print(t1)
print(t2)
print(Temperature.is_freezing(-5))    # staticmethod

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. __init__ sets up instance attributes (unique per object)
# 2. Class attributes are shared across all instances
# 3. @classmethod: alternative constructors (gets class as first arg)
# 4. @staticmethod: utility functions that don't need class/instance
print("\nDone! Move on to 02_inheritance.py")
