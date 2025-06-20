import pygame

pygame.font.init()
title_font = pygame.font.Font(None, 60)


def cupid(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
    first_lover_entered,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[4]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    if first_lover_entered == False:
        enter_name = text_objects[16]
    else:
        enter_name = text_objects[17]
    screen.blit(
        enter_name,
        (
            (screen_dim[0] / 2) - (enter_name.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
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
        game_variables.couple.append(target)
        input_text = ""
        return input_text, True
    return input_text, False


def seer(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[7]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[18]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
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
        return game_variables.player_roles[target], True
    return input_text, False


def show_seer(
    screen,
    role_index,
    role_name,
    image_objects,
    text_objects,
    screen_dim,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[2 + role_index]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # INPUT
    role_text = title_font.render(
        "The player is a: " + role_name + "! Press enter to continue", True, "Yellow"
    )
    screen.blit(
        role_text,
        (
            (screen_dim[0] / 2) - (role_text.get_width() / 2),
            13 * (screen_dim[1] / 16),
        ),
    )


def werewolf(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[3]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[19]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
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


def witch(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
    endangered_player_name,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[5]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    input_font_witch = pygame.font.Font(None, 40)
    prompt = input_font_witch.render(
        "The witch wakes up!",
        True,
        "Yellow",
    )
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # Save
    if game_variables.witch_power[0] == True:
        input_font_witch = pygame.font.Font(None, 40)
        save_text = "Write 'save' if you want to save " + str(endangered_player_name)
        prompt = input_font_witch.render(
            save_text,
            True,
            "Yellow",
        )
        screen.blit(
            prompt,
            (
                (screen_dim[0] / 2) - (prompt.get_width() / 2),
                12 * (screen_dim[1] / 16),
            ),
        )
        # Save
    if game_variables.witch_power[1] == True:
        input_font_witch = pygame.font.Font(None, 40)
        prompt = input_font_witch.render(
            f"Write the player name that you want to kill ",
            True,
            "Yellow",
        )
        screen.blit(
            prompt,
            (
                (screen_dim[0] / 2) - (prompt.get_width() / 2),
                13 * (screen_dim[1] / 16),
            ),
        )
    input_font_witch = pygame.font.Font(None, 40)
    prompt = input_font_witch.render(
        f"Write 'nothing' if you want to do nothing.",
        True,
        "Yellow",
    )
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            14 * (screen_dim[1] / 16),
        ),
    )

    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
    screen.blit(
        input_text_to_screen,
        (
            (screen_dim[0] / 2) - (input_text_to_screen.get_width() / 2),
            15 * (screen_dim[1] / 16),
        ),
    )

    input_text, target = get_text_witch(
        screen, input_text, text_objects[14], screen_dim, game_variables
    )

    if target is not None:
        input_text = ""
        return target, True
    return input_text, False


def get_text_witch(screen, input_text, error_text, screen_dim, game_variables):
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text == "save":
                    return input_text, True
                if input_text == "nothing":
                    return input_text, True
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


def savior(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[10]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[20]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
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


def thief(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    game_variables,
):
    moon = image_objects[11]
    moon = pygame.transform.scale(moon, (screen_dim[0] / 8, screen_dim[1] / 8))
    screen.blit(moon, (7 * screen_dim[0] / 8, 1 * screen_dim[1] / 64))

    card = image_objects[9]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 6),
    )
    # Title
    title = text_objects[15]
    screen.blit(title, (screen_dim[1] / 16, screen_dim[1] / 16))

    # Prompt
    prompt = text_objects[21]
    screen.blit(
        prompt,
        (
            (screen_dim[0] / 2) - (prompt.get_width() / 2),
            11 * (screen_dim[1] / 16),
        ),
    )
    # INPUT
    input_text_to_screen = title_font.render(input_text, True, "Yellow")
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
