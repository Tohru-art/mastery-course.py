"""
LESSON 4: Pandas Data Cleaning
================================
Real-world data is messy. Cleaning it is 80% of AI/ML work.
This lesson covers the most common data quality issues you'll face.
"""

import pandas as pd
import numpy as np

# ── Create a Messy Dataset ────────────────────────────────────────────────────
raw_data = {
    "name": ["Alice", "Bob", None, "Dave", "Eve", "Dave"],
    "age": [22, None, 23, 21, -5, 21],
    "score": [85, 92, None, 95, 88, 95],
    "email": ["alice@example.com", "BOB@EXAMPLE.COM", "carol@example.com", "dave@example.com", "invalid-email", "dave@example.com"],
    "country": ["USA", "usa", "US", "United States", "USA", "usa"]
}

df = pd.DataFrame(raw_data)
print("Raw data:\n", df)
print("\nShape:", df.shape)

# ── 1. Finding Missing Values ─────────────────────────────────────────────────
print("\n-- Missing Values --")
print(df.isnull())              # bool mask
print(df.isnull().sum())        # count per column
print(f"Total missing: {df.isnull().sum().sum()}")

# ── 2. Handling Missing Values ────────────────────────────────────────────────
# Option A: Drop rows with any missing values
df_dropped = df.dropna()
print(f"\nAfter dropna: {df_dropped.shape}")

# Option B: Drop only if specific column is missing
df_no_name = df.dropna(subset=["name"])

# Option C: Fill missing values
df_filled = df.copy()
df_filled["age"] = df_filled["age"].fillna(df_filled["age"].median())
df_filled["score"] = df_filled["score"].fillna(df_filled["score"].mean())
df_filled["name"] = df_filled["name"].fillna("Unknown")
print("\nAfter filling:\n", df_filled)

# ── 3. Removing Duplicates ────────────────────────────────────────────────────
df_clean = df_filled.copy()
print(f"\nDuplicates: {df_clean.duplicated().sum()}")
df_clean = df_clean.drop_duplicates()
print(f"After removing duplicates: {df_clean.shape}")

# ── 4. Fixing Data Types ──────────────────────────────────────────────────────
# Check types
print("\nDtypes:", df_clean.dtypes)

# Convert age to integer (was float because of NaN)
df_clean["age"] = df_clean["age"].astype(int)

# Convert to categorical (saves memory for low-cardinality columns)
df_clean["country"] = df_clean["country"].astype("category")

# ── 5. Normalizing String Values ──────────────────────────────────────────────
# Email: standardize to lowercase
df_clean["email"] = df_clean["email"].str.lower().str.strip()

# Country: standardize variants
country_map = {
    "usa": "USA",
    "us": "USA",
    "united states": "USA",
}
df_clean["country"] = df_clean["country"].str.lower().map(
    lambda x: country_map.get(x, x.upper())
)

print("\nNormalized countries:\n", df_clean["country"])

# ── 6. Handling Outliers ──────────────────────────────────────────────────────
# Remove invalid ages
df_clean = df_clean[df_clean["age"] >= 0]
df_clean = df_clean[df_clean["age"] <= 120]

# Z-score method (remove data points more than 3 std from mean)
scores = df_clean["score"]
z_scores = (scores - scores.mean()) / scores.std()
df_clean = df_clean[z_scores.abs() <= 3]

print(f"\nFinal clean dataset shape: {df_clean.shape}")
print(df_clean)

# ── 7. Feature Engineering ───────────────────────────────────────────────────
# Create new features from existing ones

df_clean = df_clean.reset_index(drop=True)

# Bin ages into groups
df_clean["age_group"] = pd.cut(
    df_clean["age"],
    bins=[0, 20, 25, 30, 100],
    labels=["Under 20", "21-25", "26-30", "Over 30"]
)

# Normalize scores to 0-1 range
min_s, max_s = df_clean["score"].min(), df_clean["score"].max()
df_clean["score_normalized"] = (df_clean["score"] - min_s) / (max_s - min_s)

print("\nWith engineered features:\n", df_clean[["name", "age", "age_group", "score", "score_normalized"]])

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. df.isnull().sum() → see missing values per column
# 2. fillna() or dropna() → handle missing values
# 3. drop_duplicates() → remove duplicate rows
# 4. str accessor: df["col"].str.lower(), .str.strip(), .str.replace()
# 5. pd.cut() → bin continuous values into categories
# 6. Normalize/scale features before feeding to ML models
print("\nDone! Move on to 05_pandas_analysis.py")
