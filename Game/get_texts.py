import pygame


def get_texts():
    text_objects = []
    title_font = pygame.font.Font(None, 100)
    # 0
    text_objects.append(title_font.render("Quantum Werewolf", True, "Red"))

    title_font = pygame.font.Font(None, 60)
    # 1
    text_objects.append(
        title_font.render(
            "Invalid number: must be between 0 and 1, try again",
            True,
            "Red",
        )
    )
    # 2
    text_objects.append(
        title_font.render(
            "Enter the number of villagers. Press enter when done.", True, "Red"
        )
    )
    # 3
    text_objects.append(
        title_font.render(
            "Enter the number of werewolfs. Press enter when done.", True, "Red"
        )
    )
    # 4
    title_font = pygame.font.Font(None, 45)
    text_objects.append(
        title_font.render(
            "Enter the number of Cupids (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 5
    text_objects.append(
        title_font.render(
            "Enter the number of witches (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 6
    text_objects.append(
        title_font.render(
            "Enter the number of hunters (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 7
    text_objects.append(
        title_font.render(
            "Enter the number of seers (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 8
    text_objects.append(
        title_font.render(
            "Enter the number of captains (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 9
    text_objects.append(
        title_font.render(
            "Enter the number of thieves (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 10
    text_objects.append(
        title_font.render(
            "Enter the number of saviors (must be between 0 and 1). Press enter when done.",
            True,
            "Red",
        )
    )
    # 11
    text_objects.append(
        title_font.render(
            "Enter the name of the players: write one player's name, then press enter.",
            True,
            "Red",
        )
    )
    # 12
    text_objects.append(
        title_font.render(
            "There can not be empty or duplicate names. Try again",
            True,
            "Red",
        )
    )
    # 13
    text_objects.append(
        title_font.render(
            "Distribute the following card to this player. Press enter when done",
            True,
            "Red",
        )
    )
    # 14
    text_objects.append(
        title_font.render(
            "The name is not valid or the player is dead",
            True,
            "Yellow",
        )
    )
    # 15
    title_font = pygame.font.Font(None, 70)
    text_objects.append(
        title_font.render(
            "The village has fallen asleep: Night phase",
            True,
            "Yellow",
        )
    )
    input_font = pygame.font.Font(None, 60)
    # 16
    text_objects.append(
        input_font.render(
            "Cupid wakes up! Enter the name of the first lover:",
            True,
            "Yellow",
        )
    )
    # 17
    text_objects.append(
        input_font.render(
            "Cupid wakes up! Enter the name of the second lover:",
            True,
            "Yellow",
        )
    )
    # 18
    input_font_seer = input_font = pygame.font.Font(None, 55)
    text_objects.append(
        input_font_seer.render(
            "The seer wakes up! Enter the name of the player to see the role",
            True,
            "Yellow",
        )
    )

    # 19
    input_font_werewolf = input_font = pygame.font.Font(None, 40)
    text_objects.append(
        input_font_werewolf.render(
            "The werewolves wake up! Enter the name of the player that is endangered",
            True,
            "Yellow",
        )
    )


    # 20
    input_font_saviour = input_font = pygame.font.Font(None, 40)
    text_objects.append(
        input_font_seer.render(
            "The saviour wakes up! Enter the name of the player to protect",
            True,
            "Yellow",
        )
    )

    # 21
    input_font_saviour = input_font = pygame.font.Font(None, 40)
    text_objects.append(
        input_font_seer.render(
            "The thief wakes up! Enter the name of the player swap role with",
            True,
            "Yellow",
        )
    )

    # 22
    title_font = pygame.font.Font(None, 70)
    text_objects.append(
        title_font.render(
            "The village is awake: Day phase",
            True,
            "Black",
        )
    )

    # 23
    input_font_werewolf = input_font = pygame.font.Font(None, 40)
    text_objects.append(
        input_font_werewolf.render(
            "It's time for the vote. Enter the player that the village voted for to pass the vote test: ",
            True,
            "Black",
        )
    )


    return text_objects
