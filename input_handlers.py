import pygame
from pygame.locals import *

def handle_keys(event):
    key = event.type


    # Movement Keys
    if key == KEYDOWN:
        if event.key == K_w:
            return {'move': (0, -5)}
        if event.key == K_s:
            return {'move': (0, 5)}
        if event.key == K_d:
            return {'move': (5, 0)}
        if event.key == K_a:
            return {'move': (-5, 0)}
    
    # Exit the game
    if key == pygame.QUIT:
        pygame.quit()
    
    # No key was pressed
    return {}