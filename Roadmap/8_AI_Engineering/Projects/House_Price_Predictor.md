# **Project: House Price Predictor (AI)**

Learn the basics of **Regression** by predicting a continuous value (price) based on features like area, bedrooms, and location.

---

## **1. Requirements**
- **Dataset:** Use the "Boston Housing" or "Ames Housing" dataset from Kaggle/Scikit-learn.
- **Features:** Number of rooms, age of the house, distance to city center, etc.
- **Model:** Linear Regression or Random Forest Regressor.

---

## **2. Tech Stack**
- **Language:** Python.
- **Libraries:** `pandas`, `scikit-learn`, `numpy`.

---

## **3. Key Concept: Feature Engineering**
Data is rarely perfect. You must:
- **Handle Missing Values:** Fill in or delete rows with empty data.
- **Correlation:** Find out which features actually impact the price (e.g., bedrooms matter more than the color of the door).
- **Scaling:** Normalize numbers so the model doesn't get confused by different units.

---

## **4. Step-by-Step Build**
1. **Exploratory Data Analysis (EDA):** Plot the data using `matplotlib`.
2. **Train/Test Split:** Keep some data hidden to test the model later.
3. **Training:** Fit the model to the training data.
4. **Evaluation:** Calculate the **MAE** (Mean Absolute Error).

---

## **🎯 Challenge for You:**
Try using a more advanced model like **XGBoost** or **Gradient Boosting** to see if you can lower the error rate.
