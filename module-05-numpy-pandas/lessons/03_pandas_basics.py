"""
LESSON 3: Pandas Basics
========================
Pandas = Python Data Analysis Library.
Think of it as a powerful spreadsheet in Python.
In AI: you'll use Pandas to load, explore, and clean every dataset.

Install: pip install pandas
"""

import pandas as pd
import numpy as np

# ── 1. Series — 1D labeled array ──────────────────────────────────────────────
s = pd.Series([85, 92, 78, 95, 88], index=["Alice", "Bob", "Carol", "Dave", "Eve"])
print("Series:\n", s)
print("\nAlice's score:", s["Alice"])
print("Above 90:\n", s[s > 90])

# ── 2. DataFrame — 2D table ───────────────────────────────────────────────────
# Creating from a dict (most common way)
data = {
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "age": [22, 25, 23, 21, 24],
    "score": [85, 92, 78, 95, 88],
    "grade": ["B", "A", "C", "A", "B"],
    "passed": [True, True, True, True, True]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ── 3. Exploring Your Data ────────────────────────────────────────────────────
print("\n-- Info --")
print(df.shape)          # (5, 5) — rows, columns
print(df.columns.tolist())
print(df.dtypes)

print("\n-- First/Last rows --")
print(df.head(3))        # first 3 rows
print(df.tail(2))        # last 2 rows

print("\n-- Describe (statistics) --")
print(df.describe())     # count, mean, std, min, quartiles, max

# ── 4. Selecting Data ─────────────────────────────────────────────────────────
# Single column → Series
print("\nNames column:\n", df["name"])

# Multiple columns → DataFrame
print("\nName + Score:\n", df[["name", "score"]])

# ── 5. Filtering Rows ─────────────────────────────────────────────────────────
# Boolean mask
high_scorers = df[df["score"] >= 90]
print("\nHigh scorers:\n", high_scorers)

# Multiple conditions
young_high = df[(df["age"] < 24) & (df["score"] >= 85)]
print("\nYoung and high scorers:\n", young_high)

# Using .query() — more readable
print("\nQuery syntax:", df.query("score >= 90 and age < 25"))

# ── 6. Adding & Modifying Columns ─────────────────────────────────────────────
df["score_pct"] = df["score"] / 100
df["category"] = df["score"].apply(lambda s: "High" if s >= 90 else "Low")
print("\nWith new columns:\n", df)

# ── 7. Sorting ────────────────────────────────────────────────────────────────
sorted_df = df.sort_values("score", ascending=False)
print("\nSorted by score:\n", sorted_df)

# ── 8. Loading Real Data ──────────────────────────────────────────────────────
# Most common way to load data in AI:
# df = pd.read_csv("data.csv")
# df = pd.read_json("data.json")
# df = pd.read_excel("data.xlsx")

# Save data:
# df.to_csv("output.csv", index=False)

# ── 9. Basic Aggregation ──────────────────────────────────────────────────────
print("\n-- Aggregations --")
print("Mean score:", df["score"].mean())
print("Max score:", df["score"].max())
print("Score by grade:\n", df.groupby("grade")["score"].mean())

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. DataFrame is a table; Series is a column
# 2. df["col"] selects a column; df[["col1","col2"]] selects multiple
# 3. Boolean indexing: df[df["col"] > value]
# 4. .describe() gives instant statistics
# 5. .apply() applies a function to every row/column
print("\nDone! Move on to 04_pandas_cleaning.py")
