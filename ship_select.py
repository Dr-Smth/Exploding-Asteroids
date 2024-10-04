import pygame
import sys
from constants import *

def handle_ship_select_state(screen, font, events, player_assets, selected_ship_index):
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
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button clicked
            mouse_pos = event.pos
            for index, ship_rect in enumerate(ship_rects):
                if ship_rect.collidepoint(mouse_pos):
                    selected_ship_index = index
                    break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                # Go back to the start screen
                return "start", selected_ship_index, player_assets[selected_ship_index]

    return "ship_select", selected_ship_index, player_assets[selected_ship_index]
