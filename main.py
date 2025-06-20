import pygame
import numpy as np

from Game.get_images import get_images
from Game.get_texts import get_texts
import Game.start_screen.start_screen as start_screen
import Game.num_characters.choose_character as choose_character
import Game.player_names.player_names as player_names
import Game.assign_roles.assign_roles as assign_roles
import Game.night_phase.night_functions as night_functions
import Game.day_phase.day_functions as day_functions
import Game.mecanics.Play_game as play_mecanics
import Game.mecanics.Night_game as night_mecanics
import Game.mecanics.Day_game as day_mecanics
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
            ## Transition to next step
            game_step += 1
            ### Create game_instance
            game_variables = play_mecanics.Play(players_names, num_roles)

            # Get the name and role index in the previous list
            current_player = 0
            player_name = game_variables.player_names[0]
            role_index = assign_roles.ROLES.index(
                game_variables.player_roles[game_variables.players[player_name]]
            )

    elif game_step == 3:
        screen.fill((0, 0, 0))
        distributed = assign_roles.print_roles(
            screen, player_name, role_index, image_objects, text_objects, screen_dim
        )
        if distributed == True:
            current_player += 1
            if current_player < len(game_variables.ind2name):
                # Get the name and role index in the previous list
                player_name = game_variables.player_names[current_player]
                role_index = assign_roles.ROLES.index(
                    game_variables.player_roles[game_variables.players[player_name]]
                )
            else:
                ##Transition to first night
                game_step += 1
                first_lover_entered = False
                if game_variables.num_of_roles[2] == 0:
                    game_step += 1
                night_phase_step = 0
                seer_selected = False
                night_obj = night_mecanics.Night(
                    game_variables.player_roles,
                    witch_power=game_variables.witch_power,
                    couple=game_variables.couple,
                )

    elif game_step == 4:
        screen.fill((0, 0, 0))
        input_text, name_entered = night_functions.cupid(
            screen,
            input_text,
            image_objects,
            text_objects,
            screen_dim,
            game_variables,
            first_lover_entered,
        )
        if name_entered == True:
            if first_lover_entered == False:
                first_lover_entered = True
            else:
                ##Get to the actual night process
                game_step += 1
                night_obj.in_love = couple = game_variables.couple

    elif game_step == 5:
        screen.fill((0, 0, 0))
        ###SEER
        if night_phase_step == 0:
            if not "Seer" in game_variables.player_roles:
                night_phase_step += 1
            else:
                if seer_selected == False:
                    input_text, seer_selected = night_functions.seer(
                        screen,
                        input_text,
                        image_objects,
                        text_objects,
                        screen_dim,
                        game_variables,
                    )
                    if seer_selected == True:
                        role_to_show_index = play_mecanics.ROLES.index(input_text)

                else:
                    night_functions.show_seer(
                        screen,
                        role_to_show_index,
                        input_text,
                        image_objects,
                        text_objects,
                        screen_dim,
                    )
                    for event in pygame.event.get():
                        if event.type == pygame.quit:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                night_phase_step += 1
                                input_text = ""
        # Werewolves
        elif night_phase_step == 1:
            input_text, player_chosen = night_functions.werewolf(
                screen,
                input_text,
                image_objects,
                text_objects,
                screen_dim,
                game_variables,
            )
            if player_chosen == True:
                night_obj.Werewolf(input_text)
                night_phase_step += 1
                endangered_player = game_variables.ind2name[input_text]
                input_text = ""
        ##Witches
        elif night_phase_step == 2:
            if (
                not "Witch" in game_variables.player_roles
                and game_variables.witch_power == [False, False]
            ):
                night_phase_step += 1
            else:
                input_text, choice_made = night_functions.witch(
                    screen,
                    input_text,
                    image_objects,
                    text_objects,
                    screen_dim,
                    game_variables,
                    endangered_player,
                )
                if choice_made == True:
                    if input_text == "save":
                        night_obj.Witch(save_attacked_player=True)
                    else:
                        night_obj.Witch(attack_player_index=input_text)
                    night_phase_step += 1
                    input_text = ""

    pygame.display.update()
    clock.tick(60)
