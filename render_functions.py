import pygame
from pygame.locals import *

from map_objects.game_map import tile_size
from textures import *


def render_all(screen, game_map, player):
    for y in range(game_map.height):
        for x in range(game_map.width):
            tile = game_map.tiles[x][y]
            pygame.draw.rect(screen, textures[tile.texture], (x*tile_size, y*tile_size, tile_size, tile_size))
    
    screen.blit(textures[player.texture], (player.x, player.y))

def draw_entity():
    pass