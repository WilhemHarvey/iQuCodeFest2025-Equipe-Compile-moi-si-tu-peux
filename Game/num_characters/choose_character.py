import pygame

pygame.font.init()
title_font = pygame.font.Font(None, 60)


def num_character(
    screen, character_number, image_objects, text_objects, screen_dim, input_text
):
    card = image_objects[2 + character_number]
    card = pygame.transform.scale(card, (screen_dim[0] / 3, screen_dim[0] / 3))

    screen.blit(
        card,
        ((screen_dim[0] / 2) - (card.get_width() / 2), screen_dim[1] / 4),
    )
    title = text_objects[2 + character_number]
    screen.blit(
        title, ((screen_dim[0] / 2) - (title.get_width() / 2), screen_dim[1] / 8)
    )

    input_text_to_screen = title_font.render(input_text, True, "red")
    screen.blit(
        input_text_to_screen,
        (
            (screen_dim[0] / 2) - (input_text_to_screen.get_width() / 2),
            13 * (screen_dim[1] / 16),
        ),
    )


def get_text(screen, input_text, character_number, error_text, screen_dim):
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                number_chosen = int(input_text)
                if number_chosen < 2 or character_number < 2:
                    number_of_this_character = int(number_chosen)
                    input_text = ""
                    return input_text, number_of_this_character
                else:
                    input_text = ""
                    text_to_show = error_text
                    black_space = pygame.Surface((screen_dim[0], (screen_dim[1] / 4)))
                    screen.blit(black_space, (0, 12 * (screen_dim[1] / 16)))
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
