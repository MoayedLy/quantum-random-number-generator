"""Quantum Random Number Generator (QRNG)

EC580 Special Topics in Digital Systems
University of Tripoli
Author: Moayed Jamal Eshbeni
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def generate_random_bits(n_bits: int = 8) -> str:
    simulator = AerSimulator()
    bits = ""
    for _ in range(n_bits):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        compiled_qc = transpile(qc, simulator)
        result = simulator.run(compiled_qc, shots=1).result()
        bits += list(result.get_counts().keys())[0]
    return bits

def run_distribution_test(shots: int = 1024):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    print("Circuit Diagram:")
    print(qc.draw())
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    counts = job.result().get_counts()
    
    print(f"\nResults over {shots} shots:", counts)
    plot_histogram(counts)
    plt.savefig("docs/histogram.png")
    print("Histogram saved to docs/histogram.png")

if __name__ == "__main__":
    print("--- Distribution Analysis (1024 Shots) ---")
    run_distribution_test(1024)
    
    print("\n--- 8-Bit Random Number Generation ---")
    random_bits = generate_random_bits(8)
    print("Binary :", random_bits)
    print("Decimal:", int(random_bits, 2))