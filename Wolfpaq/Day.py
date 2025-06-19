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

# Simulators of existing quantum computers
from qiskit_ibm_runtime.fake_provider import FakeNairobiV2  # , FakeQuebec

# Visualization of probablity distributions
from qiskit.visualization import plot_histogram


from utils import run_circuit


class Day:
    def __init__(
        self,
        night_circuit: QuantumCircuit,
        endangered_players: list,
        roles: list,
        couple: None,
    ):
        self.night_circuit = night_circuit
        self.roles = roles
        self.endangered_players = endangered_players
        self.couple = couple

    def night_measures(self):
        simulator = AerSimulator()

        qc = transpile(self.night_circuit, simulator)

        result = simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        res_bit_string = counts.keys()[0]

        killed_players = []
        for player, faith in zip(res_bit_string, endangered_players):
            if faith == "1":
                killed_players.append(player)
                self.roles[player] = None

        return killed_players, self.roles

    def hunter(self, player_to_kill: int):
        simulator = AerSimulator()

        qc = QuantumCircuit(1)
        qc.rx(2 * np.arcsin(np.sqrt(0.9)), 0)

        if couple is not None:
            if player_to_kill in couple:
                new_qc = QuantumCircuit(2)
                new_qc.append(qc, [0])
                new_qc.h(0)
                new_qc.cx(0, 1)
                qc = new_qc

        qc = transpile(self.night_circuit, simulator)

        result = simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        res_bit_string = counts.keys()[0]

        killed_players = []

        for player, faith in zip(res_bit_string, endangered_players):
            if faith == "1":
                killed_players.append(player)
                self.roles[player] = None

        return killed_players, self.roles




    def vote(ballot: int):

        circuit = QuantumCircuit(1)

        theta = np.pi*2/3
        circuit.rx(theta)

        result_bit = run_circuit(circuit)