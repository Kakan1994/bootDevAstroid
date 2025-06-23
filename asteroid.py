from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        # Aseteroids move in a straight line at a constant speed
        self.position += self.velocity * dt

    def split(self):
        # Split the asteroid into two smaller asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(random_angle) * ASTEROID_SPLIT_VELOCITY
        asteroid2.velocity = self.velocity.rotate(-random_angle) * ASTEROID_SPLIT_VELOCITY
        asteroid1.add(*Asteroid.containers)
        asteroid2.add(*Asteroid.containers)
        return asteroid1, asteroid2