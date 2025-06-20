import numpy as np
from qiskit import QuantumCircuit, QuantumRegister


class Night:
    """
    Represents the nighttime phase in the game, handling quantum-based actions
    such as attacks, healing, role uncovering, and other special abilities.

    Attributes:
        roles_list (list): List of roles assigned to players.
        witch_ability (list): List indicating the witch's abilities (heal and attack).
        in_love (None or list): Represents the couple in the game, if any.
        lover_in_danger (None or int): Index of the lover in danger, if applicable.
        big_attack (float): Quantum rotation angle for a strong attack.
        small_attack (float): Quantum rotation angle for a weak attack.
        heal (float): Quantum rotation angle for healing.
    """

    def __init__(self, roles, witch_power, couple=None):
        """
        Initializes the Night class with the given attributes.

        Args:
            roles (list): List of roles assigned to players.
            witch_power (list): List indicating the witch's abilities (heal and attack).
            couple (None or list): Represents the couple in the game, if any.
        """
        self.qc = QuantumCircuit(1)  # Initialize a single-qubit quantum circuit
        self.roles_list = roles  # List of roles assigned to players
        self.endangered_players = []  # List of players endangered during the night
        self.in_love = couple  # Couple in the game, if any
        self.lover_in_danger = None  # Index of the lover in danger, if applicable
        self.witch_ability = witch_power  # Witch's abilities (heal and attack)
        self.big_attack = 2 * np.pi / 3  # Rotation angle for a strong attack
        self.small_attack = np.pi / 3  # Rotation angle for a weak attack
        self.heal = -np.pi / 3  # Rotation angle for healing

    def Werewolf(self, attack_player_index):
        """
        Handles the werewolf's attack on a player.

        Args:
            attack_player_index (int): Index of the player to attack.

        Raises:
            ValueError: If trying to attack a dead player.
        """
        if self.roles_list[attack_player_index] is None:  # Check if the player is already dead
            raise ValueError("Trying to kill a dead player")

        self.qc.rx(self.big_attack, 0)  # Apply a strong attack rotation
        self.endangered_players.append(attack_player_index)  # Add the player to endangered list

        if attack_player_index in self.in_love:  # Check if the player is part of the couple
            self.lover_in_danger = attack_player_index  # Mark the lover as endangered

        return

    def Witch(self, attack_player_index=None, save_attacked_player=False):
        """
        Handles the witch's actions, either healing or attacking a player.

        Args:
            attack_player_index (int, optional): Index of the player to attack.
            save_attacked_player (bool, optional): Whether to heal the attacked player.

        Raises:
            ValueError: If trying to attack or heal a dead player.
        """
        if save_attacked_player and self.witch_ability[0]:  # Check if healing is possible
            self.qc.rx(self.heal, 0)  # Apply healing rotation
            self.witch_ability[0] = False  # Disable healing ability

        elif attack_player_index is not None and self.witch_ability[1]:  # Check if attacking is possible
            if self.roles_list[attack_player_index] is None:  # Check if the player is already dead
                raise ValueError("Trying to kill a dead player")

            if attack_player_index not in self.endangered_players:  # Check if the player is not already endangered
                if attack_player_index in self.in_love and self.lover_in_danger is not None:  # Handle couple logic
                    lover_index = [player for player in self.in_love if player != attack_player_index][0]
                    attack_qc.rx(self.small_attack / 3, lover_index)  # Apply weak attack to lover
                else:
                    additional_qubit = QuantumRegister(1)  # Add an additional qubit
                    self.qc.add_register(additional_qubit)  # Add the register to the circuit
                    attack_qc = QuantumCircuit(2)  # Create a two-qubit circuit
                    attack_qc.rx(self.small_attack / 3, 1)  # Apply weak attack rotation
                    self.qc.append(attack_qc, [0, 1])  # Append the attack circuit
                    self.endangered_players.append(attack_player_index)  # Add the player to endangered list

            elif attack_player_index in self.endangered_players:  # Handle already endangered player
                self.qc.rx(self.small_attack, 0)  # Apply weak attack rotation

            else:
                raise ValueError("Error with attack_player_index")

            self.witch_ability[1] = False  # Disable attack ability

        return

    def Seer(self, player_index):
        """
        Reveals the role of a player.

        Args:
            player_index (int): Index of the player to uncover.

        Raises:
            ValueError: If trying to uncover the role of a dead player.

        Returns:
            str: The role of the player.
        """
        if self.roles_list[player_index] is None:  # Check if the player is already dead
            raise ValueError("Trying to uncover the role of a dead player")

        return self.roles_list[player_index]  # Return the player's role

    def Thief(self, player_to_steal):
        """
        Handles the thief's action to steal another player's role.

        Args:
            player_to_steal (int): Index of the player whose role is to be stolen.

        Returns:
            list: Updated list of roles.
        """
        stealer = self.roles_list.index("Thief")  # Find the thief's index

        # Handle couple logic for stealing roles
        if stealer in self.in_love and player_to_steal not in self.in_love:
            stealer_index = self.in_love.index(stealer)
            self.in_love[stealer_index] = player_to_steal
        elif player_to_steal in self.in_love and stealer not in self.in_love:
            player_to_steal_index = self.in_love.index(player_to_steal)
            self.in_love[player_to_steal_index] = stealer

        # Handle swapping roles in endangered players
        if stealer in self.endangered_players and player_to_steal in self.endangered_players:
            q_stealer_index = self.endangered_players.index(stealer)
            q_player_to_steal_index = self.endangered_players.index(player_to_steal)
            self.qc.swap(self.endangered_players[q_stealer_index], self.endangered_players[q_player_to_steal_index])
        elif stealer in self.endangered_players:
            q_stealer_index = self.endangered_players.index(stealer)
            self.endangered_players[q_stealer_index] = player_to_steal
        elif player_to_steal in self.endangered_players:
            q_player_to_steal_index = self.endangered_players.index(player_to_steal)
            self.endangered_players[q_player_to_steal_index] = stealer

        # Swap roles in the roles list
        self.roles_list[stealer], self.roles_list[player_to_steal] = (
            self.roles_list[player_to_steal],
            self.roles_list[stealer],
        )
        return self.roles_list

    def Savior(self, player_index):
        """
        Handles the savior's action to cleanse a player.

        Args:
            player_index (int): Index of the player to cleanse.

        Raises:
            ValueError: If trying to cleanse a dead player.
        """
        if self.roles_list[player_index] is None:  # Check if the player is already dead
            raise ValueError("Trying to cleanse a dead player")

        if player_index in self.endangered_players:  # Check if the player is endangered
            position = self.endangered_players.index(player_index)
            self.qc.reset(position)  # Reset the player's quantum state

        return

    def Finish_Night(self):
        """
        Finalizes the night phase, handling couple logic and returning the quantum circuit.

        Returns:
            tuple: The quantum circuit and the list of endangered players.
        """
        num = self.qc.num_qubits  # Get the number of qubits in the circuit

        # Handle couple logic for the first lover
        if self.in_love[0] in self.endangered_players:
            lover_qc = QuantumCircuit(num + 1)  # Create a new circuit with an additional qubit
            lover_qubit_index = self.endangered_players.index(self.in_love[0])
            lover_qc.cx(lover_qubit_index, lover_qc.num_qubits - 1)  # Add a controlled-X gate
            additional_qubits = QuantumRegister(1)  # Add an additional qubit
            self.qc.add_register(additional_qubits)  # Add the register to the circuit
            self.qc.append(lover_qc, self.qc.qubits[:])  # Append the lover circuit
            self.endangered_players.append(self.in_love[1])  # Add the second lover to endangered list

        # Handle couple logic for the second lover
        elif self.in_love[1] in self.endangered_players:
            lover_qc = QuantumCircuit(num + 1)  # Create a new circuit with an additional qubit
            lover_qubit_index = self.endangered_players.index(self.in_love[1])
            lover_qc.cx(lover_qubit_index, lover_qc.num_qubits - 1)  # Add a controlled-X gate
            additional_qubits = QuantumRegister(1)  # Add an additional qubit
            self.qc.add_register(additional_qubits)  # Add the register to the circuit
            self.qc.append(lover_qc, self.qc.qubits[:])  # Append the lover circuit
            self.endangered_players.append(self.in_love[0])  # Add the first lover to endangered list

        return self.qc, self.endangered_players  # Return the quantum circuit and endangered players
