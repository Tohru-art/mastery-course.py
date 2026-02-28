"""
LESSON 6: Modules, Packages & Virtual Environments
====================================================
How to organize code into files, import them, and manage dependencies.
Essential for every real project.
"""

# ══════════════════════════════════════════════════════
# MODULES — a single .py file
# ══════════════════════════════════════════════════════
"""
Any .py file is a module. Import it with:
  import mymodule
  from mymodule import my_function
  from mymodule import my_function as fn   # alias
"""

# Standard library modules you'll use constantly
import os
import sys
import json
import math
import random
import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Union

# ── os and pathlib ────────────────────────────────────
cwd = Path.cwd()
print(f"Current dir: {cwd}")
print(f"Home dir: {Path.home()}")

# Path operations
data_path = Path("data") / "training" / "labels.csv"
print(f"Data path: {data_path}")
print(f"Stem: {data_path.stem}")     # labels
print(f"Suffix: {data_path.suffix}") # .csv
print(f"Parent: {data_path.parent}") # data/training

# ── datetime ──────────────────────────────────────────
now = datetime.datetime.now()
print(f"\nNow: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M')}")

# Parse a date string
d = datetime.datetime.strptime("2024-03-15", "%Y-%m-%d")
print(f"Parsed: {d.date()}")

# ── typing — type hints ───────────────────────────────
def process_batch(
    items: List[str],
    config: Dict[str, float],
    label: Optional[str] = None
) -> Tuple[List[str], int]:
    """Type-annotated function — makes code self-documenting."""
    processed = [item.strip().lower() for item in items if item]
    return processed, len(processed)

# ══════════════════════════════════════════════════════
# PACKAGES — a folder with __init__.py
# ══════════════════════════════════════════════════════
"""
A package is a folder of modules:

my_ai_project/
├── __init__.py        ← makes it a package
├── models/
│   ├── __init__.py
│   ├── classifier.py
│   └── regressor.py
├── data/
│   ├── __init__.py
│   └── loader.py
└── utils/
    ├── __init__.py
    └── metrics.py

Import:
  from my_ai_project.models.classifier import LogisticModel
  from my_ai_project.data.loader import DataLoader
"""

# ══════════════════════════════════════════════════════
# if __name__ == "__main__"
# ══════════════════════════════════════════════════════
"""
This is crucial for writing importable modules:

When you RUN a file directly:    __name__ == "__main__"
When you IMPORT a file:          __name__ == "module_name"

So code inside 'if __name__ == "__main__":' ONLY runs
when you run the file directly — NOT when imported.
"""

def my_useful_function():
    return "I can be imported!"

if __name__ == "__main__":
    print(my_useful_function())   # only runs when you run this file directly

# ══════════════════════════════════════════════════════
# VIRTUAL ENVIRONMENTS
# ══════════════════════════════════════════════════════
"""
A virtual environment = isolated Python installation with its own packages.
WHY: Project A needs numpy 1.20, Project B needs numpy 1.26 — no conflict!

CREATE:
  python -m venv venv

ACTIVATE:
  Windows:    venv\\Scripts\\activate
  Mac/Linux:  source venv/bin/activate

You'll see (venv) in your prompt — you're now isolated.

INSTALL:
  pip install numpy pandas scikit-learn

SAVE dependencies:
  pip freeze > requirements.txt

INSTALL from requirements:
  pip install -r requirements.txt

DEACTIVATE:
  deactivate

NEVER commit your venv/ folder to git!
(it's already in our .gitignore)
"""

print("Module 4 lessons complete! Now do the exercises.")
