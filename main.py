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
    print("Starting 'Sploding Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initiates delta time variable
    dt = 0

    # Initiates player score and high score variables
    player_score = 0
    high_score = 0

    # Load player assets
    player_assets = [
        pygame.image.load("Assets/Ships/Ahmed's SpaceShip.png").convert_alpha(),
        pygame.image.load("Assets/Ships/orange_01.png").convert_alpha(),
        pygame.image.load("Assets/Ships/orange_02.png").convert_alpha()
    ]

    # Scale player images
    player_assets = [pygame.transform.scale(img, (64, 64)) for img in player_assets]

    selected_ship_index = 0  # Default selected ship
    selected_ship_image = player_assets[selected_ship_index]
        
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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, selected_ship_image)
    asteroid_field = AsteroidField()

    # Initiates game font for on screen text
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

    game_state = "start"  # Possible states: "start", "ship_select", "running", "game_over"

    def reset_game():
        nonlocal player_score, updatable, drawable, asteroids, shots, player, asteroid_field, selected_ship_image
       
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
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, selected_ship_image)
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
            title_text = font.render("'Sploding Asteroids !!!", True, (255, 255, 255))
            instruction_text = font.render("Press ENTER to Start", True, (255, 255, 255))
            select_ship_text = font.render("Press S to Select Your Ship", True, (255, 255, 255))
            high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

            # Get rectangles for positioning
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            select_ship_rect = select_ship_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150))

            # Blit the text onto the screen
            screen.blit(title_text, title_rect)
            screen.blit(instruction_text, instruction_rect)
            screen.blit(select_ship_text, select_ship_rect)
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
                    elif event.key == pygame.K_s:
                        # Go to ship selection screen
                        game_state = "ship_select"
        
        # --- Ship selection screen logic ---
        elif game_state == "ship_select":
            # Fill the screen with a background color
            screen.fill((0, 0, 0))

            # Render the selection instructions
            select_text = font.render("Select Your Ship", True, (255, 255, 255))
            instruction_text = font.render("Click on a ship to select it", True, (255, 255, 255))
            back_text = font.render("Press B to go Back", True, (255, 255, 255))

            # Get rectangles for positioning
            select_rect = select_text.get_rect(center=(SCREEN_WIDTH / 2, 50))
            instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
            back_rect = back_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))

            # Blit the text onto the screen
            screen.blit(select_text, select_rect)
            screen.blit(instruction_text, instruction_rect)
            screen.blit(back_text, back_rect)

            # Display the ship options
            ship_rects = []
            for index, ship_image in enumerate(player_assets):
                # Calculate position for each ship
                ships_total = len(player_assets)
                spacing = 150
                total_width = (ships_total - 1) * spacing
                x_position = (SCREEN_WIDTH / 2 - total_width / 2) + index * spacing
                y_position = SCREEN_HEIGHT / 2

                # Get the rect for mouse collision detection
                ship_rect = ship_image.get_rect(center=(x_position, y_position))
                ship_rects.append(ship_rect)

                # Draw a rectangle around the selected ship
                if index == selected_ship_index:
                    pygame.draw.rect(
                        screen,
                        (255, 255, 0),
                        ship_rect.inflate(10, 10),
                        2
                    )

                # Blit the ship image
                screen.blit(ship_image, ship_rect)
            
            # Handle events on ship selection screen
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Left mouse button clicked
                    mouse_pos = event.pos
                    for index, ship_rect in enumerate(ship_rects):
                        if ship_rect.collidepoint(mouse_pos):
                            selected_ship_index = index
                            selected_ship_image = player_assets[selected_ship_index]
                            break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        # Go back to the start screen
                        game_state = "start"

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