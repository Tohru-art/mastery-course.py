"""
LESSON 4: Loops
================
Loops let you process datasets, train models, and iterate over results.
Mastering loops is critical for AI/ML work.
"""

# ── 1. for Loop ───────────────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i, end=" ")
print()

# ── 2. while Loop ─────────────────────────────────────────────────────────────
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# ── 3. break, continue, pass ──────────────────────────────────────────────────
# break → exit the loop immediately
for i in range(10):
    if i == 5:
        break           # stops at 5
    print(i, end=" ")
print("← break at 5")

# continue → skip this iteration, go to next
for i in range(10):
    if i % 2 == 0:
        continue        # skip even numbers
    print(i, end=" ")
print("← odd numbers only")

# pass → do nothing (placeholder)
for i in range(3):
    pass  # loop runs but does nothing (useful when writing skeleton code)

# ── 4. enumerate() — Loop with index ─────────────────────────────────────────
# Instead of: for i in range(len(items))
languages = ["Python", "JavaScript", "Go"]
for index, lang in enumerate(languages):
    print(f"{index}: {lang}")

# Start index at 1
for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")

# ── 5. zip() — Loop two lists together ───────────────────────────────────────
names = ["Alice", "Bob", "Carol"]
scores = [92, 87, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ── 6. Looping over Dictionaries ──────────────────────────────────────────────
model_scores = {"GPT-4": 0.95, "Claude": 0.93, "Gemini": 0.91}

for model, score in model_scores.items():
    print(f"{model}: {score:.0%}")

# Keys only
for model in model_scores.keys():
    print(model)

# Values only
for score in model_scores.values():
    print(score)

# ── 7. else on Loops (Python-specific) ────────────────────────────────────────
# The else block runs ONLY if the loop completed without hitting break
for i in range(5):
    if i == 10:      # never true
        break
else:
    print("Loop finished without break")  # this runs

# ── 8. Practical: Processing a dataset ────────────────────────────────────────
temperatures = [72, 85, 91, 68, 77, 95, 103, 88]

total = 0
above_90 = []

for temp in temperatures:
    total += temp
    if temp > 90:
        above_90.append(temp)

average = total / len(temperatures)
print(f"\nAverage: {average:.1f}°F")
print(f"Temps above 90°F: {above_90}")

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. for loops iterate over any iterable (list, dict, string, range...)
# 2. enumerate() gives you index + value — use it instead of range(len())
# 3. zip() lets you loop two lists in sync
# 4. break stops the loop, continue skips to the next iteration
# 5. loop + else is rarely used but good to know
print("\nDone! Move on to 05_functions.py")
