import pygame
from circleshape import CircleShape
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.SPLIT_RADIUS:
            pass

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        break_angle = random.uniform(20, 50) 
            
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(break_angle) * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-break_angle) * 1.2
