import pygame


def get_texts():
    text_objects = []
    title_font = pygame.font.Font(None, 100)
    text_objects.append(title_font.render("Quantum Werewolf", True, "Red"))

    return text_objects
