# **AI: Neural Networks 101**

Neural Networks are the engine behind modern AI. They are loosely inspired by the human brain.

---

## **1. The Anatomy of a Neuron**
A single "Perceptron" or neuron:
1. **Inputs:** Data coming in.
2. **Weights:** How much importance to give to each input.
3. **Bias:** An offset value.
4. **Activation Function:** Decides if the neuron should "fire" (e.g., ReLU, Sigmoid).

---

## **2. Layers**
- **Input Layer:** Receives the raw data.
- **Hidden Layers:** Where the magic (learning) happens.
- **Output Layer:** Provides the final prediction.

---

## **3. How They Learn: Backpropagation**
1. **Forward Pass:** The model makes a guess.
2. **Loss Function:** We measure how wrong the guess was.
3. **Backward Pass (Backprop):** The model goes backward to adjust weights to reduce the error next time.
4. **Optimizer:** (e.g., Adam or SGD) The math that decides how much to change the weights.

---

## **4. Popular Architectures**
- **CNN (Convolutional):** Best for Images.
- **RNN (Recurrent):** Best for Sequences (Text/Audio).
- **Transformer:** The architecture behind ChatGPT.

---

## **🎯 Exercise for You:**
1. Draw a simple neural network with 3 input neurons, 1 hidden layer with 4 neurons, and 1 output neuron.
2. Explain what happens if we set all weights to zero at the start.
