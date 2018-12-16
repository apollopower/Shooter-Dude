import pygame
from pygame.locals import *

from map_objects.game_map import *

def main():
    # Initializing pygame session
    pygame.init()
    pygame.display.set_caption("Shooter Dude")


    # Initializing Game Surface
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Colors for Tiles
    textures = {
        'WALL': (135, 135, 135),
        'FLOOR': (255, 255, 255)
    }


    test_map = GameMap(map_width, map_height)
    test_map.make_map()

    running = True

    # Main Game Loop
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for col in range(map_height):
            for row in range(map_width):
                tile = test_map.tiles[row][col]
                pygame.draw.rect(screen, textures[tile.texture], (row*tile_size, col*tile_size, tile_size, tile_size))
        
        pygame.display.update()

    
if __name__ == "__main__":
    main()