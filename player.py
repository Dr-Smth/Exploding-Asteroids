import pygame
from circleshape import *
from constants import *
from shot import *

# --- Player class logic ---
class Player(CircleShape):
    def __init__(self, x, y, image, shot_image):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.shot_image = shot_image

        # Load the player ship image
        self.original_image = image

        # Create a rect for positioning
        self.rect = self.original_image.get_rect(center=(self.position.x, self.position.y))

    # enables the player ship to be drawn to the screen
    def draw(self, screen):
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)

        # Get the rect of the rotated image and set its center
        rotated_rect = rotated_image.get_rect(center=(self.position.x, self.position.y))

        # Blit the rotated image onto the screen
        screen.blit(rotated_image, rotated_rect)

    # enables the player ship shape to rotate
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # Keep rotation within 0-360 degrees
        self.rotation %= 360

    # enables the player ship to be updated
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # --- WASD ---
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # --- Arrows ---
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)


        # --- Shooting ---
        if keys[pygame.K_SPACE] and self.cooldown == 0:
            self.shoot()
            self.cooldown = 0.3
        if self.cooldown > 0:
            if self.cooldown - dt > 0:
                self.cooldown -= dt
            else:
                self.cooldown = 0
    
    # enables the player ship to move
    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # creates a new shot when called
    def shoot(self):
        # Create a new shot at the player's position
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.shot_image, self.rotation)
        # sets, rotates, and scales up the shot velocity vector
        new_shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED