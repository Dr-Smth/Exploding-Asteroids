import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initiates delta time variable
    dt = 0

    # Initiates player score and high score variables
    player_score = 0
    high_score = 0

     # Initialize sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign sprite groups to class-level containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Initiates player and astroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Initiates game font for on screen text
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

    game_state = "start"  # Possible states: "start", "running", "game_over"

    def reset_game():
        nonlocal player_score, updatable, drawable, asteroids, shots, player, asteroid_field
       
        # Reset the score
        player_score = 0

        # Clear all sprite groups
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()

        # Reinitialize sprite groups and containers
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = updatable
        Shot.containers = (shots, updatable, drawable)

        # Recreate player and asteroid field
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()

    while True:
        events = pygame.event.get()  # Collects all events once per frame

        # quits the game if user slects teh "x" button
        for event in events:
            if event.type == pygame.QUIT:
                return
        
        # --- Start screen logic ---
        if game_state == "start":
            # Fill the screen with a background color
            screen.fill((0, 0, 0))

            # Render the game title, instructions, and high score
            title_text = font.render("Asteroids !!!", True, (255, 255, 255))
            instruction_text = font.render("Press ENTER to Start", True, (255, 255, 255))
            high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

            # Get rectangles for positioning
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))

            # Blit the text onto the screen
            screen.blit(title_text, title_rect)
            screen.blit(instruction_text, instruction_rect)
            screen.blit(high_score_text, high_score_rect)

            # Handle events on start screen
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Start the game
                        reset_game()
                        game_state = "running"
        
        # --- Main game logic ---
        elif game_state == "running":
            # Fill the screen with a background color
            screen.fill((0,0,0))

            for object in updatable:
                object.update(dt)
            
            # Player - Asteroid collision detection and handeling
            for asteroid in asteroids:
                if asteroid.collision_check(player):
                    game_state = "game_over"
                    break

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

        # --- Game over screen logic ---
        elif game_state == "game_over":
            # Fill the screen with a background color
            screen.fill((0, 0, 0))

            # Render the game over text
            game_over_text = font.render("Game Over !!!", True, (255, 0, 0))
            score_text = font.render(f"Final Score: {player_score}", True, (255, 255, 255))
            restart_text = font.render("Press R to Restart, M for Menu, or Q to Quit", True, (255, 255, 255))
            well_done_text = font.render("Well Done, You've set a new High Score !!!", True, (255, 255, 255))

             # Get rectangles for positioning
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            well_done_rect = well_done_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

             # Blit the text onto the screen
            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)
            if player_score > high_score:
                screen.blit(well_done_text, well_done_rect)


            # Handle events on game over screen
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        if player_score > high_score:
                            high_score = player_score
                        reset_game()
                        game_state = "running"
                    elif event.key ==pygame.K_m:
                        if player_score > high_score:
                            high_score = player_score
                        reset_game()
                        game_state = "start"
                    elif event.key == pygame.K_q:
                        # Quit the game
                        return
                    
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()