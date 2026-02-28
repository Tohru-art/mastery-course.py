"""
LESSON 4: Working with LLM APIs
================================
You'll use LLM APIs constantly in AI110 and in your career.
This lesson covers the Anthropic Claude API (what powers THIS tool).

Install: pip install anthropic openai
Set env var: ANTHROPIC_API_KEY=your-key-here
"""

import os
import json

# ── 1. Basic API Call (Anthropic Claude) ──────────────────────────────────────
"""
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is machine learning in one sentence?"}
    ]
)

print(message.content[0].text)
"""

# ── 2. System Prompts ─────────────────────────────────────────────────────────
"""
A system prompt sets the LLM's behavior and persona.
This is the #1 technique for controlling LLM output.
"""

SYSTEM_PROMPT = """
You are an expert Python tutor for CodePath AI110 students.
- Give concise, accurate explanations
- Always include a code example
- Point out common mistakes
- Use beginner-friendly language
""".strip()

def build_tutor_request(question):
    return {
        "model": "claude-sonnet-4-6",
        "max_tokens": 1024,
        "system": SYSTEM_PROMPT,
        "messages": [
            {"role": "user", "content": question}
        ]
    }

# ── 3. Conversation History ───────────────────────────────────────────────────
"""
LLMs are stateless — you must pass the full conversation every time.
"""

def simple_chat():
    """Simulate a multi-turn conversation."""
    conversation_history = []

    # client = anthropic.Anthropic()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            break

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Send full history each time
        # response = client.messages.create(
        #     model="claude-sonnet-4-6",
        #     max_tokens=1024,
        #     system="You are a helpful AI assistant.",
        #     messages=conversation_history
        # )
        # assistant_message = response.content[0].text

        assistant_message = f"[Demo] Echo: {user_input}"  # placeholder

        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        print(f"AI: {assistant_message}\n")

# ── 4. Structured Output ──────────────────────────────────────────────────────
"""
Getting structured (JSON) output from an LLM is a critical skill.
Tell the model to respond in JSON format.
"""

CLASSIFICATION_PROMPT = """
Classify the following text. Respond ONLY with valid JSON in this exact format:
{
  "label": "positive" | "negative" | "neutral",
  "confidence": 0.0 to 1.0,
  "reasoning": "one sentence explanation"
}

Text: {text}
"""

def classify_text(text):
    """Template for LLM-based text classification."""
    prompt = CLASSIFICATION_PROMPT.format(text=text)

    # With real API:
    # response = client.messages.create(model="claude-sonnet-4-6", ...)
    # raw = response.content[0].text
    # return json.loads(raw)

    # Demo output:
    return {
        "label": "positive",
        "confidence": 0.92,
        "reasoning": "The text expresses enthusiasm and satisfaction."
    }

result = classify_text("I love how Python makes AI so accessible!")
print("Classification result:")
print(json.dumps(result, indent=2))

# ── 5. Prompt Engineering Patterns ───────────────────────────────────────────
"""
KEY PROMPT ENGINEERING TECHNIQUES:

1. ROLE PROMPTING — give the model a persona
   "You are an expert data scientist with 10 years experience..."

2. CHAIN OF THOUGHT — ask the model to reason step-by-step
   "Think step by step. First analyze X, then Y, then conclude Z."

3. FEW-SHOT EXAMPLES — show examples of what you want
   "Here are examples of good responses:
    Input: ... Output: ...
    Input: ... Output: ..."

4. OUTPUT FORMAT — specify exactly what you want
   "Respond ONLY with valid JSON. No explanation."

5. CONSTRAINTS — tell the model what NOT to do
   "Do not include code. Limit response to 100 words."

6. SELF-CONSISTENCY — ask for multiple answers and pick the best
   "Generate 3 different approaches and recommend the best one."
"""

# ── 6. Evaluating AI-Generated Code (CodePath AI110 objective) ───────────────
"""
When an LLM generates code for you, always:

1. READ IT before running — never blindly execute LLM output
2. UNDERSTAND it — if you can't explain it, you shouldn't use it
3. TEST it — write tests or run with edge cases
4. VERIFY the logic — is the algorithm correct?
5. CHECK for security issues — SQL injection, file traversal, etc.
6. BENCHMARK it — is it efficient?

RED FLAGS in AI-generated code:
- Uses eval() or exec()
- Hardcoded credentials
- No error handling
- Inefficient O(n²) when O(n) is possible
- Overcomplicated solution to a simple problem
"""

print("Lesson 4 complete!")
print("\nNext: Lesson 5 — Prompt Engineering (deep dive)")
