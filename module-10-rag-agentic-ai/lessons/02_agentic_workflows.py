"""
LESSON 2: Agentic Workflows & Tool Use
========================================
An "agent" is an LLM that can:
1. Decide which tools to use
2. Call tools (search, run code, call APIs)
3. Use the results to keep reasoning
4. Repeat until it reaches a final answer

This is the foundation of systems like Claude Code, Cursor, and AutoGPT.

CodePath AI110: "Explore agentic workflows"
"""

import json
from typing import Any

# ══════════════════════════════════════════════════════
# PART 1: UNDERSTANDING TOOL USE
# ══════════════════════════════════════════════════════
"""
Without tool use:
  User: "What's 15% of $247.50?"
  LLM:  *might hallucinate the answer*

With tool use:
  User: "What's 15% of $247.50?"
  LLM:  "I'll use the calculator tool"
  Tool: calculator(247.50 * 0.15) → 37.125
  LLM:  "15% of $247.50 is $37.13"
"""

# ── Tool Definitions ──────────────────────────────────────────────────────────
# In Anthropic's API, tools are defined as JSON schemas

TOOLS = [
    {
        "name": "calculator",
        "description": "Performs mathematical calculations. Use for any arithmetic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A math expression to evaluate, e.g. '15 * 247.50 / 100'"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "search_knowledge_base",
        "description": "Search the course knowledge base for information on a topic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return",
                    "default": 3
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "run_python",
        "description": "Execute Python code and return the output. Use for calculations or data processing.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Python code to execute"
                }
            },
            "required": ["code"]
        }
    }
]

# ── Tool Implementations ──────────────────────────────────────────────────────

def calculator(expression: str) -> dict:
    """Safe calculator — only allows math expressions."""
    import ast
    import operator

    # Whitelist safe operations
    safe_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
    }

    def eval_expr(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return safe_ops[type(node.op)](eval_expr(node.left), eval_expr(node.right))
        elif isinstance(node, ast.UnaryOp):
            return safe_ops[type(node.op)](eval_expr(node.operand))
        else:
            raise ValueError(f"Unsafe operation: {type(node).__name__}")

    try:
        tree = ast.parse(expression, mode='eval')
        result = eval_expr(tree.body)
        return {"result": result, "expression": expression}
    except Exception as e:
        return {"error": str(e)}


def search_knowledge_base(query: str, top_k: int = 3) -> dict:
    """Demo knowledge base search."""
    kb = {
        "numpy": "NumPy provides fast numerical computation. Use np.array() for arrays.",
        "pandas": "Pandas provides DataFrames for data manipulation. Use pd.read_csv() to load data.",
        "machine learning": "ML models learn patterns from data. Always split data into train/test.",
        "RAG": "RAG = Retrieval Augmented Generation. Combines search with LLM generation.",
        "neural network": "Neural networks have layers of interconnected nodes. Use backpropagation to train.",
    }
    results = [v for k, v in kb.items() if query.lower() in k.lower()][:top_k]
    return {"query": query, "results": results or ["No results found"]}


def run_python(code: str) -> dict:
    """Execute Python code safely (demo — in production use a sandbox)."""
    import io, contextlib
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            # WARNING: In production, NEVER exec() arbitrary code!
            # Use a proper sandbox like E2B, Daytona, or Docker
            exec(code, {"__builtins__": {}})  # minimal, still not fully safe
        return {"output": output.getvalue()}
    except Exception as e:
        return {"error": str(e)}


# ── Tool Router ───────────────────────────────────────────────────────────────

def execute_tool(tool_name: str, tool_input: dict) -> Any:
    """Route tool calls to their implementations."""
    tools = {
        "calculator": calculator,
        "search_knowledge_base": search_knowledge_base,
        "run_python": run_python,
    }
    if tool_name not in tools:
        return {"error": f"Unknown tool: {tool_name}"}
    return tools[tool_name](**tool_input)


# ══════════════════════════════════════════════════════
# PART 2: THE AGENTIC LOOP
# ══════════════════════════════════════════════════════
"""
The agentic loop:
  1. User sends message
  2. LLM decides: answer directly OR use a tool
  3. If tool → call tool, get result, feed back to LLM
  4. Repeat until LLM gives a final answer (no more tool calls)
"""

class SimpleAgent:
    """
    Demonstrates the agentic loop pattern.
    Replace the 'think' method with a real LLM API call.
    """

    def __init__(self, tools):
        self.tools = tools
        self.conversation = []

    def think(self, messages):
        """
        In production, this calls:
          client.messages.create(
              model="claude-sonnet-4-6",
              tools=self.tools,
              messages=messages
          )

        For demo, we simulate tool decisions.
        """
        last_msg = messages[-1]["content"]

        if "calculate" in last_msg.lower() or any(c.isdigit() for c in last_msg):
            return {
                "type": "tool_use",
                "tool": "calculator",
                "input": {"expression": "247.50 * 0.15"}
            }
        elif "numpy" in last_msg.lower() or "pandas" in last_msg.lower():
            return {
                "type": "tool_use",
                "tool": "search_knowledge_base",
                "input": {"query": last_msg}
            }
        else:
            return {
                "type": "final_answer",
                "content": "I can help you with calculations, knowledge lookups, and Python execution."
            }

    def run(self, user_message: str, max_turns: int = 5):
        """Run the agentic loop."""
        print(f"\nUser: {user_message}")
        self.conversation.append({"role": "user", "content": user_message})

        for turn in range(max_turns):
            response = self.think(self.conversation)

            if response["type"] == "final_answer":
                print(f"Agent: {response['content']}")
                return response["content"]

            elif response["type"] == "tool_use":
                tool_name = response["tool"]
                tool_input = response["input"]

                print(f"[Agent using tool: {tool_name}({tool_input})]")
                tool_result = execute_tool(tool_name, tool_input)
                print(f"[Tool result: {tool_result}]")

                # Add tool result to conversation
                self.conversation.append({
                    "role": "tool_result",
                    "tool": tool_name,
                    "result": tool_result
                })

                # Synthesize final answer
                answer = f"Used {tool_name}. Result: {tool_result}"
                print(f"Agent: {answer}")
                return answer

        return "Max turns reached"


# Demo
agent = SimpleAgent(TOOLS)
agent.run("Can you calculate 15% of 247.50?")

# ══════════════════════════════════════════════════════
# PART 3: REAL ANTHROPIC TOOL USE
# ══════════════════════════════════════════════════════
"""
Real implementation with Anthropic API:

import anthropic
client = anthropic.Anthropic()

def run_agent(user_message):
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            tools=TOOLS,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            # No more tool calls — we're done
            return response.content[0].text

        elif response.stop_reason == "tool_use":
            # Process tool calls
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })

            messages.append({"role": "user", "content": tool_results})
"""

print("\nDone! Move on to 03_fine_tuning.py")
