import pygame
import random
from circleshape import *
from constants import *

# --- Asteroid Class logic ---
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroid_assets):
        super().__init__(x, y, radius)
        self.asteroid_assets = asteroid_assets
        self.image = random.choice(asteroid_assets)
        if radius <= 20:
            self.image = pygame.transform.scale(self.image, (32, 32))
        elif radius <= 40:
            self.image = pygame.transform.scale(self.image, (64, 64))
        else:
            self.image = pygame.transform.scale(self.image, (128, 128))

        # Create a rect for positioning
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
    
    # enables an asteroid to be drawn to the screen
    def draw(self, screen):
        # Update image position
        self.rect = self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        # Blit the asteroid image onto the screen
        screen.blit(self.image, self.rect)
    
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

            asteroid = Asteroid(self.position.x, self.position.y, new_radius, self.asteroid_assets)
            asteroid.velocity = first_angle * 1.2

            asteroid = Asteroid(self.position.x, self.position.y, new_radius, self.asteroid_assets)
            asteroid.velocity = second_angle * 1.2

            if self.radius <= 40:
                return 150
            else:
                return 300