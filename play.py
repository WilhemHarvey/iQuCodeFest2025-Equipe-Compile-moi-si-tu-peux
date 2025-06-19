import random
import numpy as np

class Play:

    def __init__(self):

        self.player_names = []
        self.player_count = 0
        self.roles = ['Villager','Werewolf','Cupid', 'Witch','Hunter', 
                      'Seer','Captain', 'Thief', 'Salvater']
        self.role_counts = []
        self.player_roles = []
        self.players = {}
        
        print(f"Please enter the number of players for the role of: ")
        for role in self.roles:
            count = int(input(f"{role}: "))
            if count >= 0:  # Validate for non-negative numbers
                self.role_counts.append(count)
                self.player_count += count
                for i in range(count): 
                    self.player_roles.append(role)
            else: 
                raise ValueError("\nPlease enter a valid non-negative integer number")
    
        # print(self.player_roles)

        print(f"\nPlease enter the names of the {self.player_count} players:")
        for i in range(self.player_count):
            name = input(f"Player {i + 1}: ").strip()
            self.player_names.append(name)


        self.players = self.assign_roles()

    def assign_roles(self) -> dict: 
        """
        Assigns roles to players based on the specified counts.
        Returns a dictionary mapping player names to their assigned roles.
        """

        inds = list(range(self.player_count))
        random.shuffle(inds)
        # print(inds)

        players = {}
        for player_id, role_index in enumerate(inds):
            players[self.player_names[player_id]] = role_index


        return players
    
if __name__ == "__main__":
    play = Play()
    # print("\nAssigned Players and Roles:")
    # for player, role in play.players.items():
    #     print(f"{player}: {play.player_roles[role]}")