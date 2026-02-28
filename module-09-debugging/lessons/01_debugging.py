"""
LESSON 1: Reading Errors & Debugging
=======================================
Every developer spends 50% of their time debugging.
Learn to do it fast and systematically.
"""

# ══════════════════════════════════════════════════════
# PART 1: READING TRACEBACKS
# ══════════════════════════════════════════════════════
"""
A traceback tells you:
  - WHAT went wrong (exception type + message)
  - WHERE it happened (file + line number)
  - HOW you got there (call stack)

Example traceback:
  Traceback (most recent call last):
    File "main.py", line 10, in <module>
      result = process_data(data)       ← how you got here
    File "utils.py", line 25, in process_data
      return items[index]               ← WHERE the error is
  IndexError: list index out of range   ← WHAT the error is

READING STRATEGY:
  1. Read the LAST line first → that's the error
  2. Read the line JUST ABOVE it → that's where the error happened
  3. Trace upward to understand HOW you got there
"""

# ══════════════════════════════════════════════════════
# PART 2: COMMON ERRORS AND HOW TO FIX THEM
# ══════════════════════════════════════════════════════

def demo_common_errors():
    errors_and_fixes = [
        {
            "error": "NameError: name 'x' is not defined",
            "cause": "Using a variable before assigning it, or typo in name",
            "fix": "Check spelling, make sure variable is assigned in the right scope"
        },
        {
            "error": "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
            "cause": "Mixing types: trying to add 5 + '3'",
            "fix": "Use type casting: int('3') or str(5)"
        },
        {
            "error": "AttributeError: 'NoneType' object has no attribute 'split'",
            "cause": "Calling a method on None — function returned None unexpectedly",
            "fix": "Check if value is None before using it: if x is not None: x.split()"
        },
        {
            "error": "KeyError: 'username'",
            "cause": "Accessing a dict key that doesn't exist",
            "fix": "Use .get('username') or check 'username' in d first"
        },
        {
            "error": "IndexError: list index out of range",
            "cause": "Accessing index that doesn't exist",
            "fix": "Check len(list) before indexing, or use negative index carefully"
        },
        {
            "error": "RecursionError: maximum recursion depth exceeded",
            "cause": "Infinite recursion — missing or wrong base case",
            "fix": "Verify your base case is reachable and terminates the recursion"
        },
    ]

    print("=== Common Python Errors ===")
    for item in errors_and_fixes:
        print(f"\n  ERROR: {item['error']}")
        print(f"  CAUSE: {item['cause']}")
        print(f"  FIX:   {item['fix']}")


demo_common_errors()

# ══════════════════════════════════════════════════════
# PART 3: DEBUGGING TECHNIQUES
# ══════════════════════════════════════════════════════

# Technique 1: Print Debugging
def buggy_function(data):
    result = []
    for i, item in enumerate(data):
        print(f"[DEBUG] i={i}, item={item!r}, type={type(item).__name__}")  # debug print
        processed = item.upper()  # will fail if item is not a string
        result.append(processed)
    return result

try:
    buggy_function(["hello", 42, "world"])
except Exception as e:
    print(f"\nCaught: {type(e).__name__}: {e}")

# Technique 2: Using pdb (Python Debugger)
"""
Add this line BEFORE the line you want to inspect:
  import pdb; pdb.set_trace()

Commands in pdb:
  n  → next line
  s  → step into function
  c  → continue to next breakpoint
  p x  → print variable x
  pp x → pretty-print x
  l  → show current code
  q  → quit debugger

Modern Python 3.7+: use breakpoint() instead:
  breakpoint()  ← same as pdb.set_trace()
"""

# Technique 3: Narrowing Down the Problem
def find_bug_example(numbers):
    """
    Strategy: Binary search for the bug.
    Add checkpoints to narrow down where things go wrong.
    """
    print(f"Input: {numbers}")                 # checkpoint 1

    step1 = [x * 2 for x in numbers]
    print(f"After step 1 (double): {step1}")  # checkpoint 2

    step2 = [x for x in step1 if x > 5]
    print(f"After step 2 (filter): {step2}")  # checkpoint 3

    step3 = sum(step2)
    print(f"After step 3 (sum): {step3}")     # checkpoint 4

    return step3

find_bug_example([1, 2, 3, 4, 5])

# Technique 4: Rubber Duck Debugging
"""
Explain your code out loud (to yourself, a rubber duck, or a classmate).
Often, the act of explaining it reveals the bug.
Before asking for help, be able to say:
  "I expected X to happen, but Y happened instead, because..."
"""

# ══════════════════════════════════════════════════════
# PART 4: DEBUGGING AI-GENERATED CODE
# ══════════════════════════════════════════════════════
"""
When debugging code you got from an AI (Claude, ChatGPT, Copilot):

STEP 1: READ IT FULLY before running
  - Do you understand every line?
  - If not, ask the AI to explain it

STEP 2: CHECK for common AI mistakes
  - Data leakage in ML pipelines
  - Off-by-one errors in loops/slices
  - Assumes data is always clean (no NaN handling)
  - Uses deprecated API calls
  - Imports a library that isn't installed

STEP 3: TEST with simple inputs
  - Start with tiny, known inputs where you can predict the output
  - If it fails, you know where to look

STEP 4: VERIFY the output makes sense
  - For ML: is accuracy/loss in a reasonable range?
  - For data: are there the right number of rows/columns?
  - For text: does the output format match what you expected?

STEP 5: CHECK edge cases
  - What happens with empty input?
  - What about None values?
  - What about very large/small numbers?
"""

print("\nDone! Move on to 02_testing.py")
