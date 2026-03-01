"""
LESSON 1: Variables, Types & Type Casting
==========================================
Run this file: python lessons/01_variables_types.py
"""

# ── 1. Variables ──────────────────────────────────────────────────────────────
# A variable is just a label pointing to a value in memory.

name = "Alex"           # str
age = 21                # int
gpa = 3.85              # float
is_enrolled = True      # bool
score = None            # NoneType (represents "no value")

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)
print("Score:", score)









# ── 2. Checking Types ─────────────────────────────────────────────────────────
print("\n-- Types --")
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(gpa))         # <class 'float'>
print(type(is_enrolled)) # <class 'bool'>

# ── 3. Type Casting ───────────────────────────────────────────────────────────
# Converting between types

age_as_string = str(age)          # int → str
gpa_as_int = int(gpa)             # float → int (truncates, doesn't round!)
number_string = "42"
number = int(number_string)       # str → int

print("\n-- Type Casting --")
print(age_as_string, type(age_as_string))
print(gpa_as_int, type(gpa_as_int))
print(number, type(number))

# Common mistake: this will CRASH
# bad = int("hello")  # ValueError: invalid literal for int()

# ── 4. Multiple Assignment ────────────────────────────────────────────────────
x = y = z = 0           # all three point to 0
a, b, c = 1, 2, 3       # unpacking — very pythonic!
print("\na, b, c =", a, b, c)

# Swap variables (Python style — no temp variable needed)
a, b = b, a
print("After swap: a, b =", a, b)

# ── 5. Naming Conventions ─────────────────────────────────────────────────────
# Python uses snake_case for variables and functions
# CamelCase is for classes (you'll see this in Module 3)

user_name = "Alex"       # GOOD
# userName = "Alex"      # works but not Pythonic
# USERNAME = "Alex"      # reserved for constants by convention
MAX_RETRIES = 3          # constant — ALL_CAPS by convention

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Python is dynamically typed — you don't declare types
# 2. Use type() to check what type a value is
# 3. Use int(), str(), float() to convert types
# 4. snake_case for variable names
# 5. UPPER_CASE for constants
print("\nDone! Move on to 02_strings.py")
