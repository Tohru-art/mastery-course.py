"""
LESSON 3: Decision Trees & Random Forests
==========================================
Tree-based models are the most widely used in industry (after neural nets).
Random Forests are usually the first model to try on tabular data.
"""

import numpy as np
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ══════════════════════════════════════════════════════
# DECISION TREE
# ══════════════════════════════════════════════════════
"""
A decision tree splits data at thresholds (e.g., "mean radius > 14.5?")
choosing the split that best separates classes (measured by Gini impurity).

Pros: Interpretable, no scaling needed
Cons: Overfits easily (max_depth controls this)
"""
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, dt.predict(X_test)):.3f}")

# Visualize what it learned
print(f"\nTree depth: {dt.get_depth()}")
print(f"Leaf nodes: {dt.get_n_leaves()}")
print(f"Top 5 features: {np.argsort(dt.feature_importances_)[::-1][:5]}")
print(f"Top 5 feature names: {[data.feature_names[i] for i in np.argsort(dt.feature_importances_)[::-1][:5]]}")

# ══════════════════════════════════════════════════════
# RANDOM FOREST — ensemble of trees
# ══════════════════════════════════════════════════════
"""
Random Forest = many decision trees, each trained on a random subset
of data AND features. Average their predictions.

WHY IT WORKS: Individual trees overfit, but in different ways.
Averaging them cancels out the noise. This is "bagging."

Pros: Very strong out-of-the-box, no scaling needed, handles missing data
Cons: Less interpretable than a single tree, slower to train
"""
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print(f"\nRandom Forest Accuracy: {accuracy_score(y_test, y_pred_rf):.3f}")
print(classification_report(y_test, y_pred_rf, target_names=["malignant", "benign"]))

# Feature importance
importances = rf.feature_importances_
top5_idx = np.argsort(importances)[::-1][:5]
print("Top 5 important features:")
for i in top5_idx:
    print(f"  {data.feature_names[i]}: {importances[i]:.3f}")

# Out-of-bag score (free validation without a separate test set)
rf_oob = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
rf_oob.fit(X_train, y_train)
print(f"\nOOB Score: {rf_oob.oob_score_:.3f}")  # similar to cross-val

# ══════════════════════════════════════════════════════
# GRADIENT BOOSTING — sequential ensemble
# ══════════════════════════════════════════════════════
"""
Unlike Random Forest (parallel trees), Gradient Boosting builds trees
SEQUENTIALLY — each tree corrects the errors of the previous.
Often slightly better than Random Forest but slower.
"""
gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1,
                                  max_depth=3, random_state=42)
gb.fit(X_train, y_train)
print(f"\nGradient Boosting Accuracy: {accuracy_score(y_test, gb.predict(X_test)):.3f}")

# ── Comparison ────────────────────────────────────────
models = {
    "Decision Tree": dt,
    "Random Forest": rf,
    "Gradient Boosting": gb,
}
print("\n── Model Comparison (5-fold CV) ──")
for name, model in models.items():
    cv = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    print(f"{name:20s}: {cv.mean():.3f} ± {cv.std():.3f}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Decision trees are interpretable but overfit — control with max_depth
# 2. Random Forest: parallel ensemble → robust, great default
# 3. Gradient Boosting: sequential ensemble → often slightly better
# 4. Feature importance from RF is very useful for feature selection
# 5. Tree models DON'T require feature scaling
print("\nDone! Move on to 04_features.py")
