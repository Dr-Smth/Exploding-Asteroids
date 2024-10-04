import pygame
from circleshape import *
from constants import *

# --- Shot Class logic ---
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # enables a shot to be drawn to the screen
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    # enables shots to be updated
    def update(self, dt):
        self.position += self.velocity * dt