# **Phase 8: AI Engineering - Generative AI & LLMs**

- 🤖 [LLM & Prompt Engineering Deep Dive](./GenAI/LLM_Prompt_Engineering.md)

Generative AI is changing how we build software. This phase covers Large Language Models (LLMs) and how to integrate them into applications.

---

## **1. Understanding LLMs**

- **Transformers:** The architecture behind GPT, BERT, and Llama.
- **Tokens & Context Window:** How models read and remember text.
- **Hallucinations:** Why models sometimes lie and how to prevent it.

---

## **2. Prompt Engineering**

Being an AI Engineer means knowing how to talk to the model.
- **Zero-shot / Few-shot Prompting:** Giving examples to the model.
- **Chain of Thought:** Asking the model to "think step-by-step."
- **System Prompts:** Setting the personality and constraints of the AI.

---

## **3. RAG (Retrieval-Augmented Generation)**

LLMs are only as good as the data they have. RAG allows you to connect an LLM to your own data (like Zoho's help documents).
- **Embeddings:** Converting text into numbers.
- **Vector Databases:** Storing and searching those numbers (e.g., Pinecone, Milvus, or ChromaDB).
- **Similarity Search:** Finding the right context to feed the LLM.

---

## **4. Agents and Tools**

AI is more than just a chatbot. It can **act**.
- **Function Calling:** Allowing the AI to call your code (e.g., "AI, book a meeting for tomorrow").
- **LangChain / LlamaIndex:** Frameworks for building AI agents.

---

## **5. Ethical AI**
- Bias and Fairness.
- Data Privacy (Crucial for Zoho as they take privacy very seriously).
- Transparency.

---

## **🎯 Exercise for You:**
Build a **Document Chatbot** using RAG.
1. Take a PDF file.
2. Split it into chunks and store them in a vector database.
3. When a user asks a question, retrieve the relevant chunks and use an LLM (like GPT-4 or Llama 3) to answer.

[Back to Master Index ->](../../Zoho%20Software%20Engineer%20Preparation%20Roadmap.md)
