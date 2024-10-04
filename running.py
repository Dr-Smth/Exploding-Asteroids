from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def handle_running_state(screen, updatable, drawable, asteroids, shots, player, dt, player_score, font):
    # Fill the screen with a background color
    screen.fill((0,0,0))

    for object in updatable:
        object.update(dt)
    
    # Player - Asteroid collision detection and handeling
    for asteroid in asteroids:
        if asteroid.collision_check(player):
            return "game_over", player_score

    # Shot - Asteroid collision detection and handeling
    for asteroid in asteroids:
        for shot in shots:
            if asteroid.collision_check(shot):
                player_score += asteroid.split()
                shot.kill()

    # Draws all drawable objects to the screen
    for object in drawable:
        object.draw(screen)

    # Render the score text
    score_text = font.render(f"Score: {player_score}", True, (255, 255, 255))
    # Blit the score text onto the screen at the desired position
    screen.blit(score_text, (10, 10))

    return "running", player_score
