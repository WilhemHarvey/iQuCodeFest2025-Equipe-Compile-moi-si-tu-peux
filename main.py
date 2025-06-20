import pygame

from Game.get_images import get_images
from Game.get_texts import get_texts
import Game.start_screen.start_screen as start_screen
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

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
    if game_step == 0:
        step_done = start_screen.intro_screen(
            screen, image_objects, text_objects, screen_dim
        )
        game_step += step_done
    elif game_step == 1:
        screen.fill((0, 0, 0))
        screen.blit(test_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)
