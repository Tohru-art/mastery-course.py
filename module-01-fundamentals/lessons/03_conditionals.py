"""
LESSON 3: Conditionals & Boolean Logic
========================================
Control flow is the backbone of every program.
"""

# ── 1. if / elif / else ───────────────────────────────────────────────────────
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# ── 2. Comparison Operators ───────────────────────────────────────────────────
x = 10
print(x == 10)   # equal
print(x != 5)    # not equal
print(x > 5)     # greater than
print(x < 20)    # less than
print(x >= 10)   # greater than or equal
print(x <= 10)   # less than or equal

# ── 3. Boolean Operators ──────────────────────────────────────────────────────
age = 20
has_id = True

# and → both must be True
if age >= 18 and has_id:
    print("Access granted")

# or → at least one must be True
is_admin = False
is_staff = True
if is_admin or is_staff:
    print("Can access dashboard")

# not → flips True/False
is_banned = False
if not is_banned:
    print("User can post")

# ── 4. Truthiness (IMPORTANT for Python) ─────────────────────────────────────
# In Python, these values are "falsy" (treated as False in conditions):
# False, None, 0, 0.0, "", [], {}, set()
# Everything else is "truthy"

name = ""
if name:                     # "" is falsy
    print("Has name")
else:
    print("No name provided")   # this runs

items = [1, 2, 3]
if items:                    # non-empty list is truthy
    print("List has items")

# ── 5. Ternary / Inline if ────────────────────────────────────────────────────
# Python's version of the ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(status)

# ── 6. Chained Comparisons (Python-specific, very clean) ─────────────────────
grade_num = 85
if 80 <= grade_num < 90:     # works! (no need for 'and')
    print("B grade")

# ── 7. None Checks ────────────────────────────────────────────────────────────
result = None
if result is None:           # use 'is' for None, not ==
    print("No result yet")

if result is not None:
    print("Got a result!")

# ── 8. Practical: AI confidence threshold ─────────────────────────────────────
confidence = 0.87

if confidence >= 0.90:
    label = "High confidence"
elif confidence >= 0.70:
    label = "Medium confidence"
else:
    label = "Low confidence — needs review"

print(f"Prediction confidence {confidence:.0%}: {label}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use 'is' / 'is not' for None comparisons
# 2. Python has truthiness — empty things are falsy
# 3. Ternary: value = x if condition else y
# 4. Chained comparisons work: 0 < x < 10
print("\nDone! Move on to 04_loops.py")
