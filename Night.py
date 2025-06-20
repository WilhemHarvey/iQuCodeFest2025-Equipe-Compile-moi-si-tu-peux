import numpy as np
from qiskit import QuantumCircuit, QuantumRegister


class Night:

    def __init__(self,roles, witch_power, couple=None):

        self.qc = QuantumCircuit(1)

        self.roles_list = roles
        self.endangered_players = []

        self.in_love = couple
        self.lover_in_danger = None

        self.witch_ability = witch_power

        self.big_attack = 2 * np.pi / 3
        self.small_attack = np.pi / 3
        self.heal = -np.pi / 3

    def Werewolf(self, attack_player_index):

        if self.roles_list[attack_player_index] == None:
            raise ValueError("Trying to kill a dead player")

        self.qc.rx(self.big_attack, 0)

        self.endangered_players.append(attack_player_index)

        if attack_player_index in self.in_love :
            self.lover_in_danger = attack_player_index

        return

    def Witch(
        self, attack_player_index = None, save_attacked_player=False, 
    ):

        if save_attacked_player == True and self.witch_ability[0] != False:
            self.qc.rx(self.heal, 0)
            self.witch_ability[0] = False

        elif attack_player_index != None and self.witch_ability[1] != False :
            
            if self.roles_list[attack_player_index] == None :
                raise ValueError("Trying to kill a dead player")
        
            if attack_player_index not in self.endangered_players :
                if attack_player_index in self.in_love and self.lover_in_danger != None :
                    lover_index = [player for player in self.in_love if player != attack_player_index][0]
                    attack_qc.rx(self.small_attack/3, lover_index)
                else :

                    additional_qubit = QuantumRegister(1)
                    self.qc.add_register(additional_qubit)

                    attack_qc = QuantumCircuit(2)
                    attack_qc.rx(self.small_attack/3, 1)

                    self.qc.append(attack_qc, [0,1])
                    self.endangered_players.append(attack_player_index)

            elif attack_player_index in self.endangered_players:
                self.qc.rx(self.small_attack, 0)

            else:
                raise ValueError("error with attack_player_index")
            
            self.witch_ability[1] = False


        return
    

    def Seer(self, player_index):
        if self.roles_list[player_index] == None:
            raise ValueError("Trying to uncover the role of a dead player")

        return self.roles_list[player_index]

    def Thief(self, player_to_steal):
        stealer = self.roles_list.index("Thief")
        if stealer in self.in_love and player_to_steal not in self.in_love:
            #self.in_love[np.argwhere(self.in_love == stealer)[0][0]] = player_to_steal
            stealer_index = self.in_love.index(stealer)
            self.in_love[stealer_index] = player_to_steal
        elif player_to_steal in self.in_love and stealer not in self.in_love:
            # self.in_love[np.argwhere(self.in_love == player_to_steal)[0][0]] = stealer
            player_to_steal_index = self.in_love.index(player_to_steal)
            self.in_love[player_to_steal_index] = stealer

        if (
            stealer in self.endangered_players
            and player_to_steal in self.endangered_players
        ):
            # q_stealer = np.argwhere(self.endangered_players == stealer)[0][0]
            # q_player_to_steal = np.argwhere(self.endangered_players == player_to_steal)[
            #     0
            # ][0]
            q_stealer_index = self.endangered_players.index(stealer)
            q_stealer = self.endangered_players[q_stealer_index]

            q_player_to_steal_index = self.endangered_players.index(player_to_steal)
            q_player_to_steal = self.endangered_players[q_player_to_steal_index]


            self.qc.swap(q_stealer, q_player_to_steal)

        elif stealer in self.endangered_players:
            q_stealer_index = self.endangered_players.index(stealer)
            # q_stealer = self.endangered_players[q_stealer_index]
            self.endangered_players[q_stealer_index] = player_to_steal

        elif player_to_steal in self.endangered_players:
            q_player_to_steal_index = self.endangered_players.index(player_to_steal)
            # q_player_to_steal = self.endangered_players[q_player_to_steal_index]
            self.endangered_players[q_player_to_steal_index] = stealer

        self.roles_list[stealer], self.roles_list[player_to_steal] = (
            self.roles_list[player_to_steal],
            self.roles_list[stealer],
        )
        return self.roles_list

    def Savior(self, player_index):

        if self.roles_list[player_index] == None:
            raise ValueError("Trying to cleanse a dead player")

        if player_index in self.endangered_players:
            position = self.endangered_players.index(player_index)
            self.qc.reset(position)

        return
    
    def Finish_Night(self):        
        num = self.qc.num_qubits        
        if self.in_love[0] in self.endangered_players:
            lover_qc = QuantumCircuit(num + 1)            
            lover_qubit_index = self.endangered_players.index(self.in_love[0])
            lover_qc.cx(lover_qubit_index, lover_qc.num_qubits - 1)            
            additional_qubits = QuantumRegister(1)
            self.qc.add_register(additional_qubits)            
            self.qc.append(lover_qc, self.qc.qubits[:])            
            self.endangered_players.append(self.lover_in_danger)        
        elif self.in_love[1] in self.endangered_players:
            lover_qc = QuantumCircuit(num+1)
            lover_qubit_index = num+1            
            lover_qubit_index = self.endangered_players.index(self.in_love[1])
            lover_qc.cx(lover_qubit_index, lover_qc.num_qubits - 1)            
            additional_qubits = QuantumRegister(1)
            self.qc.add_register(additional_qubits)            
            self.qc.append(lover_qc, self.qc.qubits[:])            
            self.endangered_players.append(self.lover_in_danger)        
    
        return self.qc, self.endangered_players
