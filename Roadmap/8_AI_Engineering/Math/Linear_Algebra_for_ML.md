# **AI: Linear Algebra for Machine Learning**

Machine learning models see the world as a giant collection of numbers arranged in patterns. Linear Algebra is the language used to describe those patterns.

---

## **1. The Hierarchy of Data**
1. **Scalar:** A single number. `x = 5`
2. **Vector:** A 1D array of numbers. `v = [1, 2, 3]` (e.g., coordinates of a point).
3. **Matrix:** A 2D array of numbers. (e.g., a grayscale image).
4. **Tensor:** A multi-dimensional array (3D and beyond). (e.g., a color image or a video).

---

## **2. Core Operations**

### **Matrix Multiplication**
The most important operation in Deep Learning. It’s how weights are applied to inputs.
- **Rule:** Columns of A must match Rows of B.

### **Transpose**
Flipping a matrix over its diagonal. Useful for aligning data shapes.

---

## **3. Why it matters for Zoho?**
When Zoho's **Zia** processes a customer's voice, it converts that audio into a series of numbers (Vectors/Tensors). To analyze those numbers, the system performs millions of matrix operations per second.

---

## **🎯 Exercise for You:**
1. Using **NumPy**, create two 3x3 matrices and multiply them.
2. Find the **Dot Product** of two vectors. What does the result represent?
