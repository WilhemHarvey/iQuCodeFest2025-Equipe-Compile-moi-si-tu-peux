import pygame

import Game as to_name
import Wolfpaq as game
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Quantum werewolf")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
