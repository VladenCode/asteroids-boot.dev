import pygame
from constants.py import LINE_WIDTH


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.radius, LINE_WIDTH)
    
    def update(self, dt):
        # must override
        pass
