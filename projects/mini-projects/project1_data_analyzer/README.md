# Mini-Project 1: Data Analyzer

> **Skills used:** Python fundamentals, Pandas, Matplotlib, File I/O
> **Estimated time:** 2-3 hours

## Goal
Build a command-line tool that analyzes a CSV dataset and produces a visual report.

## Requirements
1. Accept a CSV file path as input
2. Show a summary: shape, missing values, data types, basic statistics
3. Generate 3 plots: distribution of a numeric column, correlation heatmap, top categories
4. Save the plots to a `report/` folder
5. Print a written summary to the terminal

## Starter Code

```python
# project1_data_analyzer/main.py
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    """Load CSV and return DataFrame. Handle FileNotFoundError."""
    # YOUR CODE HERE
    pass

def summarize(df):
    """Print a text summary of the dataset."""
    # YOUR CODE HERE
    pass

def plot_distribution(df, column, output_dir):
    """Plot histogram of a numeric column."""
    # YOUR CODE HERE
    pass

def plot_correlation(df, output_dir):
    """Plot correlation heatmap of numeric columns."""
    # YOUR CODE HERE
    pass

def generate_report(filepath, numeric_col=None):
    df = load_data(filepath)
    os.makedirs("report", exist_ok=True)
    summarize(df)
    if numeric_col:
        plot_distribution(df, numeric_col, "report")
    plot_correlation(df, "report")
    print("\nReport saved to report/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file> [numeric_column]")
    else:
        filepath = sys.argv[1]
        col = sys.argv[2] if len(sys.argv) > 2 else None
        generate_report(filepath, col)
```

## Sample Dataset
Use any CSV from [Kaggle](https://www.kaggle.com/datasets) or the UCI ML Repository.
A good starter: [Titanic dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

## Commit
```bash
git add projects/mini-projects/project1_data_analyzer/
git commit -m "feat(project1): complete data analyzer"
```
