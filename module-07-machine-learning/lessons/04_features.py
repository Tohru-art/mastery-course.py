"""
LESSON 4: Feature Engineering & Preprocessing
===============================================
"Garbage in, garbage out." Better features = better models.
This is where domain knowledge meets ML.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, LabelEncoder,
    OneHotEncoder, PolynomialFeatures
)
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

np.random.seed(42)

# ══════════════════════════════════════════════════════
# SCALING — most models need this
# ══════════════════════════════════════════════════════
data = np.array([[1000, 0.5], [2000, 1.5], [3000, 2.5], [4000, 3.5]])

# StandardScaler: mean=0, std=1 — best for most models
ss = StandardScaler()
print("Standard scaled:\n", ss.fit_transform(data).round(3))

# MinMaxScaler: range [0,1] — good for neural networks
mm = MinMaxScaler()
print("MinMax scaled:\n", mm.fit_transform(data).round(3))

# ══════════════════════════════════════════════════════
# ENCODING CATEGORICAL VARIABLES
# ══════════════════════════════════════════════════════
df = pd.DataFrame({
    "color": ["red", "blue", "green", "red", "blue"],
    "size":  ["S", "M", "L", "XL", "M"],
    "price": [10, 20, 15, 12, 22]
})

# Label Encoding — only for ordinal (S < M < L < XL)
size_order = {"S": 0, "M": 1, "L": 2, "XL": 3}
df["size_encoded"] = df["size"].map(size_order)
print("\nLabel encoded size:\n", df[["size", "size_encoded"]])

# One-Hot Encoding — for nominal categories (no order)
ohe = pd.get_dummies(df["color"], prefix="color")
df_ohe = pd.concat([df, ohe], axis=1)
print("\nOne-hot encoded:\n", df_ohe)

# ══════════════════════════════════════════════════════
# HANDLING MISSING VALUES
# ══════════════════════════════════════════════════════
X = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9], [np.nan, 11, 12]])
print("\nWith missing:\n", X)

imputer = SimpleImputer(strategy="mean")  # fill with column mean
print("After imputing:\n", imputer.fit_transform(X).round(2))

# Other strategies: "median", "most_frequent", "constant"

# ══════════════════════════════════════════════════════
# FEATURE CREATION
# ══════════════════════════════════════════════════════
# From real dataset
housing = pd.DataFrame({
    "area_sqft": [1200, 1800, 900, 2400, 1500],
    "bedrooms":  [2, 3, 1, 4, 3],
    "bathrooms": [1, 2, 1, 3, 2],
    "age_years": [10, 5, 25, 2, 15],
    "price":     [250000, 380000, 180000, 520000, 310000]
})

# Create interaction features
housing["price_per_sqft"] = housing["price"] / housing["area_sqft"]
housing["bed_bath_ratio"] = housing["bedrooms"] / housing["bathrooms"]
housing["area_per_bedroom"] = housing["area_sqft"] / housing["bedrooms"]
housing["is_new"] = (housing["age_years"] < 10).astype(int)

print("\nEngineered features:\n",
      housing[["area_per_bedroom", "bed_bath_ratio", "is_new"]].head())

# Polynomial features (for non-linear relationships)
X_simple = np.array([[1], [2], [3], [4]])
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_simple)
print("\nPolynomial features (degree=2):\n", X_poly)  # [x, x²]

# ══════════════════════════════════════════════════════
# SKLEARN PIPELINE — chain everything together
# ══════════════════════════════════════════════════════
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("imputer",  SimpleImputer(strategy="mean")),
    ("scaler",   StandardScaler()),
    ("model",    RandomForestClassifier(n_estimators=50, random_state=42))
])

pipeline.fit(X_train, y_train)
print(f"\nPipeline accuracy: {pipeline.score(X_test, y_test):.3f}")

# The pipeline handles everything — no data leakage!
# pipeline.predict(X_new)  ← automatically imputes and scales new data

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. StandardScaler for most models; MinMaxScaler for neural nets
# 2. Label encoding for ordinal; One-hot for nominal
# 3. Use SimpleImputer — don't drop rows with missing data blindly
# 4. Create features that capture domain knowledge (price per sqft, ratios)
# 5. Always use Pipeline — prevents data leakage and keeps code clean
print("\nDone! Move on to 05_evaluation.py")
