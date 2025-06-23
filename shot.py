from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)

    def update(self, dt):
        # Shots move in a straight line at a constant speed
        self.position += self.velocity * dt

        # Remove the shot if it goes off-screen
        if (self.position.x < 0 or self.position.x > pygame.display.get_surface().get_width() or
            self.position.y < 0 or self.position.y > pygame.display.get_surface().get_height()):
            self.kill()