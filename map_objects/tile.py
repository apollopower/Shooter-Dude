import pygame
from pygame.locals import *

class Tile:
    def __init__(self, size=40, texture="FLOOR", blocked=False, block_sight=None):
        self.size = size
        self.texture = texture
        self.blocked = blocked
        
        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight