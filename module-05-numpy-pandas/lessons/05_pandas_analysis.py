"""
LESSON 5: Pandas — Groupby, Merge & Analysis
=============================================
GroupBy, merging DataFrames, and pivot tables — the tools for real analysis.
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# ── Build a dataset ───────────────────────────────────
students = pd.DataFrame({
    "student_id": range(1, 11),
    "name": ["Alice","Bob","Carol","Dave","Eve","Frank","Grace","Henry","Iris","Jack"],
    "department": ["CS","Math","CS","AI","Math","AI","CS","Math","AI","CS"],
    "gpa": np.random.uniform(2.5, 4.0, 10).round(2),
    "year": np.random.choice([1,2,3,4], 10),
    "scholarship": np.random.choice([True, False], 10),
})
print("Students:\n", students.head(), "\n")

# ══════════════════════════════════════════════════════
# GROUPBY — split-apply-combine
# ══════════════════════════════════════════════════════
# Split into groups → apply a function → combine results

# Single aggregation
dept_avg = students.groupby("department")["gpa"].mean().round(2)
print("Avg GPA by dept:\n", dept_avg)

# Multiple aggregations
dept_stats = students.groupby("department")["gpa"].agg(["mean", "min", "max", "count"])
print("\nGPA stats by dept:\n", dept_stats.round(2))

# Multiple columns
summary = students.groupby("department").agg(
    avg_gpa=("gpa", "mean"),
    total_students=("student_id", "count"),
    scholarship_count=("scholarship", "sum")
).round(2)
print("\nFull summary:\n", summary)

# Custom aggregation
def gpa_range(x):
    return x.max() - x.min()

custom = students.groupby("department")["gpa"].agg(
    avg="mean",
    spread=gpa_range
).round(2)
print("\nCustom agg:\n", custom)

# ══════════════════════════════════════════════════════
# MERGE / JOIN — combine DataFrames
# ══════════════════════════════════════════════════════
# Like SQL joins

courses = pd.DataFrame({
    "student_id": [1, 1, 2, 3, 4, 5, 6],
    "course": ["ML", "Python", "Stats", "ML", "DL", "Python", "DL"],
    "grade": ["A", "B", "A", "B", "A", "C", "A"]
})

# INNER JOIN — only matching rows
enrolled = students.merge(courses, on="student_id", how="inner")
print("\nInner join shape:", enrolled.shape)
print(enrolled[["name", "course", "grade"]].head())

# LEFT JOIN — all students, even those without courses
all_students = students.merge(courses, on="student_id", how="left")
print("\nLeft join (students without courses have NaN):")
print(all_students[all_students["course"].isna()][["name", "course"]])

# ══════════════════════════════════════════════════════
# PIVOT TABLE
# ══════════════════════════════════════════════════════
pivot = students.pivot_table(
    values="gpa",
    index="department",
    columns="year",
    aggfunc="mean"
).round(2)
print("\nGPA pivot (dept × year):\n", pivot)

# ══════════════════════════════════════════════════════
# APPLY — custom row/column operations
# ══════════════════════════════════════════════════════
def classify_student(row):
    if row["gpa"] >= 3.7:
        return "Honors"
    elif row["gpa"] >= 3.0:
        return "Good Standing"
    else:
        return "Academic Probation"

students["status"] = students.apply(classify_student, axis=1)
print("\nWith status:\n", students[["name", "gpa", "status"]])

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. groupby().agg() is your main tool for summarizing data
# 2. .merge() works like SQL joins — inner, left, right, outer
# 3. .pivot_table() creates cross-tabulations
# 4. .apply(func, axis=1) applies a function to each row
print("\nModule 5 complete! Now do the exercises.")
