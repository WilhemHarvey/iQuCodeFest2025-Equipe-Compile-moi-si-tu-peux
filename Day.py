import numpy as np
from qiskit import transpile
from utils import run_circuit

# Visualization of the problem graph
import matplotlib.pyplot as plt
import networkx as nx

# Matricial computation and classical optimization
import numpy as np
from scipy.optimize import minimize

# Creation of quantum circuits
from qiskit import QuantumCircuit
from qiskit import QuantumRegister

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

# Visualization of probability distributions
from qiskit.visualization import plot_histogram


from utils import run_circuit


class Day:
    """
    Represents the daytime phase in the game, handling quantum-based decisions
    such as voting, hunter actions, and night measures.

    Attributes:
        night_circuit (QuantumCircuit): Quantum circuit used during the night phase.
        endangered_players (list): List of players endangered during the night.
        roles (list): List of roles assigned to players.
        couple (None or list): Represents the couple in the game, if any.
    """

    def __init__(
        self,
        night_circuit: QuantumCircuit,
        endangered_players: list,
        roles: list,
        couple: None,
    ):
        """
        Initializes the Day class with the given attributes.

        Args:
            night_circuit (QuantumCircuit): Quantum circuit used during the night phase.
            endangered_players (list): List of players endangered during the night.
            roles (list): List of roles assigned to players.
            couple (None or list): Represents the couple in the game, if any.
        """
        self.night_circuit = night_circuit  # Quantum circuit for night phase
        self.roles = roles  # Roles assigned to players
        self.endangered_players = endangered_players  # Players endangered during the night
        self.couple = couple  # Couple in the game, if any

    def night_measures(self):
        """
        Executes the night circuit and determines which players are killed.

        Returns:
            tuple: A list of killed players and the updated roles.
        """
        res_bitstring = run_circuit(self.night_circuit)  # Run the night quantum circuit

        killed_players = []  # List to store killed players
        for faith, player in zip(res_bitstring, self.endangered_players):
            if faith == "1":  # Check if the player is killed
                killed_players.append(player)

        return killed_players, self.roles  # Return killed players and updated roles

    def hunter(self, player_to_kill: int):
        """
        Handles the hunter's action to kill a player, considering the couple's relationship.

        Args:
            player_to_kill (int): The index of the player to kill.

        Returns:
            tuple: A list of killed players and the updated roles.
        """
        players_to_kill = [player_to_kill]  # List of players to kill
        qc = QuantumCircuit(1)  # Create a single-qubit quantum circuit
        qc.rx(2 * np.arcsin(np.sqrt(0.9)), 0)  # Apply rotation to simulate probability

        if self.couple is not None:  # Check if there is a couple
            if player_to_kill in self.couple:  # If the player is part of the couple
                additional_qubit = QuantumRegister(1)  # Add an additional qubit
                qc.add_register(additional_qubit)  # Add the register to the circuit
                new_qc = QuantumCircuit(qc.num_qubits)  # Create a new circuit
                new_qc.append(qc, qc.qubits[:])  # Append the original circuit
                new_qc.cx(0, new_qc.num_qubits - 1)  # Add a controlled-X gate
                qc = new_qc  # Update the circuit

        res_bitstring = run_circuit(qc)  # Run the quantum circuit
        killed_players = []  # List to store killed players

        for faith, player in zip(res_bitstring, players_to_kill):
            if faith == "1":  # Check if the player is killed
                killed_players.append(player)
            self.roles[player] = None  # Update the player's role to None

        return killed_players, self.roles  # Return killed players and updated roles

    def vote(self, ballot: int) -> bool:
        """
        Decides if the voted player dies or not based on a quantum circuit.

        Args:
            ballot (int): The index of the voted player.

        Returns:
            tuple: A boolean indicating if the player was killed and the updated roles.
        """
        circuit = QuantumCircuit(1)  # Create a single-qubit quantum circuit

        theta = np.pi * 2 / 3  # Define the rotation angle
        circuit.rx(theta, 0)  # Apply rotation to simulate probability

        result_bit = run_circuit(circuit)  # Run the quantum circuit

        if result_bit == "1":  # Check if the player is killed
            self.roles[ballot] = None  # Update the player's role to None
            return True, self.roles  # Return True and updated roles

        return False, self.roles  # Return False and updated roles
