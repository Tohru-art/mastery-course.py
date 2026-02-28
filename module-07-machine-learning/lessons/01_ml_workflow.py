"""
LESSON 1: The Complete ML Workflow
=====================================
This is THE pattern you'll use for every ML project.
Master this flow and every model becomes easier.

Install: pip install scikit-learn
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix
)

# ══════════════════════════════════════════════════════════════
# THE ML WORKFLOW (memorize this pattern)
# ══════════════════════════════════════════════════════════════
#
# 1. LOAD & EXPLORE data
# 2. PREPROCESS  (clean, encode, scale)
# 3. SPLIT       (train / validation / test)
# 4. TRAIN model
# 5. EVALUATE    (accuracy, F1, confusion matrix)
# 6. IMPROVE     (tune, try different models)
# 7. REPORT      (explain results)
#
# ══════════════════════════════════════════════════════════════

print("=" * 50)
print("STEP 1: Load & Explore Data")
print("=" * 50)

iris = load_iris()
X = iris.data       # features: (150, 4) — sepal/petal length/width
y = iris.target     # labels: 0=setosa, 1=versicolor, 2=virginica

print(f"Features shape: {X.shape}")
print(f"Labels shape: {y.shape}")
print(f"Classes: {iris.target_names}")
print(f"Feature names: {iris.feature_names}")
print(f"\nFirst 5 rows:\n{X[:5]}")
print(f"\nClass distribution:")
for i, name in enumerate(iris.target_names):
    print(f"  {name}: {(y == i).sum()} samples")

print("\n" + "=" * 50)
print("STEP 2: Preprocess")
print("=" * 50)

# Feature scaling — required for many algorithms (SVM, logistic regression, KNN)
# StandardScaler: (x - mean) / std → mean=0, std=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fit on all data, then transform

print(f"Before scaling — mean: {X.mean(axis=0).round(2)}")
print(f"After scaling  — mean: {X_scaled.mean(axis=0).round(2)}")
print(f"After scaling  — std:  {X_scaled.std(axis=0).round(2)}")

print("\n" + "=" * 50)
print("STEP 3: Train/Test Split")
print("=" * 50)

# NEVER train and test on the same data!
# 80% train, 20% test — stratify keeps class balance in both splits
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42,   # for reproducibility
    stratify=y         # maintain class distribution
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

print("\n" + "=" * 50)
print("STEP 4: Train Model")
print("=" * 50)

model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train, y_train)   # LEARN from training data

print("Model trained!")

print("\n" + "=" * 50)
print("STEP 5: Evaluate")
print("=" * 50)

# Predict on TEST data (data model never saw)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("(rows=actual, cols=predicted)")

# Cross-validation — more reliable than a single train/test split
cv_scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"\n5-Fold Cross-Validation: {cv_scores.round(3)}")
print(f"Mean: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

print("\n" + "=" * 50)
print("STEP 6: Predict New Data")
print("=" * 50)

# In production: scale new data with the SAME fitted scaler
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])   # new measurement
new_flower_scaled = scaler.transform(new_flower)  # use fitted scaler!

prediction = model.predict(new_flower_scaled)
probabilities = model.predict_proba(new_flower_scaled)

print(f"Prediction: {iris.target_names[prediction[0]]}")
print(f"Probabilities: {dict(zip(iris.target_names, probabilities[0].round(3)))}")

# ── Key Mistakes to Avoid ─────────────────────────────────────────────────────
"""
COMMON MISTAKES:

1. DATA LEAKAGE — scaling BEFORE splitting
   BAD:  scaler.fit_transform(X)  → then split
   GOOD: split first, fit scaler on X_train only, transform both

2. NOT using random_state → results change every run

3. Using training accuracy as your metric
   BAD:  model.score(X_train, y_train)  ← of course it's good
   GOOD: model.score(X_test, y_test)   ← real evaluation

4. Ignoring class imbalance
   If 95% of labels are class 0, a model that always predicts 0 gets 95% accuracy!
   → Use F1 score, precision/recall for imbalanced data
"""

print("\nDone! Move on to 02_regression.py")
