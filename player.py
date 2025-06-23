from circleshape import CircleShape
from shot import Shot
import pygame
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        # Start with a unit vector pointing up from 0,0 to 0,1
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        forward = (pygame.Vector2(0, 1).rotate(self.rotation))
        velocity = forward * PLAYER_SHOT_SPEED
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y)
        shot.velocity = velocity
        shot.add(*Shot.containers)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shot_cooldown = PLAYER_SHOT_COOLDOWN
                self.shoot()
