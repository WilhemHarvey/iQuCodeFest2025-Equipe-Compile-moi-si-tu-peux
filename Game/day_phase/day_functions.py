import pygame

pygame.font.init()
title_font = pygame.font.Font(None, 60)


def vote(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
):
    sun = image_objects[12]
    sun = pygame.transform.scale(sun, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(sun, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[13]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[22]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[23]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Black")
    screen.blit(
        input_text_to_screen,
        (
            (screen_dim[0] / 2) - (input_text_to_screen.get_width() / 2),
            13 * (screen_dim[1] / 16),
        ),
    )
    input_text, target = get_text(
        screen, input_text, text_objects[14], screen_dim, game_variables
    )

    if target is not None:
        input_text = ""
        return target, True
    return input_text, False


def get_text(screen, input_text, error_text, screen_dim, game_variables):
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                player_name = input_text
                if player_name in game_variables.active_player_names:
                    target = game_variables.players[player_name]
                    input_text = ""
                    return player_name, target
                else:
                    input_text = ""
                    text_to_show = error_text
                    black_space = pygame.Surface((screen_dim[0], (screen_dim[1] / 2)))
                    screen.blit(black_space, (0, 11 * (screen_dim[1] / 16)))
                    screen.blit(
                        text_to_show,
                        (
                            (screen_dim[0] / 2) - (text_to_show.get_width() / 2),
                            13 * (screen_dim[1] / 16),
                        ),
                    )
                    pygame.display.update()
                    pygame.time.wait(2000)

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    return input_text, None


def night_results(
    screen,
    image_objects,
    text_objects,
    screen_dim,
    killed_player_roles,
    killed_player_names,
):
    sun = image_objects[12]
    sun = pygame.transform.scale(sun, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(sun, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    # Title
    title = text_objects[22]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[24]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            3 * (screen_dim[1] / 16),
        ),
    )
    font_players = pygame.font.Font(None, 40)
    if len(killed_player_roles) == 0:
        prompt = font_players.render(
            "Nobody was killed!",
            True,
            "Black",
        )
        screen.blit(
            prompt,
            (
                (screen_dim[0] / 2) - (prompt.get_width() / 2),
                (5) * (screen_dim[1] / 16),
            ),
        )
    else:
        for i, player_name, player_role in enumerate(
            zip(killed_player_names, killed_player_roles)
        ):
            prompt = font_players.render(
                player_name + "was killed as a " + player_role,
                True,
                "Black",
            )
            screen.blit(
                prompt,
                (
                    (screen_dim[0] / 2) - (prompt.get_width() / 2),
                    (5 + 2 * i) * (screen_dim[1] / 16),
                ),
            )
            prompt = font_players.render(
                "Press enter to continue",
                True,
                "Black",
            )
            screen.blit(
                prompt,
                (
                    (screen_dim[0] / 2) - (prompt.get_width() / 2),
                    (15) * (screen_dim[1] / 16),
                ),
            )
