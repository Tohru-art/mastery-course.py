"""
LESSON 5: Model Evaluation & Improving AI-Generated Code
==========================================================
A model isn't good until you can PROVE it's good.
Also: how to critically evaluate and fix AI-generated ML code.
(Directly from CodePath AI110 objectives)
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, classification_report
)

# ── 1. The Core Metrics ───────────────────────────────────────────────────────
"""
CONFUSION MATRIX:
              Predicted Positive  Predicted Negative
Actual Pos    TP (True Pos)       FN (False Neg)
Actual Neg    FP (False Pos)      TN (True Neg)

ACCURACY    = (TP + TN) / Total  — "how often is it right?"
PRECISION   = TP / (TP + FP)     — "of all positives predicted, how many are real?"
RECALL      = TP / (TP + FN)     — "of all real positives, how many did we catch?"
F1 SCORE    = 2 * P * R / (P+R)  — harmonic mean of precision & recall

When to use which:
- ACCURACY: balanced classes
- PRECISION: false positives are expensive (spam → you don't want good email in spam)
- RECALL: false negatives are expensive (cancer → you don't want to miss a case)
- F1: when both matter
- ROC-AUC: overall model quality, good for imbalanced classes
"""

# ── 2. Building an Imbalanced Dataset ────────────────────────────────────────
X, y = make_classification(
    n_samples=1000, n_features=20,
    n_informative=10, n_redundant=5,
    weights=[0.9, 0.1],   # 90% class 0, 10% class 1 — IMBALANCED
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)
y_prob = model.predict_proba(X_test_s)[:, 1]

print("=== Model Evaluation ===")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}  ← looks great, but deceiving!")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred):.3f}  ← only catching this % of positives")
print(f"F1 Score:  {f1_score(y_test, y_pred):.3f}")
print(f"ROC-AUC:   {roc_auc_score(y_test, y_prob):.3f}")
print()
print(classification_report(y_test, y_pred, target_names=["Majority", "Minority"]))

# ── 3. Fixing the Class Imbalance Problem ─────────────────────────────────────
model_balanced = LogisticRegression(class_weight="balanced", random_state=42)
model_balanced.fit(X_train_s, y_train)
y_pred_b = model_balanced.predict(X_test_s)

print("=== Balanced Model ===")
print(f"Recall (minority): {recall_score(y_test, y_pred_b):.3f}  ← much better!")
print(f"F1 Score: {f1_score(y_test, y_pred_b):.3f}")

# ── 4. Hyperparameter Tuning with GridSearchCV ────────────────────────────────
print("\n=== Hyperparameter Tuning ===")
param_grid = {
    "C": [0.01, 0.1, 1, 10],         # regularization strength
    "penalty": ["l1", "l2"],
    "solver": ["liblinear"]
}

grid_search = GridSearchCV(
    LogisticRegression(class_weight="balanced", random_state=42),
    param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1          # use all CPU cores
)
grid_search.fit(X_train_s, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best CV F1: {grid_search.best_score_:.3f}")

best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test_s)
print(f"Test F1 with best params: {f1_score(y_test, y_pred_best):.3f}")

# ── 5. Critically Evaluating AI-Generated Code ────────────────────────────────
"""
CodePath AI110 Goal: Assess, test, and improve AI-generated code.

Common bugs in AI-generated ML code:

BUG 1: Data leakage
  AI might write: scaler.fit_transform(X) → then split
  FIX: Always split first, fit scaler only on X_train

BUG 2: Wrong evaluation
  AI might write: model.score(X_train, y_train)  ← training accuracy
  FIX: Always evaluate on X_test (held-out data)

BUG 3: Missing stratify in split
  AI might write: train_test_split(X, y, test_size=0.2)
  FIX: Add stratify=y to preserve class balance

BUG 4: Not setting random_state
  AI might write: LogisticRegression()
  FIX: Always set random_state=42 for reproducibility

BUG 5: Using accuracy for imbalanced data
  AI might report: "98% accuracy!" (but 98% of data is class 0)
  FIX: Use F1, precision, recall, ROC-AUC

WORKFLOW FOR REVIEWING AI-GENERATED ML CODE:
1. Check for data leakage (scaler fit before split?)
2. Check evaluation metric (appropriate for the task?)
3. Check reproducibility (random_state set?)
4. Check for class imbalance handling
5. Run the code and verify results make sense
6. Test edge cases (empty input, all-same class, etc.)
"""

print("\nDone! Module 7 lessons complete. Now do the exercises.")
