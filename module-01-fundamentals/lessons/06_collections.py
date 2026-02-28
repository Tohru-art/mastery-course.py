"""
LESSON 6: Collections — Lists, Tuples, Sets, Dicts
====================================================
Python's built-in data structures. You'll use these in EVERY program.
In AI/ML: lists hold data, dicts store model results, sets remove duplicates.
"""

# ══════════════════════════════════════════════════════
# LISTS — ordered, mutable, allows duplicates
# ══════════════════════════════════════════════════════
print("── LISTS ──")
scores = [85, 92, 78, 95, 88]

# Access & Slice
print(scores[0])       # 85 (first)
print(scores[-1])      # 88 (last)
print(scores[1:3])     # [92, 78]

# Modify
scores.append(99)          # add to end
scores.insert(0, 100)      # insert at position
scores.remove(78)          # remove first occurrence of 78
popped = scores.pop()      # remove and return last item
print(scores)

# Sort
scores.sort()                        # sorts in place, ascending
scores.sort(reverse=True)            # descending
sorted_copy = sorted(scores)         # returns new sorted list (doesn't modify original)

# Useful methods
print(len(scores))         # length
print(sum(scores))         # sum of all numbers
print(max(scores))         # maximum
print(min(scores))         # minimum
print(scores.count(92))    # how many times 92 appears
print(95 in scores)        # True — check membership

# Copying a list (IMPORTANT — avoid this bug)
original = [1, 2, 3]
wrong_copy = original      # NOT a copy — both point to same list!
right_copy = original.copy()  # actual copy
# or: right_copy = original[:]

# ══════════════════════════════════════════════════════
# TUPLES — ordered, IMMUTABLE, allows duplicates
# ══════════════════════════════════════════════════════
print("\n── TUPLES ──")
# Use tuples for data that shouldn't change (coordinates, RGB colors, etc.)

coordinates = (40.7128, -74.0060)   # NYC lat/lon
rgb_red = (255, 0, 0)

lat, lon = coordinates    # unpacking
print(f"Latitude: {lat}, Longitude: {lon}")

# Tuples can be used as dict keys (lists cannot)
location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

# ══════════════════════════════════════════════════════
# SETS — unordered, mutable, NO duplicates
# ══════════════════════════════════════════════════════
print("\n── SETS ──")
# Sets are great for: removing duplicates, fast membership testing, set math

tags = {"python", "ai", "ml", "python", "ai"}  # duplicates removed
print(tags)  # {'python', 'ai', 'ml'} — order not guaranteed

tags.add("data-science")
tags.discard("ml")      # remove (no error if not found)

# Set operations
ml_skills = {"python", "statistics", "linear-algebra"}
cs_skills = {"python", "algorithms", "data-structures"}

print(ml_skills & cs_skills)   # intersection — shared skills
print(ml_skills | cs_skills)   # union — all skills combined
print(ml_skills - cs_skills)   # difference — ml_skills but not in cs_skills

# Remove duplicates from a list
raw_labels = ["cat", "dog", "cat", "bird", "dog", "cat"]
unique_labels = list(set(raw_labels))
print(unique_labels)

# ══════════════════════════════════════════════════════
# DICTS — key-value pairs, ordered (Python 3.7+), mutable
# ══════════════════════════════════════════════════════
print("\n── DICTS ──")
# Dicts are everywhere in AI — storing model configs, results, mappings

model = {
    "name": "ResNet-50",
    "accuracy": 0.943,
    "parameters": 25_000_000,
    "layers": 50
}

# Access
print(model["name"])                     # KeyError if key doesn't exist
print(model.get("version", "unknown"))   # safe access with default

# Modify
model["accuracy"] = 0.951   # update existing
model["framework"] = "PyTorch"   # add new key

# Delete
del model["layers"]
removed = model.pop("framework")   # remove and return

# Iterate
for key, value in model.items():
    print(f"  {key}: {value}")

# Check key existence
if "name" in model:
    print("Has name field")

# Dict from two lists (very useful!)
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print(combined)  # {'a': 1, 'b': 2, 'c': 3}

# Nested dicts (common for AI model results)
results = {
    "model_1": {"accuracy": 0.92, "f1": 0.91},
    "model_2": {"accuracy": 0.95, "f1": 0.94},
}
print(results["model_2"]["f1"])

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# LIST  → ordered, mutable, allows duplicates — use for sequences of data
# TUPLE → ordered, immutable — use for fixed data, can be dict keys
# SET   → unordered, no duplicates — use for unique values, fast lookup
# DICT  → key-value — use for mapping, configs, storing structured results
print("\nDone! Move on to 07_comprehensions.py")
