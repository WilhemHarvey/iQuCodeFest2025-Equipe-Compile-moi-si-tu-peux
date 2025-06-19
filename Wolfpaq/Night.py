import numpy as np
from qiskit import QuantumCircuit


class Night:
    def __init__(self, active_players, roles, witch_power, couple = None, first_night = False):
        
        self.qc = QuantumCircuit
        self.alive = active_players
        self.roles_list = roles
        self.in_love = couple
        self.night_1 = first_night
        self.endangered_players=[]

    def Witch(self, save_attacked_player = False):

        if save_attacked_player == True and self.witch_power[0] != False :
            self.qc.rx(-np.pi/3, 0)

        elif True:
            pass


        

