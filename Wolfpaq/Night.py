import numpy as np
from qiskit import QuantumCircuit


class Night:

    def __init__(self, roles, witch_power, couple = None):
        
        self.qc = QuantumCircuit()

        self.roles_list = roles
        self.endangered_players = []

        self.in_love = couple
        self.lover_in_danger = None

        self.witch_ability = witch_power

        self.big_attack = 2 * np.pi / 3
        self.small_attack = np.pi / 3
        self.heal = -np.pi / 3

    def cupid(self, players_to_marry):

        self.in_love = players_to_marry

        return


    def Werewolf(self, attack_player_index):

        if self.roles_list[attack_player_index] == None:
            raise ValueError("Trying to kill a dead player")

        self.qc.rx(self.big_attack, 0)

        self.endangered_players.append(attack_player_index)

        if attack_player_index in self.in_love :
            self.lover_in_danger = attack_player_index

        return
    
    def Witch(self, save_attacked_player = False, attack_player_index = None):

        if attack_player not in self.alive:
            raise ValueError("Trying to kill a dead player")

        if save_attacked_player == True and self.witch_ability[0] != False:
            self.qc.rx(self.heal, 0)
            self.witch_ability[0] = False

        elif attack_player_index != None and self.witch_ability[1] != False :
            
            if self.roles_list[attack_player_index] == None :
                raise ValueError("Trying to kill a dead player")
        
            if attack_player_index not in self.endangered_players :
                if attack_player_index in self.in_love and self.couple_in_danger != None :
                    lover_index = [player for player in self.in_love if player != attack_player_index][0]
                    attack_qc.rx(self.small_attack/3, lover_index)
                else :
                    attack_qc = QuantumCircuit(2)
                    attack_qc.rx(self.small_attack/3, 1)
                    self.qc.append(attack_qc, [0,1])
                    self.endangered_players.append(attack_player_index)

            elif attack_player_index in self.endangered_players:
                self.qc.rx(self.small_attack, 0)

            else:
                raise ValueError("error with attack_player_index")

        return

    def Clairvoyante(self, player_index):
        if self.roles_list[player_index] == None:
            raise ValueError("Trying to uncover the role of a dead player")

        return self.roles_list[player_index]

    def thief(self, player_to_steal):
        stealer = np.argwhere(self.roles == "thief")[0][0]
        if stealer in self.couple and player_to_steal not in self.couple:
            self.couple[np.argwhere(self.couple == stealer)[0][0]] = player_to_steal
        elif player_to_steal in self.couple and stealer not in self.couple:
            self.couple[np.argwhere(self.couple == player_to_steal)[0][0]] = stealer

        if (
            stealer in self.endangered_players
            and player_to_steal in self.endangered_players
        ):
            q_stealer = np.argwhere(self.endangered_players == stealer)[0][0]
            q_player_to_steal = np.argwhere(self.endangered_players == player_to_steal)[
                0
            ][0]

            self.qc.swap(q_stealer, q_player_to_steal)

        elif stealer in self.endangered_players:
            q_stealer = np.argwhere(self.endangered_players == stealer)[0][0]
            self.endangered_players[q_stealer] = player_to_steal
        elif player_to_steal in self.endangered_players:
            q_player_to_steal = np.argwhere(self.endangered_players == stealer)[0][0]
            self.endangered_players[q_player_to_steal] = stealer

        self.roles[stealer], self.roles[player_to_steal] = (
            self.roles[player_to_steal],
            self.roles[stealer],
        )
        return self.roles

    def Savior(self, player_index):

        if self.roles_list[player_index] == None:
            raise ValueError("Trying to cleanse a dead player")

        if player_index in self.endangered_players:
            self.qc.reset(player_index)

        return
    
    def Finish_Night(self):
        
        for player in self.in_love :
            if player in self.endangered_players :
                lover_qc = QuantumCircuit(3)
                self.qc.append(lover_qc, [0,1,2])
                self.qc.cx(0,1)
                self.endangered_players.append(self.lover_in_danger)

        return self.qc

    
   