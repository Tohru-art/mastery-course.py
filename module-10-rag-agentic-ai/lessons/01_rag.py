"""
LESSON 1: RAG — Retrieval-Augmented Generation
================================================
RAG solves the biggest problem with LLMs: they don't know YOUR data.
Instead of retraining, you retrieve relevant documents and give them
to the LLM as context at query time.

Architecture:
  Documents → Embed → Vector Store
                          ↓
  User Query → Embed → Retrieve similar docs → LLM → Answer

Install: pip install anthropic chromadb sentence-transformers
"""

# ══════════════════════════════════════════════════════
# PART 1: UNDERSTANDING EMBEDDINGS
# ══════════════════════════════════════════════════════
"""
An EMBEDDING converts text into a vector of numbers.
Semantically similar text → vectors that are close together.

Example:
  "I love Python" → [0.2, -0.5, 0.8, ...]  (384 dimensions)
  "Python is great" → [0.21, -0.48, 0.79, ...]  ← very similar!
  "The sky is blue" → [0.9, 0.1, -0.3, ...]  ← very different

This lets us find relevant documents by measuring vector similarity.
"""

import numpy as np

def cosine_similarity(vec_a, vec_b):
    """Measure similarity between two vectors. Returns -1 to 1."""
    dot = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot / (norm_a * norm_b)

# Demo: fake embeddings to show the concept
embedding_python_1 = np.array([0.8, 0.2, 0.1, -0.3])
embedding_python_2 = np.array([0.75, 0.25, 0.12, -0.28])  # similar topic
embedding_sky = np.array([-0.1, 0.9, 0.4, 0.8])           # different topic

print("Similarity: Python vs Python-related:", cosine_similarity(embedding_python_1, embedding_python_2))
print("Similarity: Python vs Sky topic:", cosine_similarity(embedding_python_1, embedding_sky))

# ══════════════════════════════════════════════════════
# PART 2: SIMPLE RAG FROM SCRATCH (no library)
# ══════════════════════════════════════════════════════

class SimpleRAG:
    """
    A minimal RAG system to understand the core concepts.
    Uses random embeddings for demo — in production, use sentence-transformers.
    """

    def __init__(self):
        self.documents = []
        self.embeddings = []

    def _fake_embed(self, text):
        """In real RAG, replace this with: model.encode(text)"""
        np.random.seed(hash(text) % (2**32))
        return np.random.randn(64)

    def add_documents(self, docs):
        """Index documents into the vector store."""
        for doc in docs:
            self.documents.append(doc)
            self.embeddings.append(self._fake_embed(doc))
        print(f"Indexed {len(docs)} documents. Total: {len(self.documents)}")

    def retrieve(self, query, top_k=3):
        """Find the most relevant documents for a query."""
        query_embedding = self._fake_embed(query)
        similarities = [
            cosine_similarity(query_embedding, doc_emb)
            for doc_emb in self.embeddings
        ]
        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [self.documents[i] for i in top_indices]

    def answer(self, query, top_k=3):
        """Retrieve context and build a prompt for an LLM."""
        relevant_docs = self.retrieve(query, top_k)

        # Build the RAG prompt
        context = "\n\n".join(f"[Document {i+1}]: {doc}" for i, doc in enumerate(relevant_docs))

        prompt = f"""Use the following context to answer the question.
If the answer isn't in the context, say "I don't have that information."

Context:
{context}

Question: {query}

Answer:"""
        return prompt, relevant_docs


# Demo
rag = SimpleRAG()
rag.add_documents([
    "Python was created by Guido van Rossum and released in 1991.",
    "Machine learning is a subset of AI that learns from data.",
    "Neural networks are inspired by the human brain's neuron structure.",
    "NumPy provides fast numerical computation for Python.",
    "Pandas is used for data manipulation and analysis.",
    "Transformer architecture uses self-attention mechanisms.",
    "RAG combines retrieval with generation for better LLM responses.",
    "Fine-tuning adapts a pre-trained model to a specific task.",
])

query = "What is NumPy used for?"
prompt, docs = rag.answer(query)
print(f"\nQuery: {query}")
print(f"Retrieved docs: {docs}")
print(f"\nPrompt that would be sent to LLM:\n{prompt}")

# ══════════════════════════════════════════════════════
# PART 3: PRODUCTION RAG WITH CHROMADB
# ══════════════════════════════════════════════════════
"""
Real production RAG uses:
- sentence-transformers for high-quality embeddings
- ChromaDB or Pinecone as a vector database
- chunking strategy for long documents

# pip install chromadb sentence-transformers
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize
chroma_client = chromadb.Client()
collection = chroma_client.create_collection("my_knowledge_base")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")  # fast, good quality

# Index documents
documents = ["doc 1 text", "doc 2 text", ...]
embeddings = embed_model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

# Query
query = "your question here"
query_embedding = embed_model.encode([query]).tolist()
results = collection.query(query_embeddings=query_embedding, n_results=3)

# Build prompt and call LLM
context = "\\n".join(results["documents"][0])
# ... send to Anthropic/OpenAI API
"""

# ══════════════════════════════════════════════════════
# PART 4: KEY CONCEPTS IN RAG
# ══════════════════════════════════════════════════════
"""
CHUNKING STRATEGY:
- Split long documents into chunks (usually 256-512 tokens)
- Overlap chunks slightly (e.g., 50 tokens) to avoid cutting context

RETRIEVAL QUALITY:
- Test with questions you know the answers to
- Check if the right documents are being retrieved

PROMPT DESIGN:
- Tell the model to only use the provided context
- Tell it to say "I don't know" if context is insufficient
- This prevents hallucination

EVALUATION:
- Faithfulness: is the answer supported by the retrieved docs?
- Relevance: are the right docs being retrieved?
- Answer quality: is the final answer correct?
"""

print("\nDone! Move on to 02_agentic_workflows.py")
