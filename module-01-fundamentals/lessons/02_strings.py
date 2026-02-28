"""
LESSON 2: Strings
==================
Strings are everywhere in AI — prompts, labels, text data, API responses.
Master them.
"""

# ── 1. Creating Strings ───────────────────────────────────────────────────────
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""

print(s3)

# ── 2. f-strings (USE THESE — they're the modern way) ────────────────────────
name = "Alex"
score = 95.678
print(f"Name: {name}, Score: {score:.2f}")  # :.2f = 2 decimal places
print(f"2 + 2 = {2 + 2}")                   # expressions work inside {}

# ── 3. String Methods ─────────────────────────────────────────────────────────
text = "  Hello, World!  "

print(text.strip())           # removes leading/trailing whitespace
print(text.lower())           # lowercase
print(text.upper())           # uppercase
print(text.replace("World", "Python"))
print(text.strip().split(", "))   # split into list: ['Hello', 'World!  ']

sentence = "the quick brown fox"
print(sentence.title())       # Title Case
print(sentence.capitalize())  # Capitalize first letter only
print(sentence.count("o"))    # count occurrences of "o"
print(sentence.startswith("the"))  # True
print(sentence.endswith("fox"))    # True

# ── 4. String Indexing & Slicing ──────────────────────────────────────────────
# Strings are sequences — you can index and slice them
word = "Python"
#        P  y  t  h  o  n
# index: 0  1  2  3  4  5
#       -6 -5 -4 -3 -2 -1  (negative indexing from the end)

print(word[0])       # 'P'
print(word[-1])      # 'n'  (last character)
print(word[2:5])     # 'tho'  [start:end] — end is NOT included
print(word[:3])      # 'Pyt'  (from start to index 3)
print(word[3:])      # 'hon'  (from index 3 to end)
print(word[::-1])    # 'nohtyP'  (reverse a string!)

# ── 5. Useful String Operations ───────────────────────────────────────────────
# Check if substring exists
print("Py" in word)        # True
print("Java" not in word)  # True

# String length
print(len(word))           # 6

# Join a list of strings
words = ["AI", "is", "awesome"]
print(" ".join(words))     # "AI is awesome"

# Strip specific characters
messy = "###data###"
print(messy.strip("#"))    # "data"

# Check string content
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True

# ── 6. String Formatting for AI Work ─────────────────────────────────────────
# Building prompts dynamically (you'll use this a LOT in AI work)
user_input = "What is machine learning?"
system_prompt = "You are a helpful AI tutor."

full_prompt = f"""
System: {system_prompt}
User: {user_input}
Assistant:"""

print(full_prompt)

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. Use f-strings for formatting — they're clean and fast
# 2. Strings are immutable (you can't change them in place)
# 3. str.strip(), .lower(), .split(), .join() are your most-used methods
# 4. Slicing [start:end:step] works on all sequences (strings, lists, etc.)
print("\nDone! Move on to 03_conditionals.py")
