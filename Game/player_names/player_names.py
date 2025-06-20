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
    title = text_objects[11]
    screen.blit(
        title, ((screen_dim[0] / 2) - (title.get_width() / 2), screen_dim[1] / 8)
    )
    # TODO, ÉCRIRE SUR DES LIGNES DIFFÉRENTES ET GARDER CE QUI EST ÉCRIT
    input_text_to_screen = title_font.render(input_text, True, "red")
    screen.blit(
        input_text_to_screen,
        (
            (screen_dim[0] / 2) - (input_text_to_screen.get_width() / 2),
            13 * (screen_dim[1] / 16),
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
