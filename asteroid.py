import pygame
import random
from circleshape import *
from constants import *

# --- Asteroid Class logic ---
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # enables an asteroid to be drawn to the screen
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    # enables asteroids to be updated
    def update(self, dt):
        self.position += self.velocity * dt

    # logic to split into two smaller asteroids when colliding with a shot
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 50
        else:
            split_angle = random.uniform(20, 50)

            first_angle = self.velocity.rotate(split_angle)
            second_angle = self.velocity.rotate(-split_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = first_angle * 1.2

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = second_angle * 1.2

            return 100

