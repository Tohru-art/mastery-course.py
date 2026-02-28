# Mini-Project 3: RAG Chatbot

> **Skills used:** LLM APIs, RAG, Prompt Engineering, Guardrails
> **Estimated time:** 4-6 hours
> **Directly aligns with CodePath AI110 objectives**

## Goal
Build a RAG-powered chatbot that answers questions about a topic using your own documents.

## What You'll Build
A Python CLI chatbot that:
1. Loads a set of text documents (your notes, articles, documentation)
2. Embeds them and stores in ChromaDB
3. When asked a question, retrieves relevant docs and answers using Claude/GPT
4. Has input guardrails (length check, injection detection)
5. Has output guardrails (sensitive data redaction)
6. Maintains conversation history for multi-turn chat

## Architecture
```
User Query
    ↓
Input Guardrails
    ↓
Embed Query → ChromaDB → Top-K Docs
    ↓
Build RAG Prompt (system + context + history + query)
    ↓
LLM API (Claude/GPT)
    ↓
Output Guardrails
    ↓
Response to User
```

## Requirements Checklist
- [ ] Documents loaded and indexed (at least 10 docs)
- [ ] Semantic search working (retrieves relevant docs)
- [ ] LLM integration with system prompt
- [ ] Multi-turn conversation history
- [ ] Input guardrails implemented
- [ ] Output guardrails implemented
- [ ] Graceful error handling (API failures, empty results)
- [ ] README with setup instructions

## Bonus Challenges
- [ ] Add a confidence score — if top retrieved doc has low similarity, say "I don't know"
- [ ] Add a "show sources" command to display which docs were used
- [ ] Deploy as a simple Flask web app

## Commit
```bash
git add projects/mini-projects/project3_llm_chatbot/
git commit -m "feat(project3): RAG chatbot with guardrails"
```
