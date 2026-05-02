# **AI: LLM & Prompt Engineering**

Being an AI Engineer is 50% code and 50% knowing how to communicate with Large Language Models (LLMs).

---

## **1. The Prompt Hierarchy**
1. **Instruction:** What you want the model to do.
2. **Context:** Background info or data the model needs.
3. **Input Data:** The specific piece of data to process.
4. **Output Indicator:** The format you want (JSON, Markdown, etc.).

---

## **2. Prompting Techniques**

### **Zero-Shot Prompting**
Direct instruction without examples.
*"Summarize this email."*

### **Few-Shot Prompting**
Giving 2-3 examples of the desired behavior.
*"Review: This app is great! -> Sentiment: Positive. Review: It crashes constantly. -> Sentiment: Negative. Review: It's okay, nothing special. -> Sentiment:"*

### **Chain-of-Thought (CoT)**
Asking the model to explain its reasoning.
*"Think step-by-step before providing the final answer."*

---

## **3. Temperature & Top-P**
- **Temperature (0.0 to 1.0):** 
    - 0.0: Consistent and predictable (Best for code/facts).
    - 1.0: Creative and random (Best for poems/stories).
- **Top-P:** Limits the vocabulary to a percentage of most likely words.

---

## **4. System Prompts**
Setting the "Personality" or "Role" of the AI.
*"You are a senior security auditor at Zoho. Review the following code for vulnerabilities."*

---

## **🎯 Exercise for You:**
Create a system prompt for a **Zoho Support Bot** that:
1. Always remains polite.
2. If it doesn't know the answer, it refers the user to `support@zoho.com`.
3. Never discusses competitor products.
