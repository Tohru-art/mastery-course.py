"""
LESSON 1: Matplotlib Basics
=============================
Matplotlib is the foundation of Python visualization.
You'll use it to plot training curves, confusion matrices, and data distributions.

Install: pip install matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

# ── 1. Line Plot — Training Curves ────────────────────────────────────────────
epochs = list(range(1, 21))
train_loss = [1.0 / (e ** 0.5) + np.random.normal(0, 0.02) for e in epochs]
val_loss = [1.0 / (e ** 0.4) + np.random.normal(0, 0.03) for e in epochs]

plt.figure(figsize=(10, 4))
plt.plot(epochs, train_loss, label="Train Loss", color="blue", linewidth=2)
plt.plot(epochs, val_loss, label="Val Loss", color="red", linestyle="--", linewidth=2)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("training_curves.png", dpi=150)
plt.show()
print("Saved: training_curves.png")

# ── 2. Bar Chart — Model Comparison ──────────────────────────────────────────
models = ["Logistic Reg", "Random Forest", "SVM", "Neural Net", "Transformer"]
accuracies = [0.82, 0.91, 0.88, 0.94, 0.97]

colors = ["#4CAF50" if a >= 0.90 else "#FF9800" for a in accuracies]

plt.figure(figsize=(10, 5))
bars = plt.bar(models, accuracies, color=colors, edgecolor="black", width=0.6)
plt.axhline(y=0.90, color="red", linestyle="--", label="90% threshold")

# Add value labels on bars
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f"{acc:.0%}", ha="center", va="bottom", fontweight="bold")

plt.ylim(0, 1.05)
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.legend()
plt.tight_layout()
plt.savefig("model_comparison.png", dpi=150)
plt.show()

# ── 3. Scatter Plot — Data Distribution ──────────────────────────────────────
np.random.seed(42)
class_0 = np.random.randn(100, 2) + [0, 0]
class_1 = np.random.randn(100, 2) + [3, 3]

plt.figure(figsize=(8, 6))
plt.scatter(class_0[:, 0], class_0[:, 1], c="blue", alpha=0.6, label="Class 0", s=50)
plt.scatter(class_1[:, 0], class_1[:, 1], c="red", alpha=0.6, label="Class 1", s=50)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("2D Feature Space — Two Classes")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("scatter.png", dpi=150)
plt.show()

# ── 4. Subplots — Multiple plots in one figure ────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Histogram
data = np.random.normal(70, 15, 500)
axes[0].hist(data, bins=30, color="steelblue", edgecolor="black", alpha=0.7)
axes[0].set_title("Score Distribution")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Count")

# Plot 2: Line with confidence band
x = np.linspace(0, 10, 100)
y = np.sin(x)
noise = 0.2
axes[1].plot(x, y, color="blue", label="Signal", linewidth=2)
axes[1].fill_between(x, y - noise, y + noise, alpha=0.3, color="blue")
axes[1].set_title("Signal with Confidence Band")
axes[1].legend()

# Plot 3: Pie chart
labels = ["Python", "JavaScript", "Java", "Other"]
sizes = [45, 25, 20, 10]
axes[2].pie(sizes, labels=labels, autopct="%1.0f%%", startangle=90,
            colors=["#FF6B6B", "#4ECDC4", "#45B7D1", "#95E1D3"])
axes[2].set_title("Language Popularity")

plt.suptitle("My Analytics Dashboard", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
plt.show()

# ── 5. Confusion Matrix ────────────────────────────────────────────────────────
# This is one of the most important plots in ML evaluation
confusion = np.array([[45, 5, 0],
                       [3, 38, 9],
                       [1, 4, 45]])
class_names = ["Cat", "Dog", "Bird"]

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(confusion, cmap="Blues")
plt.colorbar(im)

ax.set_xticks(range(len(class_names)))
ax.set_yticks(range(len(class_names)))
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")

# Add numbers to cells
for i in range(len(class_names)):
    for j in range(len(class_names)):
        color = "white" if confusion[i, j] > 30 else "black"
        ax.text(j, i, confusion[i, j], ha="center", va="center",
                fontweight="bold", color=color, fontsize=12)

plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.show()

import os
for f in ["training_curves.png", "model_comparison.png", "scatter.png", "dashboard.png", "confusion_matrix.png"]:
    if os.path.exists(f):
        os.remove(f)

print("\nDone! Move on to 02_seaborn.py")
