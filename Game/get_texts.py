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

    return text_objects
