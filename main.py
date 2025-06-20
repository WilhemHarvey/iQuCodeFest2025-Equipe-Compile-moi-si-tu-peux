import pygame
import numpy as np

from Game.get_images import get_images
from Game.get_texts import get_texts
import Game.start_screen.start_screen as start_screen
import Game.num_characters.choose_character as choose_character
import Game.player_names.player_names as player_names
import Wolfpaq as mecanics
from sys import exit

pygame.init()
screen_dim = tuple([1200, 800])
screen = pygame.display.set_mode(screen_dim)
pygame.display.set_caption("Quantum werewolf")
clock = pygame.time.Clock()

image_objects = get_images()
text_objects = get_texts()
game_step = 0


while True:
    # Starting screen
    if game_step == 0:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                exit()
        step_done = start_screen.intro_screen(
            screen, image_objects, text_objects, screen_dim
        )
        ## Prepare parameters for next step
        game_step += step_done
        character = 0
        num_roles = []
        input_text = ""
    # Choose your character
    elif game_step == 1:
        screen.fill((0, 0, 0))
        choose_character.num_character(
            screen, character, image_objects, text_objects, screen_dim, input_text
        )
        input_text, number_of_this_character = choose_character.get_text(
            screen, input_text, character, text_objects[1], screen_dim
        )
        if number_of_this_character is not None:
            character += 1
            num_roles.append(number_of_this_character)
        if character == 9:
            # Preparing next step
            game_step += 1
            players_names = []
            num_players = np.sum(num_roles)
    elif game_step == 2:
        screen.fill((0, 0, 0))
        input_text, new_player = player_names.print_names(
            screen,
            input_text,
            image_objects,
            text_objects,
            screen_dim,
            text_objects[12],
            players_names,
        )
        if new_player is not None:
            players_names.append(new_player)
            input_text = ""
        if len(players_names) == num_players:
            game_step += 1

    elif game_step == 3:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(60)
