"""
LESSON 2: Seaborn — Statistical Visualization
===============================================
Seaborn builds on Matplotlib for beautiful statistical plots in one line.
Install: pip install seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")   # clean default style
np.random.seed(42)

# ── Build a dataset ───────────────────────────────────
df = pd.DataFrame({
    "model": ["Logistic"]*30 + ["Random Forest"]*30 + ["Neural Net"]*30,
    "accuracy": (
        list(np.random.normal(0.82, 0.03, 30)) +
        list(np.random.normal(0.91, 0.02, 30)) +
        list(np.random.normal(0.94, 0.015, 30))
    ),
    "dataset_size": np.random.choice([100, 500, 1000, 5000], 90),
    "training_time": np.random.exponential(2, 90),
})

# ── 1. Distribution plot ──────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram + KDE
sns.histplot(data=df, x="accuracy", hue="model", kde=True,
             bins=20, alpha=0.5, ax=axes[0])
axes[0].set_title("Accuracy Distribution by Model")

# Box plot — shows median, quartiles, outliers
sns.boxplot(data=df, x="model", y="accuracy", ax=axes[1])
axes[1].set_title("Accuracy Spread by Model")
axes[1].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig("seaborn_distributions.png", dpi=150)
plt.show()

# ── 2. Relationship plots ─────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatter with regression line
sns.regplot(data=df, x="dataset_size", y="accuracy", ax=axes[0])
axes[0].set_title("Accuracy vs Dataset Size")

# Scatter colored by model
sns.scatterplot(data=df, x="training_time", y="accuracy",
                hue="model", style="model", s=60, ax=axes[1])
axes[1].set_title("Accuracy vs Training Time")

plt.tight_layout()
plt.savefig("seaborn_relationships.png", dpi=150)
plt.show()

# ── 3. Correlation heatmap ────────────────────────────
numeric_df = df[["accuracy", "dataset_size", "training_time"]]
corr = numeric_df.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, square=True)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("seaborn_heatmap.png", dpi=150)
plt.show()

# ── 4. Violin plot — distribution shape ───────────────
plt.figure(figsize=(10, 5))
sns.violinplot(data=df, x="model", y="accuracy", inner="box")
plt.title("Accuracy Distribution (Violin)")
plt.tight_layout()
plt.savefig("seaborn_violin.png", dpi=150)
plt.show()

# Cleanup
import os
for f in ["seaborn_distributions.png", "seaborn_relationships.png",
          "seaborn_heatmap.png", "seaborn_violin.png"]:
    if os.path.exists(f): os.remove(f)

print("\nDone! Move on to 03_ml_visualization.py")
