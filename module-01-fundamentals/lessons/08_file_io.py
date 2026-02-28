"""
LESSON 8: File I/O
===================
Reading and writing files is essential — AI models load datasets from files,
save results, and log outputs. Master this early.
"""

import os
import json
import csv

# ── 1. Writing a Text File ────────────────────────────────────────────────────
# 'w' = write (creates new file or overwrites existing)
with open("output.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("File written.")

# ── 2. Reading a Text File ────────────────────────────────────────────────────
# Always use 'with' — it automatically closes the file even if an error occurs
with open("output.txt", "r") as f:
    content = f.read()        # reads entire file as one string
print(content)

with open("output.txt", "r") as f:
    lines = f.readlines()     # reads into a list of lines
print(lines)

with open("output.txt", "r") as f:
    for line in f:            # line by line (memory efficient for large files)
        print(line.strip())

# ── 3. Appending to a File ────────────────────────────────────────────────────
# 'a' = append (adds to end without overwriting)
with open("output.txt", "a") as f:
    f.write("Appended line\n")

# ── 4. JSON Files (You'll Use This All the Time) ─────────────────────────────
# JSON is the most common format for AI configs, API responses, datasets

model_config = {
    "name": "my_classifier",
    "learning_rate": 0.001,
    "epochs": 50,
    "layers": [128, 64, 32],
    "dropout": 0.3
}

# Write JSON
with open("model_config.json", "w") as f:
    json.dump(model_config, f, indent=2)   # indent=2 makes it pretty

print("JSON saved.")

# Read JSON
with open("model_config.json", "r") as f:
    loaded_config = json.load(f)

print(loaded_config["learning_rate"])   # 0.001
print(loaded_config["layers"])          # [128, 64, 32]

# ── 5. CSV Files (Data Science Staple) ────────────────────────────────────────
# CSV = Comma-Separated Values — used for datasets

# Write CSV
rows = [
    ["Name", "Score", "Grade"],
    ["Alice", 92, "A"],
    ["Bob", 85, "B"],
    ["Carol", 78, "C"]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open("results.csv", "r") as f:
    reader = csv.DictReader(f)   # each row becomes a dict
    for row in reader:
        print(f"{row['Name']}: {row['Score']}")

# ── 6. Working with File Paths ────────────────────────────────────────────────
# Use os.path for cross-platform path handling
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

file_path = os.path.join(current_dir, "output.txt")
print(f"Full path: {file_path}")

# Check if file exists
if os.path.exists("output.txt"):
    print("File exists!")
    print(f"Size: {os.path.getsize('output.txt')} bytes")

# List files in directory
files = os.listdir(".")
print("Files:", files)

# ── 7. Clean Up ───────────────────────────────────────────────────────────────
# Remove the test files we created
for fname in ["output.txt", "model_config.json", "results.csv"]:
    if os.path.exists(fname):
        os.remove(fname)
print("Cleaned up test files.")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Always use 'with open(...)' — it handles closing automatically
# 2. Modes: 'r'=read, 'w'=write, 'a'=append, 'rb'/'wb' for binary
# 3. json.dump/load for JSON files — very common in AI work
# 4. csv.writer/DictReader for CSV files
# 5. Use os.path.join() for paths — works on Windows AND Mac/Linux
print("\nDone! Move on to 09_error_handling.py")
