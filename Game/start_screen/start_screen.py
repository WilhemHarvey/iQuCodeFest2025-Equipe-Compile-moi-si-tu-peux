import pygame


def intro_screen(screen, image_objects, text_objects, screen_dim):
    # Logo
    were_wolf_logo = image_objects[0]
    were_wolf_logo = pygame.transform.scale(
        were_wolf_logo, (screen_dim[0] / 2, screen_dim[1] / 2)
    )
    screen.blit(
        were_wolf_logo,
        ((screen_dim[0] / 2) - (were_wolf_logo.get_width() / 2), screen_dim[1] / 4),
    )
    # Title
    title = text_objects[0]
    screen.blit(
        title, ((screen_dim[0] / 2) - (title.get_width() / 2), screen_dim[1] / 8)
    )
    # Button

    button = image_objects[1]
    button = pygame.transform.scale(
        button, (screen_dim[0] / 3, screen_dim[1] / 5)
    ).convert_alpha()

    rectangle = button.get_rect()
    rectangle.topleft = (
        (screen_dim[0] / 2) - (button.get_width() / 2),
        12 * (screen_dim[1] / 16),
    )

    screen.blit(
        button,
        (rectangle.x, rectangle.y),
    )

    pos = pygame.mouse.get_pos()

    if rectangle.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            return 1

    return 0
