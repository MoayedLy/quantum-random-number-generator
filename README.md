# Quantum Random Number Generator (QRNG)

An implementation of a single-qubit Quantum Random Number Generator utilizing quantum superposition and state measurement in Qiskit.

Developed for **EC580: Special Topics in Digital Systems** at the **University of Tripoli**.

- **Author:** Moayed Jamal Eshbeni
- **Student ID:** 2210249584

---

## Overview

Unlike classical Pseudo-Random Number Generators (PRNGs), which rely on deterministic algorithms and initial seeds, a **Quantum Random Number Generator (QRNG)** derives randomness from the fundamental indeterminism of quantum mechanics (Born's rule).

By preparing a qubit in an equal superposition state using a Hadamard gate ($H$), the outcome of measuring the qubit collapses to either $\vert{}0\rangle$ or $\vert{}1\rangle$ with an exact theoretical probability of $50\%$.

---

## Theory & Mathematical Formulation

### 1. State Initialization
The qubit starts in the ground basis state:
$$\vert{}\psi_0\rangle = \vert{}0\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

### 2. Applying the Hadamard Gate
The Hadamard transformation matrix is:
$$H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$$

Applying $H$ to $\vert{}\psi_0\rangle$:
$$\vert{}\psi_1\rangle = H\vert{}0\rangle = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \frac{\vert{}0\rangle + \vert{}1\rangle}{\sqrt{2}}$$

### 3. Measurement & Collapse
By Born's rule, the probability of measuring each basis state is the squared magnitude of its amplitude:
$$P(0) = \left\vert{}\frac{1}{\sqrt{2}}\right\vert{}^2 = \frac{1}{2} = 50\%$$
$$P(1) = \left\vert{}\frac{1}{\sqrt{2}}\right\vert{}^2 = \frac{1}{2} = 50\%$$

Upon measurement, the qubit's wave function collapses irreversibly into either $0$ or $1$.

---

## Quantum Circuit

```text
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0
```

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/quantum-random-number-generator.git
   cd quantum-random-number-generator
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Run as a Python Script
```bash
python qrng.py
```

### Run via Jupyter Notebook
Launch the notebook environment to view step-by-step visualizations:
```bash
jupyter notebook Quantum_Random_Number_Generator_QRNG.ipynb
```

---

## Experimental Results

- **1024 Shots Test:** Simulated on Qiskit's `AerSimulator`, yielding a balanced distribution:
  - Outcome `'0'`: ~506 (~49.4%)
  - Outcome `'1'`: ~518 (~50.6%)
- **8-Bit Integer Generation:** By chaining 8 independent single-qubit circuits with single-shot measurements, an unbiased byte is produced (e.g., `11011110`$_2$ = `222`$_{10}$).

---

## Project Artifacts

- **Presentation:** [presentation/Quantum_Random_Number_Generator.pptx](presentation/)
- **Notebook:** [Quantum_Random_Number_Generator_QRNG.ipynb](Quantum_Random_Number_Generator_QRNG.ipynb)
- **Hand Calculations:** Available in [`docs/hand_calculation.jpg`](docs/)