"""
LESSON 5: Regular Expressions
================================
Regex = pattern matching for strings.
Essential for parsing text data, validating inputs, and cleaning datasets.
"""

import re

# ══════════════════════════════════════════════════════
# REGEX CHEAT SHEET
# ══════════════════════════════════════════════════════
"""
CHARACTERS:
  .       any character (except newline)
  \d      digit [0-9]
  \D      non-digit
  \w      word character [a-zA-Z0-9_]
  \W      non-word character
  \s      whitespace (space, tab, newline)
  \S      non-whitespace

QUANTIFIERS:
  *       0 or more
  +       1 or more
  ?       0 or 1 (optional)
  {n}     exactly n
  {n,m}   between n and m

ANCHORS:
  ^       start of string
  $       end of string
  \b      word boundary

GROUPS:
  (abc)   capture group
  (?:abc) non-capture group
  a|b     a OR b
  [abc]   character class: a, b, or c
  [^abc]  NOT a, b, or c
"""

# ══════════════════════════════════════════════════════
# CORE FUNCTIONS
# ══════════════════════════════════════════════════════

# re.search — find first match anywhere in string
text = "My email is alice@example.com and bob@test.org"
match = re.search(r"[\w.]+@[\w.]+\.\w+", text)
if match:
    print("Found email:", match.group())   # alice@example.com

# re.findall — find ALL matches
emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("All emails:", emails)

# re.match — only matches at the START of string
print(re.match(r"\d+", "123abc"))    # match
print(re.match(r"\d+", "abc123"))    # None

# re.fullmatch — entire string must match
print(re.fullmatch(r"\d+", "123"))   # match
print(re.fullmatch(r"\d+", "123abc")) # None

# re.sub — replace matches
text = "Phone: 555-123-4567, or 555.987.6543"
normalized = re.sub(r"[\-.]", "", text)   # remove dashes and dots
print("Normalized:", normalized)

# Replace with a function
def mask_email(match):
    email = match.group()
    user, domain = email.split("@")
    return f"{user[0]}***@{domain}"

masked = re.sub(r"[\w.]+@[\w.]+\.\w+", mask_email, "Send to alice@example.com")
print("Masked:", masked)

# ══════════════════════════════════════════════════════
# GROUPS — extract specific parts
# ══════════════════════════════════════════════════════
date_text = "Event on 2024-03-15"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
if m:
    print(f"\nFull date: {m.group(0)}")    # 2024-03-15
    print(f"Year: {m.group(1)}")           # 2024
    print(f"Month: {m.group(2)}")          # 03
    print(f"Day: {m.group(3)}")            # 15

# Named groups — much more readable
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date_text)
if m:
    print(f"Year: {m.group('year')}, Month: {m.group('month')}")

# ══════════════════════════════════════════════════════
# COMPILE for reuse (faster when using same pattern many times)
# ══════════════════════════════════════════════════════
email_pattern = re.compile(r"\b[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}\b")
phone_pattern = re.compile(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")

texts = [
    "Contact: john@example.com",
    "Phone: 555-123-4567",
    "Not an email: @broken",
    "Email: mary.smith@company.co.uk"
]

for t in texts:
    if email_pattern.search(t):
        print(f"EMAIL: {email_pattern.search(t).group()}")
    if phone_pattern.search(t):
        print(f"PHONE: {phone_pattern.search(t).group()}")

# ══════════════════════════════════════════════════════
# AI/ML USE CASE: Clean text data
# ══════════════════════════════════════════════════════
def clean_text(text):
    """Prepare text for NLP/LLM input."""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "[URL]", text)         # remove URLs
    text = re.sub(r"@\w+", "[USER]", text)                   # remove @mentions
    text = re.sub(r"#(\w+)", r"\1", text)                    # keep hashtag text
    text = re.sub(r"[^\w\s\[\]]", " ", text)                 # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()                 # normalize whitespace
    return text

raw = "Check out https://example.com! @alice loves #MachineLearning 🤖"
print("\nCleaned:", clean_text(raw))

# ── KEY TAKEAWAYS ─────────────────────────────────────────────────────────────
# 1. re.search: find first match anywhere
# 2. re.findall: find all matches as a list
# 3. re.sub: replace matches
# 4. re.compile: pre-compile pattern for performance
# 5. Use raw strings r"..." to avoid double-escaping backslashes
# 6. Test your regex at regex101.com
print("\nDone! Move on to 06_modules_venv.py")
