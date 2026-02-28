"""
LESSON 2: Linear & Logistic Regression
========================================
The two workhorses of ML. Understanding them deeply helps you
understand every more complex model.
"""

import numpy as np
from sklearn.datasets import make_regression, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# ══════════════════════════════════════════════════════
# LINEAR REGRESSION — predict a continuous value
# ══════════════════════════════════════════════════════
print("=" * 40)
print("LINEAR REGRESSION")
print("=" * 40)

X, y = make_regression(n_samples=200, n_features=5, noise=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)

print(f"R² Score: {r2_score(y_test, y_pred):.3f}")   # 1.0 = perfect
print(f"RMSE: {mean_squared_error(y_test, y_pred)**0.5:.2f}")
print(f"Coefficients: {model.coef_.round(2)}")
print(f"Intercept: {model.intercept_:.2f}")

# Ridge — adds L2 penalty to prevent overfitting
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_s, y_train)
print(f"\nRidge R²: {r2_score(y_test, ridge.predict(X_test_s)):.3f}")

# Lasso — adds L1 penalty, drives some coefficients to 0 (feature selection)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_s, y_train)
print(f"Lasso R²: {r2_score(y_test, lasso.predict(X_test_s)):.3f}")
print(f"Lasso non-zero coefficients: {(lasso.coef_ != 0).sum()}")

# ══════════════════════════════════════════════════════
# LOGISTIC REGRESSION — predict a category
# ══════════════════════════════════════════════════════
print("\n" + "=" * 40)
print("LOGISTIC REGRESSION")
print("=" * 40)

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                     random_state=42, stratify=y)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

clf = LogisticRegression(max_iter=200, random_state=42)
clf.fit(X_train_s, y_train)
y_pred = clf.predict(X_test_s)
y_prob = clf.predict_proba(X_test_s)[:, 1]

print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["malignant", "benign"]))

# Confidence threshold
print("High confidence predictions (>90%):")
high_conf = y_prob > 0.9
print(f"  {high_conf.sum()} out of {len(y_prob)} predictions")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# LINEAR REG: predict continuous values. Evaluate with R², RMSE.
# LOGISTIC REG: predict classes. Evaluate with accuracy, F1, AUC.
# RIDGE: L2 regularization — shrinks coefficients, good default
# LASSO: L1 regularization — zeros out weak features (automatic feature selection)
print("\nDone! Move on to 03_trees.py")
