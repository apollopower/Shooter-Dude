import pygame
from pygame.locals import *

from textures import *
from map_objects.game_map import *
from input_handlers import handle_keys
from render_functions import *
from entity import *

def main():
    # Initializing pygame session
    pygame.init()
    pygame.display.set_caption("Shooter Dude")


    # Initializing Game Surface
    screen = pygame.display.set_mode((screen_width, screen_height))

    test_map = GameMap(map_width, map_height)
    test_map.make_map()

    player = Entity(int(screen_width / 2), int(screen_height / 2), 'PLAYER')


    # Main Game Loop
    while True:

        render_all(screen, test_map, player)

        # Event Handling
        for event in pygame.event.get():
            action = handle_keys(event)
        
        move = action.get('move')

        if move:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy

            if not test_map.is_blocked(destination_x, destination_y):
                player.move(dx, dy)
        
        pygame.display.update()

    
if __name__ == "__main__":
    main()