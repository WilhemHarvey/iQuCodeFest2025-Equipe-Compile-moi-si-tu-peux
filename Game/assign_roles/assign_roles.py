import pygame

pygame.font.init()
title_font = pygame.font.Font(None, 60)

ROLES = [
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


def print_roles(
    screen,
    player_name,
    role_index,
    image_objects,
    text_objects,
    screen_dim,
):
    card = image_objects[2 + role_index]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 4),
    )
    title = text_objects[13]
    screen.blit(
        title, ((screen_dim[0] / 2) - (title.get_width() / 2), screen_dim[1] / 8)
    )

    character_name = ROLES[role_index]

    input_text_to_screen = title_font.render(
        player_name + ": " + character_name, True, "red"
    )
    screen.blit(
        input_text_to_screen,
        (
            (screen_dim[0] / 2) - (input_text_to_screen.get_width() / 2),
            13 * (screen_dim[1] / 16),
        ),
    )

    return get_text()


def get_text():
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True

    return False
