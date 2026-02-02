import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        # must override
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_asteriod_direction = self.velocity.rotate(random_angle)
            second_asteroid_direction = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_split_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_split_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_split_asteroid.velocity = first_asteriod_direction * 1.2
            second_split_asteroid.velocity = second_asteroid_direction * 1.2
