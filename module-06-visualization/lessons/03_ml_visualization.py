"""
LESSON 3: Visualizing ML Results
==================================
The plots you'll create in every ML project: confusion matrices,
learning curves, feature importance, ROC curves.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

np.random.seed(42)

# ── 1. Learning Curves ────────────────────────────────
epochs = np.arange(1, 51)
train_loss = 2.0 * np.exp(-0.1 * epochs) + np.random.normal(0, 0.02, 50)
val_loss   = 2.2 * np.exp(-0.08 * epochs) + np.random.normal(0, 0.03, 50)
train_acc  = 1 - np.exp(-0.12 * epochs) * 0.9 + np.random.normal(0, 0.01, 50)
val_acc    = 1 - np.exp(-0.1 * epochs) * 0.92 + np.random.normal(0, 0.015, 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(epochs, train_loss, label="Train", color="blue", lw=2)
ax1.plot(epochs, val_loss,   label="Val",   color="red",  lw=2, linestyle="--")
ax1.fill_between(epochs, train_loss-0.05, train_loss+0.05, alpha=0.2, color="blue")
ax1.set(xlabel="Epoch", ylabel="Loss", title="Training & Validation Loss")
ax1.legend(); ax1.grid(True, alpha=0.3)

ax2.plot(epochs, train_acc, label="Train", color="green", lw=2)
ax2.plot(epochs, val_acc,   label="Val",   color="orange", lw=2, linestyle="--")
ax2.set(xlabel="Epoch", ylabel="Accuracy", title="Training & Validation Accuracy")
ax2.legend(); ax2.grid(True, alpha=0.3)

plt.suptitle("Model Training History", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("learning_curves.png", dpi=150)
plt.show()

# ── 2. Feature Importance ─────────────────────────────
features = ["age", "income", "education", "experience", "num_skills", "certifications"]
importances = np.array([0.23, 0.19, 0.17, 0.15, 0.14, 0.12])
colors = ["#2ecc71" if i == 0 else "#3498db" for i in range(len(features))]

plt.figure(figsize=(9, 5))
bars = plt.barh(features, importances, color=colors, edgecolor="black")
for bar, imp in zip(bars, importances):
    plt.text(bar.get_width() + 0.003, bar.get_y() + bar.get_height()/2,
             f"{imp:.0%}", va="center", fontweight="bold")
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150)
plt.show()

# ── 3. ROC Curve ──────────────────────────────────────
# Simulate model predictions
y_true = np.random.randint(0, 2, 200)
y_scores_good  = y_true * 0.7 + np.random.uniform(0, 0.3, 200)
y_scores_ok    = y_true * 0.4 + np.random.uniform(0, 0.6, 200)
y_scores_random = np.random.uniform(0, 1, 200)

def compute_roc(y_true, y_score):
    thresholds = np.linspace(0, 1, 100)
    tprs, fprs = [], []
    for t in thresholds:
        preds = (y_score >= t).astype(int)
        tp = ((preds==1) & (y_true==1)).sum()
        fp = ((preds==1) & (y_true==0)).sum()
        fn = ((preds==0) & (y_true==1)).sum()
        tn = ((preds==0) & (y_true==0)).sum()
        tprs.append(tp/(tp+fn+1e-10))
        fprs.append(fp/(fp+tn+1e-10))
    return fprs, tprs

plt.figure(figsize=(7, 6))
for label, scores, color in [
    ("Good Model",   y_scores_good,   "blue"),
    ("OK Model",     y_scores_ok,     "green"),
    ("Random",       y_scores_random, "red"),
]:
    fprs, tprs = compute_roc(y_true, scores)
    plt.plot(fprs, tprs, label=label, color=color, lw=2)

plt.plot([0, 1], [0, 1], "k--", alpha=0.5, label="No Skill")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves — Model Comparison")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("roc_curves.png", dpi=150)
plt.show()

import os
for f in ["learning_curves.png", "feature_importance.png", "roc_curves.png"]:
    if os.path.exists(f): os.remove(f)

print("\nModule 6 complete! Now do the exercises.")
