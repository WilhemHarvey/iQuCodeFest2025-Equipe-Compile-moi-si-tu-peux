import numpy as np
from qiskit import QuantumCircuit


class Night:
    def __init__(self, active_players, roles, witch_power, couple = None, first_night = False):
        
        self.qc = QuantumCircuit()

        self.alive = active_players
        self.roles_list = roles
        self.endangered_players=[]
        self.night_1 = first_night

        self.in_love = couple
        self.witch_ability = witch_power
        
        self.big_attack = 2*np.pi/3
        self.small_attack = np.pi/3
        self.heal = -np.pi/3

    def Werewolf(self, attack_player = None) :
        
        return
    
    def Witch(self, save_attacked_player = False, attack_player = None, attack_player_index = None):

        if attack_player not in self.alive :
            raise ValueError("Trying to kill a dead player")
        
        if save_attacked_player == True and self.witch_ability[0] != False :
            self.qc.rx(self.heal, 0)
            self.witch_ability[0] = False

        elif attack_player != None and self.witch_ability[1] != False and attack_player_index !=None :

            if attack_player_index not in self.endegered_players :
                attack_qc = QuantumCircuit(2)
                attack_qc.rx(self.small_attack/3, 1)
                self.qc.append(attack_qc, [0,1])
                self.endangered_players.append(attack_player_index)

            elif attack_player_index in self.endegered_players :
                self.qc.rx(self.small_attack, 0)

            else :
                raise ValueError("error with attack_player_index")
                
        return


            