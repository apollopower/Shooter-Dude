import pygame
from pygame.locals import *

from map_objects.tile import *
from map_objects.rectangle import *

tile_size = 40

map_width = 20
map_height = 15

screen_width = map_width * tile_size
screen_height = map_height * tile_size

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
    
    def initialize_tiles(self):
        tiles = [[Tile() for y in range(self.height)] for x in range(self.width)]
        return tiles
    
    def make_map(self):
        for y in range(map_height):
            for x in range(map_width):
                if (x == 0 or y == 0) or (x == map_width - 1 or y == map_height - 1):
                    self.tiles[x][y].texture = "WALL"
                    self.tiles[x][y].blocked = True
        
    
    def create_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                tile = self.tiles[x][y]

                tile.texture = 'FLOOR'
                tile.blocked = False
                tile.block_sight = False