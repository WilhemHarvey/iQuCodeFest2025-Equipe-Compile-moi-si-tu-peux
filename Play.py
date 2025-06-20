import random

from Day import *
from Night import *

# TODO: handles the exception raised, the program must not stop but just start over
# exactly at the same state as before the exception was raised
# TODO: handles all cases where the user does not enter a valid input ! 

class Play:

    def __init__(self):

        # Attributes related to the players and their roles
        self.player_names = []
        self.player_count = 0
        self.ROLES = [
            "Villager",
            "Werewolf",
            "Cupid",
            "Witch",
            "Hunter",
            "Seer",
            "Captain",
            "Thief",
            "Savior",
        ]
        self.role_counts = []
        self.active_player_roles = []
        self.active_players = {}
        self.ind2name = (
            []
        )  # list containing the name of the players, at the index of their role

        # Attributes related to the game state
        self.CONTINUE = True
        self.tour_count = 0
        self.NIGHT = False
        self.DAY = False

        self.couple = None
        self.witch_power = [True, True]  # [can_heal, can_attack]
        self.night_circuit = None
        self.endangered_players = []  
        

        self.N_circuit = None
        self.N_endangered_players = None

        self.N_circuit = None
        self.N_endangered_players = None

        ##### Initialize the game #####
        print(f"Please enter the number of players for the role of: ")
        for role in self.ROLES:
            count = int(input(f"{role}: "))
            if count >= 0:  # Validate for non-negative numbers
                self.role_counts.append(count)
                self.player_count += count
                for i in range(count):
                    self.active_player_roles.append(role)
            else:
                raise ValueError("\nPlease enter a valid non-negative integer number")

        # print(self.active_player_roles)

        print(f"\nPlease enter the names of the {self.player_count} players:")
        for i in range(self.player_count):
            name = str(input(f"Player {i + 1}: ").strip())
            self.player_names.append(name)

        self.active_players, self.ind2name = self.assign_roles()

        print("\nAssigned Players and Roles:")
        for player, role in self.active_players.items():
            print(f"{player}: {self.active_player_roles[role]}")

        ##### Launch the game #####

        while self.CONTINUE:

            # Start a new tour
            self.tour_count += 1
            print(f"\nTour {self.tour_count} begins!")
            print("Active players and their roles:")
            for player, role in self.active_players.items():
                print(f"{player}: {self.active_player_roles[role]}")

            # Night phase
            print("\nThe village falls asleep...")
            # Cupid if first night only
            if self.tour_count ==1:
                if 'Cupid' in self.active_player_roles:
                    print("\nCupid wakes up...\n Which players do you want to marry (enter their names):")
                    player1= str(input("\nPlayer 1:"))
                    player2 = str(input("\nPlayer 2:"))
                    self.couple = [self.name2index(player1), self.name2index(player2)]
            self.night_phase()

            # Day phase
            self.day_phase()

            # After the end of one entire tour, check of the end conditions
            self.CONTINUE = self.check_end_conditions()

    def assign_roles(self):
        """
        Assigns roles to players based on the specified counts.
        Returns a dictionary mapping player names to their assigned roles.
        """

        inds = list(range(self.player_count))
        random.shuffle(inds)
        # print(inds)

        players = {}
        ind2name = [None] * self.player_count
        for player_id, role_index in enumerate(inds):
            players[self.player_names[player_id]] = role_index
            ind2name[role_index] = self.player_names[player_id]

        return players, ind2name

    def night_phase(self):
        """
        Handles the night phase of the game, including player actions and role-specific abilities.
        """

        # Create a Night instance
        night = Night(self.active_player_roles, 
                      self.witch_power, self.couple)

        # Role-specific actions during the night
        if "Seer" in self.active_player_roles:
            print("\nThe Seer wakes up...")
            player_name = str(input("Which player role do you want to see? (Enter player name): "))
            role = night.Clairvoyante(self.name2index(player_name))
            print(f"\nThe role of {player_name} is: {role}")
            print("\nThe Seer goes back to sleep...")


        if "Werewolf" in self.active_player_roles:
            print("\nThe Werewolves wake up...")
            attack_player_index = str(input("Which player do you want to attack? (Enter player name): "))
            night.Werewolf(self.name2index(attack_player_index))
            print("\nThe Werewolves go back to sleep...")
            

        if 'Witch' in self.active_player_roles:
            print("\nThe Witch wakes up...")
            save_attacked_player = bool(input("Do you want to save the attacked player? (True/False): "))
            if save_attacked_player:
                night.Witch(save_attacked_player=True)
            else: 
                print("\nThe Witch can attack another player.")
                attack_player = str(input("Which player do you want to attack? (Enter player name): "))
                night.Witch(save_attacked_player=False, 
                            attack_player=attack_player,
                            attack_player_index=self.name2index(attack_player))
            print("\nThe Witch goes back to sleep...")

        if "Savior" in self.active_player_roles:
            print("\nThe Savior wakes up...")
            player_index = str(input("Which player do you want to save? (Enter player name): "))
            night.Savior(self.name2index(player_index))
            print("\nThe Savior goes back to sleep...")
        
        if "Thief" in self.active_player_roles:
            print("\nThe Thief wakes up...")
            player_index = str(input("Which player do you want to steal? (Enter player name): "))
            self.active_player_roles = night.Thief(self.name2index(player_index))
            print("\nThe Thief goes back to sleep...")

        # end of the phase night
        self.night_circuit, self.endangered_players = night.finish_night()
        print("\nThe night is now over.")
        

    
    def day_phase(self):
        """
        Handles the day phase of the game, including voting and player actions.
        """
        print("\nThe village wakes up...")

        day = Day(self.N_circuit, self.N_endangered_players, self.active_player_roles,self.couple)

        # Voting phase

        votes = {}
        for player in self.players.keys():
            vote = str(input(f"{player}, who do you want to vote for? (Enter player name): ").strip())
            if vote in self.players:
                votes[vote] = votes.get(vote, 0) + 1
            else:
                print(f"{vote} is not a valid player.")

        voted_player_name = str(
            input("Game master, who does the village vote for? (Enter player name): ")
        )
        voted_player_index = self.name2index(voted_player_name)
        voted_player_role = self.active_player_roles[voted_player_index]

        voted_player_is_killed, self.active_player_roles = Day.vote(Day, voted_player_index)

        if voted_player_is_killed == True :
            print(f"\n {voted_player_name} was killed as a result of the vote. His role was {voted_player_role}.")
            if voted_player_role == "Hunter" :
                hunter_victim_name = str(input("Who does the hunter want to kill? (Enter player name): "))
                hunter_victim_index = self.name2index(hunter_victim_name)
                hunter_victim_role = self.roles(hunter_victim_index)
                dead_players, self.roles = Day.hunter(Day,hunter_victim_index)
                if len(dead_players) == 1 :
                    print(f"\n {hunter_victim_name} was killed as a result of the vote. His role was {hunter_victim_role}.")

        voted_player_is_killed, self.active_player_roles = Day.vote(Day, voted_player_index)

        if voted_player_is_killed == True :
            print(f"\n {voted_player_name} was killed as a result of the vote. His role was {voted_player_role}.")
            if voted_player_role == "Hunter" :
                hunter_victim_name = str(input("Who does the hunter want to kill? (Enter player name): "))
                hunter_victim_index = self.name2index(hunter_victim_name)
                hunter_victim_role = self.roles(hunter_victim_index)
                dead_players, self.roles = Day.hunter(Day,hunter_victim_index)
                if len(dead_players) == 1 :
                    print(f"\n {hunter_victim_name} was killed as a result of the vote. His role was {hunter_victim_role}.")

        elif voted_player_is_killed == False :
            print(f"\n {voted_player_name} survived the villagers execution attempt!")


    def check_end_conditions(self) -> bool:
        """
        Checks the end conditions of the game.
        Returns True if the game should continue, False otherwise.
        """
       
        werewolves_count = 0
        villagers_count = 0

        for role in self.active_player_roles:
            if role == "Werewolf":
                werewolves_count += 1
            elif role is None:
                pass
            else: 
                villagers_count += 1
            
        # winning conditions: 
        if werewolves_count == 0:
            print("\nAll the Werewolves have been killed. The villagers have won the game!")
            return False
        elif werewolves_count > villagers_count:
            print("\nThere are now less villagers alive than Werewolves. The werewolves have won the game!")
            return False
        else:
            return True
    
        

    def name2index(self, name:str) -> int:
        """
        Converts a player name to its index in the active players list.
        """
        if name in self.active_players:
            return self.active_players[name]
        else:
            raise ValueError(f"Player {name} not found in active players.")

    def index2name(self, index: int) -> str:
        """
        Converts a player index to its name in the active players list.
        """
        if 0 <= index < self.player_count:
            return self.ind2name[index]
        else:
            raise ValueError(f"Index {index} is out of bounds for active players.")


if __name__ == "__main__":
    play = Play()
    print("\nAssigned Players and Roles:")
    for player, role in play.players.items():
        print(f"{player}: {play.player_roles[role]}")