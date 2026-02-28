"""
MODULE 7 EXERCISES — Machine Learning
=======================================
Run: python exercises/exercises_07.py
Install: pip install scikit-learn
"""
import numpy as np
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score


# ══════════════════════════════════════════════════════
# EXERCISE 1: Complete ML Pipeline
# ══════════════════════════════════════════════════════
def train_and_evaluate(X, y, model, test_size=0.2, random_state=42):
    """
    Complete ML pipeline:
    1. Split into train/test with stratify=y
    2. Scale with StandardScaler (fit on train only!)
    3. Train the model
    4. Return a dict:
       {"accuracy": ..., "f1": ..., "model": trained_model, "scaler": fitted_scaler}
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# EXERCISE 2: Find the Best Model
# ══════════════════════════════════════════════════════
def find_best_model(X, y, models: dict) -> dict:
    """
    Given a dict of {name: model}, train and evaluate each one.
    Return a dict: {"best_name": str, "best_score": float,
                    "all_scores": {name: score}}
    Use 5-fold cross-validation with accuracy scoring.
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# EXERCISE 3: Fix the Buggy ML Code
# ══════════════════════════════════════════════════════
def buggy_ml_pipeline(X, y):
    """
    This function has 3 bugs. Find and fix them all.
    Return: {"accuracy": float, "note": "bugs fixed"}

    BUG HINTS (don't look until you've tried!):
    1. Data leakage in scaling
    2. Evaluating on wrong set
    3. Missing stratify
    """
    from sklearn.linear_model import LogisticRegression

    # BUG 1: scaler fitted on ALL data before split
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # BUG 2: No stratify
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    # BUG 3: Evaluating on training data
    accuracy = accuracy_score(y_train, model.predict(X_train))
    return {"accuracy": accuracy, "note": "not fixed yet"}


# ══════════════════════════════════════════════════════
# EXERCISE 4: Feature Importance
# ══════════════════════════════════════════════════════
def get_top_features(X, y, feature_names: list, n: int = 5) -> list:
    """
    Train a RandomForestClassifier and return the top-n most important
    feature names as a list (sorted by importance, highest first).
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# TEST RUNNER
# ══════════════════════════════════════════════════════
def run_tests():
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier

    passed = failed = 0
    def check(name, result, expected, tol=0.01):
        nonlocal passed, failed
        ok = abs(result - expected) <= tol if isinstance(expected, float) else result == expected
        if ok: print(f"  PASS  {name}"); passed += 1
        else:
            print(f"  FAIL  {name}")
            print(f"         Expected: {expected}, Got: {result}")
            failed += 1

    print("\n=== MODULE 7 TESTS ===\n")

    iris = load_iris()
    X, y = iris.data, iris.target

    # Exercise 1
    result = train_and_evaluate(X, y, LogisticRegression(max_iter=200, random_state=42))
    if result:
        check("pipeline returns accuracy", "accuracy" in result, True)
        check("pipeline accuracy >= 0.9", result.get("accuracy", 0) >= 0.9, True)
        check("pipeline has scaler", result.get("scaler") is not None, True)

    # Exercise 2
    models = {
        "logistic": LogisticRegression(max_iter=200, random_state=42),
        "rf": RandomForestClassifier(n_estimators=50, random_state=42),
        "dt": DecisionTreeClassifier(random_state=42),
    }
    best = find_best_model(X, y, models)
    if best:
        check("find_best has best_name", "best_name" in best, True)
        check("find_best has all_scores", len(best.get("all_scores", {})), 3)
        check("best score >= 0.9", best.get("best_score", 0) >= 0.9, True)

    # Exercise 3 — fixed version should have accuracy on TEST set
    cancer = load_breast_cancer()
    fixed = buggy_ml_pipeline(cancer.data, cancer.target)
    if fixed:
        check("bugs fixed note", "fixed" in fixed.get("note", "").lower(), True)
        check("test accuracy reasonable", 0.85 <= fixed.get("accuracy", 0) <= 1.0, True)

    # Exercise 4
    top = get_top_features(X, y, iris.feature_names.tolist(), n=3)
    if top:
        check("top features count", len(top), 3)
        check("top features are strings", all(isinstance(f, str) for f in top), True)

    print(f"\n{'='*30}\nResults: {passed} passed, {failed} failed")
    if failed == 0: print("All tests passed! Commit your work.")

if __name__ == "__main__":
    run_tests()
