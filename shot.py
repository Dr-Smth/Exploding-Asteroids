import pygame
from circleshape import *
from constants import *

# --- Shot Class logic ---
class Shot(CircleShape):
    def __init__(self, x, y, radius, shot_image, rotation):
        super().__init__(x, y, radius)
        self.image = shot_image
        self.rotation = -rotation
        # Set the initial position
        self.rect = self.image.get_rect(center=(x, y))
    
    # enables a shot to be drawn to the screen
    def draw(self, screen):
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rotated_rect = rotated_image.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(rotated_image, rotated_rect)
    
    # enables shots to be updated
    def update(self, dt):
        self.position += self.velocity * dt