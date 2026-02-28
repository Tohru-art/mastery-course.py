"""
MODULE 5 EXERCISES — NumPy & Pandas
=====================================
Run: python exercises/exercises_05.py
Install: pip install numpy pandas
"""

import numpy as np
import pandas as pd


# ══════════════════════════════════════════════════════
# SECTION 1: NumPy
# ══════════════════════════════════════════════════════

def normalize_array(arr):
    """
    Normalize a NumPy array to the range [0, 1] using min-max scaling.
    Formula: (x - min) / (max - min)
    If max == min, return array of zeros.
    """
    # YOUR CODE HERE
    pass


def standardize_array(arr):
    """
    Standardize a NumPy array: subtract mean, divide by std deviation.
    Formula: (x - mean) / std
    If std == 0, return array of zeros.
    """
    # YOUR CODE HERE
    pass


def matrix_stats(matrix):
    """
    Given a 2D NumPy array, return a dict with:
    - "row_means": mean of each row (1D array)
    - "col_means": mean of each column (1D array)
    - "overall_mean": scalar mean of all elements
    - "max_row_index": index of the row with the highest mean
    """
    # YOUR CODE HERE
    pass


def one_hot_encode(labels, num_classes):
    """
    Convert a 1D array of integer class labels to a 2D one-hot matrix.
    Example: one_hot_encode([0, 2, 1], 3) →
             [[1, 0, 0],
              [0, 0, 1],
              [0, 1, 0]]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# SECTION 2: Pandas
# ══════════════════════════════════════════════════════

def load_and_describe(data_dict):
    """
    Create a DataFrame from data_dict and return a summary dict:
    - "shape": tuple (rows, cols)
    - "missing_total": total count of missing values
    - "numeric_means": dict of {col_name: mean} for numeric columns only
    """
    # YOUR CODE HERE
    pass


def clean_dataframe(df):
    """
    Clean the given DataFrame:
    1. Drop duplicate rows.
    2. Fill missing numeric values with the column median.
    3. Fill missing string columns with "Unknown".
    4. Strip whitespace from all string columns.
    5. Lowercase all string columns.
    Return the cleaned DataFrame (don't modify in place).
    """
    # YOUR CODE HERE
    pass


def top_n_by_group(df, group_col, value_col, n=3):
    """
    For each group in group_col, return the top n rows by value_col.
    Return a new DataFrame sorted by group_col then value_col descending.

    Example:
        df = DataFrame with "department" and "salary" columns
        top_n_by_group(df, "department", "salary", 2)
        → top 2 salaries per department
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# CHALLENGE: Build a Mini Data Pipeline
# ══════════════════════════════════════════════════════

def ai_data_pipeline(raw_data):
    """
    Process raw AI training data:

    Input: list of dicts, each with "text" (str), "label" (str), "confidence" (float)

    Steps:
    1. Create a DataFrame.
    2. Drop rows where "text" is null or empty.
    3. Drop rows where confidence < 0.5.
    4. Normalize "confidence" to [0, 1] range.
    5. Add a "text_length" column (number of characters in "text").
    6. Add a "label_encoded" column: encode each unique label as an integer
       (sort labels alphabetically for consistent encoding).
    7. Return the cleaned DataFrame with only:
       ["text", "label", "label_encoded", "confidence", "text_length"]
    """
    # YOUR CODE HERE
    pass


# ══════════════════════════════════════════════════════
# TEST RUNNER
# ══════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    def check(name, result, expected, tol=1e-4):
        nonlocal passed, failed
        if isinstance(expected, np.ndarray):
            ok = np.allclose(result, expected, atol=tol) if result is not None else False
        elif isinstance(expected, float):
            ok = abs(result - expected) < tol if result is not None else False
        else:
            ok = result == expected
        if ok:
            print(f"  PASS  {name}")
            passed += 1
        else:
            print(f"  FAIL  {name}")
            print(f"         Expected: {expected}")
            print(f"         Got:      {result}")
            failed += 1

    print("\n=== MODULE 5 TESTS ===\n")

    # normalize_array
    a = np.array([0.0, 5.0, 10.0])
    check("normalize basic", normalize_array(a), np.array([0.0, 0.5, 1.0]))
    check("normalize same", normalize_array(np.array([3.0, 3.0])), np.array([0.0, 0.0]))

    # standardize_array
    b = np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
    std_result = standardize_array(b)
    check("standardize mean ~0", abs(std_result.mean()) < 1e-10, True)
    check("standardize std ~1", abs(std_result.std() - 1.0) < 1e-10, True)

    # matrix_stats
    m = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    stats = matrix_stats(m)
    if stats:
        check("row_means", stats["row_means"], np.array([2.0, 5.0, 8.0]))
        check("col_means", stats["col_means"], np.array([4.0, 5.0, 6.0]))
        check("overall_mean", stats["overall_mean"], 5.0)
        check("max_row_index", stats["max_row_index"], 2)

    # one_hot_encode
    labels = np.array([0, 2, 1])
    ohe = one_hot_encode(labels, 3)
    expected_ohe = np.array([[1,0,0],[0,0,1],[0,1,0]])
    check("one_hot_encode", ohe, expected_ohe)

    # load_and_describe
    data = {"a": [1, 2, None], "b": [4.0, 5.0, 6.0], "c": ["x", "y", "z"]}
    desc = load_and_describe(data)
    if desc:
        check("shape", desc["shape"], (3, 3))
        check("missing_total", desc["missing_total"], 1)
        check("numeric mean b", abs(desc["numeric_means"].get("b", 0) - 5.0) < 1e-4, True)

    # clean_dataframe
    df_messy = pd.DataFrame({
        "name": ["  Alice  ", "Bob", "Alice  ", None],
        "score": [85.0, None, 85.0, 92.0]
    })
    cleaned = clean_dataframe(df_messy)
    if cleaned is not None:
        check("clean: no duplicates", cleaned.duplicated().sum(), 0)
        check("clean: no nulls", cleaned.isnull().sum().sum(), 0)
        check("clean: lowercase", "alice" in cleaned["name"].values, True)

    # top_n_by_group
    df_g = pd.DataFrame({
        "dept": ["Eng", "Eng", "Eng", "HR", "HR"],
        "salary": [100, 200, 150, 80, 90]
    })
    top = top_n_by_group(df_g, "dept", "salary", 2)
    if top is not None:
        check("top_n count", len(top), 4)
        check("top_n max eng salary", top[top["dept"]=="Eng"]["salary"].max(), 200)

    # ai_data_pipeline
    raw = [
        {"text": "I love python", "label": "positive", "confidence": 0.9},
        {"text": "", "label": "neutral", "confidence": 0.7},
        {"text": "Terrible bug", "label": "negative", "confidence": 0.3},
        {"text": "Great library", "label": "positive", "confidence": 0.85},
        {"text": None, "label": "positive", "confidence": 0.95},
    ]
    result = ai_data_pipeline(raw)
    if result is not None:
        check("pipeline: rows", len(result), 2)
        check("pipeline: cols", set(result.columns), {"text","label","label_encoded","confidence","text_length"})
        check("pipeline: has text_length", "text_length" in result.columns, True)

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed! Commit your work.")


if __name__ == "__main__":
    run_tests()
