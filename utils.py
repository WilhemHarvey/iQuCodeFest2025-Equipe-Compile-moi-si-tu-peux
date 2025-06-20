import numpy as np
from qiskit import transpile

# Visualization of the problem graph
import matplotlib.pyplot as plt
import networkx as nx

# Matricial computation and calssical optimization
import numpy as np
from scipy.optimize import minimize

# Creation of quantum circuits
from qiskit import QuantumCircuit

# Structure used to build Hamiltonians
from qiskit.quantum_info import SparsePauliOp

# Method used to create QAOA circuits to optimize
from qiskit.circuit.library import QAOAAnsatz

# Tools used for the execution of quantum circuits
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import SamplerV2 as Sampler

# Transpilation of quantum circuits on IBM's simulators and quantum computers
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Quantum computer simulator
from qiskit_aer import AerSimulator


def run_circuit(circuit: QuantumCircuit) -> str:
    """
    This util function measure all of the qubits of the given circuit only once,
    and return the bit string containing the result.

    Args:
        circuit (QuantumCircuit): the quantum circuit to measure

    Returns:
        str: the bit string obtained after the measure
    """
    circuit.measure_all()

    simulator = AerSimulator()

    qc = transpile(circuit, simulator)

    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()
    res_bitstring = list(counts.keys())[0]  # Convert dict_keys to a list

    return res_bitstring
