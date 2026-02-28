"""
LESSON 6: Clustering — Unsupervised Learning
=============================================
Clustering finds patterns in data WITHOUT labels.
Use it for: customer segmentation, anomaly detection, data exploration.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

np.random.seed(42)

# ══════════════════════════════════════════════════════
# K-MEANS CLUSTERING
# ══════════════════════════════════════════════════════
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

print(f"Silhouette score: {silhouette_score(X_scaled, labels):.3f}")
print(f"Cluster centers (scaled):\n{kmeans.cluster_centers_.round(2)}")
print(f"Samples per cluster: {dict(zip(*np.unique(labels, return_counts=True)))}")

# ── Choosing K: Elbow Method ──────────────────────────
inertias = []
silhouettes = []
K_range = range(2, 9)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, km.labels_))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(K_range, inertias, "bo-"); ax1.set(xlabel="k", ylabel="Inertia", title="Elbow Method")
ax2.plot(K_range, silhouettes, "ro-"); ax2.set(xlabel="k", ylabel="Silhouette", title="Silhouette Score")
plt.tight_layout()
plt.savefig("clustering_elbow.png", dpi=150); plt.show()

# ══════════════════════════════════════════════════════
# DBSCAN — finds clusters of arbitrary shape
# ══════════════════════════════════════════════════════
X_moons, _ = make_moons(n_samples=300, noise=0.1, random_state=42)

# K-Means fails on non-spherical clusters
km_fail = KMeans(n_clusters=2, random_state=42)
labels_km = km_fail.fit_predict(X_moons)

# DBSCAN handles arbitrary shapes
dbscan = DBSCAN(eps=0.3, min_samples=5)
labels_db = dbscan.fit_predict(X_moons)  # -1 = noise point

n_clusters = len(set(labels_db)) - (1 if -1 in labels_db else 0)
n_noise = (labels_db == -1).sum()
print(f"\nDBSCAN: {n_clusters} clusters, {n_noise} noise points")

# ══════════════════════════════════════════════════════
# PRACTICAL: Customer Segmentation
# ══════════════════════════════════════════════════════
customers = np.array([
    [25, 30000, 0.8],   # young, low income, high engagement
    [22, 28000, 0.9],
    [45, 80000, 0.3],   # middle-aged, high income, low engagement
    [50, 90000, 0.2],
    [35, 55000, 0.6],   # mid, mid, mid
    [30, 45000, 0.7],
    [60, 70000, 0.1],   # older, high income, very low engagement
    [55, 75000, 0.15],
])

X_cust = StandardScaler().fit_transform(customers)
km_cust = KMeans(n_clusters=3, random_state=42, n_init=10)
segments = km_cust.fit_predict(X_cust)

print("\nCustomer Segmentation:")
for i, (row, seg) in enumerate(zip(customers, segments)):
    print(f"  Customer {i+1} [Age:{row[0]:.0f}, Income:${row[1]:,.0f}, Eng:{row[2]:.0f}] → Segment {seg}")

import os
for f in ["clustering_elbow.png"]:
    if os.path.exists(f): os.remove(f)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. K-Means: fast, good for spherical clusters, you must choose k
# 2. DBSCAN: arbitrary shapes, auto-detects outliers, sensitive to eps
# 3. Silhouette score: closer to 1.0 = better cluster separation
# 4. Always scale features before clustering
# 5. Use elbow method + silhouette score to choose K
print("\nModule 7 lessons complete! Now do the exercises.")
