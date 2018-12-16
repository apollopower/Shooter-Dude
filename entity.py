import pygame
from pygame.locals import *

class Entity:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

    def move(self, dx, dy):
        # Move entity given amount
        self.x += dx
        self.y += dy