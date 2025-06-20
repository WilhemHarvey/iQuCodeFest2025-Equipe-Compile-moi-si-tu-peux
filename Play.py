import random

from Day import *
from Night import *

# TODO: handles the exception raised, the program must not stop but just start over
# exactly at the same state as before the exception was raised


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
        self.witch_power = [True, True]  # [can_heal, can_kill]

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
            name = input(f"Player {i + 1}: ").strip()
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
            print("Current players and their roles:")
            for player, role in self.active_players.items():
                print(f"{player}: {self.active_player_roles[role]}")

            # Night phase
            self.night_phase()

            # Day phase
            self.day_phase()

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
        print("\nThe village falls asleep...")

        # Create a Night instance
        night = Night(
            self.active_players, self.active_player_roles, self.witch_power, self.couple
        )

        # Cupidon if first night only
        if self.tour_count == 1:
            if "Cupid" in self.active_player_roles:
                print("\nCupid wakes up...")

        # Role-specific actions during the night
        if "Seer" in self.active_player_roles:
            print("\nThe Seer wakes up...")
            player_name = str(
                input("Which player role do you want to see? (Enter player name): ")
            )
            role = night.Clairvoyante(self.name2index(player_name))
            print(f"\nThe role of {player_name} is: {role}")

        if "Werewolf" in self.active_player_roles:
            print("\nThe Werewolves wake up...")

        if "Witch" in self.active_player_roles:
            print("\nThe Witch wakes up...")

        if "Savior" in self.active_player_roles:
            print("\nThe Savior wakes up...")

        if "Thief" in self.active_player_roles:
            print("\nThe Thief wakes up...")

        # end of the phase night
        print("\nThe night is over.")

    def day_phase(self):
        """
        Handles the day phase of the game, including voting and player actions.
        """
        print("\nThe village wakes up...")

        # Voting phase
        votes = {}
        player_name = str(
            input("Game master, who does the village vote for? (Enter player name): ")
        )
        player_index = self.name2index(player_name)
        # TODO ELIMATE

        # Determine the player with the most votes
        if votes:
            max_votes = max(votes.values())
            voted_players = [
                player for player, count in votes.items() if count == max_votes
            ]

            if len(voted_players) == 1:
                killed_player = voted_players[0]
                print(f"{killed_player} has been voted out!")
                del self.players[killed_player]
            else:
                print("No clear decision was made, no one is voted out.")
        else:
            print("No votes were cast.")

    def name2index(self, name: str) -> int:
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
    # print("\nAssigned Players and Roles:")
    # for player, role in play.players.items():
    #     print(f"{player}: {play.player_roles[role]}")
