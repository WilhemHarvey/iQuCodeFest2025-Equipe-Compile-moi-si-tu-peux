import pygame


def get_images():
    images_objects = []
    # 0
    images_objects.append(pygame.image.load("Game/start_screen/logo_loup_garou.png"))
    # 1
    images_objects.append(pygame.image.load("Game/start_screen/start_button.png"))
    # 2
    images_objects.append(pygame.image.load("Game/num_characters/villager_card.png"))
    # 3
    images_objects.append(pygame.image.load("Game/num_characters/werewolf_card.png"))
    # 4
    images_objects.append(pygame.image.load("Game/num_characters/cupid_card.png"))
    # 5
    images_objects.append(pygame.image.load("Game/num_characters/witch_card.png"))
    # 6
    images_objects.append(pygame.image.load("Game/num_characters/hunter_card.png"))
    # 7
    images_objects.append(pygame.image.load("Game/num_characters/seer_card.png"))
    # 8
    images_objects.append(pygame.image.load("Game/num_characters/captain_card.png"))
    # 9
    images_objects.append(pygame.image.load("Game/num_characters/thief_card.png"))
    # 10
    images_objects.append(pygame.image.load("Game/num_characters/savior_card.png"))
    # 11
    images_objects.append(pygame.image.load("Game/night_phase/moon.png"))
    return images_objects
