import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def handle_running_state(screen, updatable, drawable, asteroids, shots, player, dt, player_score, asteroid_kill_score, asteroid_kills, time_score, font, events):
    # Fill the screen with a background color
    screen.fill((0,0,0))

    time_score += dt * 20
    if time_score >= 1:
        player_score += 1
        time_score = 0
    
    for object in updatable:
        object.update(dt)
    
    # Player - Asteroid collision detection and handeling
    for asteroid in asteroids:
        if asteroid.collision_check(player):
            return "game_over", player_score, asteroid_kill_score, asteroid_kills, time_score

    # Shot - Asteroid collision detection and handeling
    for asteroid in asteroids:
        for shot in shots:
            if asteroid.collision_check(shot):
                temp_asteroid_score = asteroid.split()
                asteroid_kill_score += temp_asteroid_score
                player_score += temp_asteroid_score
                asteroid_kills += 1
                shot.kill()

    # Draws all drawable objects to the screen
    for object in drawable:
        object.draw(screen)

    # Render the score text
    score_text = font.render(f"Score: {player_score}", True, (255, 140, 0))
    # Blit the score text onto the screen at the desired position
    screen.blit(score_text, (10, 10))

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return "running", player_score, asteroid_kill_score, asteroid_kills, time_score