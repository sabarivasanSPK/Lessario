# **Project: Sentiment Analyzer (AI)**

Build an AI model that can read a customer review and tell you if it's **Positive**, **Negative**, or **Neutral**.

---

## **1. Requirements**
- **Text Input:** A piece of text (e.g., "I love Zoho CRM!").
- **Classification:** The model predicts the sentiment.
- **Accuracy:** At least 80% on a test dataset.

---

## **2. Tech Stack**
- **Language:** Python.
- **Libraries:** `scikit-learn` or `NLTK`.
- **Dataset:** Use the "IMDB Movie Reviews" or "Amazon Reviews" dataset.

---

## **3. The AI Workflow**
1. **Preprocessing:** Remove stop words (the, is, and) and convert text to lowercase.
2. **Vectorization:** Convert words into numbers using **TF-IDF** or **CountVectorizer**.
3. **Training:** Use a **Naive Bayes** or **Logistic Regression** model.
4. **Testing:** Check the model with new sentences.

---

## **4. Step-by-Step Build**
1. Load your dataset using `pandas`.
2. Split data into `Training` (80%) and `Testing` (20%).
3. Train the model using the training data.
4. Predict sentiment for a few custom strings.

---

## **🎯 Challenge for You:**
Deploy this model as a **Web API** using Flask or FastAPI so a frontend can use it.
