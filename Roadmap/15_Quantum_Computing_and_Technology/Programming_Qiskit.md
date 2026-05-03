# **Phase 15: Quantum - Programming with Qiskit**

You can actually run code on a real Quantum Computer today using **IBM Quantum** and the **Qiskit** library.

---

## **1. What is Qiskit?**
Qiskit is an open-source SDK (Software Development Kit) for working with quantum computers at the level of pulses, circuits, and application modules.

---

## **2. A Simple Quantum Circuit**
In Qiskit, you build a circuit by adding gates to qubits.

```python
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

# Create a circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard Gate (Puts the qubit in Superposition)
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Run the simulation
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print(counts) # Should be ~500 for '0' and ~500 for '1'
```

---

## **3. The "Hello World" of Quantum (Bell State)**
A Bell State is the simplest example of **Entanglement**.
1. Put Qubit A in Superposition (H gate).
2. Connect Qubit A to Qubit B (CNOT gate).
3. Now, whatever A becomes, B will also become!

---

## **4. Learning Resources**
- [IBM Quantum Learning](https://learning.quantum.ibm.com/): A free, interactive course.
- [Qiskit Textbook](https://learn.qiskit.org/content/v2/): The "Bible" of quantum programming.

---

## **🎯 Exercise for You:**
1. Install Qiskit: `pip install qiskit`.
2. Run the "Superposition" code above on your laptop.
3. Observe how the results are probabilistic (around 50/50).

---

[Back to Master Index ->](../../Zoho%20Software%20Engineer%20Preparation%20Roadmap.md)
