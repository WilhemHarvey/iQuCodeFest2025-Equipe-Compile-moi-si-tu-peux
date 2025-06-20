import pygame

pygame.font.init()
title_font = pygame.font.Font(None, 60)


def print_names(
    screen,
    input_text,
    image_objects,
    text_objects,
    screen_dim,
    error_text,
    players_names,
):
    # Title
    title = text_objects[11]
    screen.blit(
        title, ((screen_dim[0] / 2) - (title.get_width() / 2), screen_dim[1] / 8)
    )
    # previous_names
    font = pygame.font.SysFont(None, 40)

    line_height = 40  # Vertical spacing between lines
    if len(players_names) > 15:
        players_names_to_show = players_names[-15:]
    else:
        players_names_to_show = players_names

    for i, name in enumerate(players_names_to_show):
        text_surface = font.render(name, True, "red")  # white text
        screen.blit(
            text_surface,
            (100, screen_dim[1] / 8 + screen_dim[1] / 16 + (i * line_height)),
        )

    input_text_to_screen = title_font.render(
        f"Player {len(players_names)+1}: " + input_text, True, "red"
    )
    screen.blit(
        input_text_to_screen,
        (
            100,
            screen_dim[1] / 8
            + screen_dim[1] / 16
            + (len(players_names_to_show) * line_height),
        ),
    )

    return get_names(screen, error_text, screen_dim, players_names, input_text)


def get_names(screen, error_text, screen_dim, players_names, input_text):
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not input_text == "" and input_text not in players_names:
                    return input_text, input_text
                else:
                    input_text = ""
                    text_to_show = error_text
                    black_space = pygame.Surface((screen_dim[0], (screen_dim[1] / 4)))
                    screen.blit(black_space, (0, 12 * (screen_dim[1] / 16)))
                    screen.blit(
                        text_to_show,
                        (
                            (screen_dim[0] / 2) - (text_to_show.get_width() / 2),
                            12 * (screen_dim[1] / 16),
                        ),
                    )
                    pygame.display.update()
                    pygame.time.wait(2000)

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
    return input_text, None
