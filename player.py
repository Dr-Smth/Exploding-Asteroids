import pygame
from circleshape import *
from constants import *
from shot import *

# --- Player class logic ---
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    # creates the player ship shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # enables the player ship shape to be drawn to the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    # enables the player ship shape to rotate
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

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
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # creates a new shot when called
    def shoot(self):
        # Create a new shot at the player's position
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        # sets, rotates, and scales up the shot velocity vector
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED