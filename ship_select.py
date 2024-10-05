import pygame
import sys
from constants import *

def handle_ship_select_state(screen, font, events, player_assets, selected_ship_index):
    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Render the selection instructions
    select_text = font.render("Select Your Ship", True, (255, 140, 0))
    instruction_text = font.render("Click on a ship, or use the arrow keys, to select it", True, (192, 192, 192))
    back_text = font.render("Press ENTER to select ship and go to the main menu", True, (192, 192, 192))

    # Get rectangles for positioning
    select_rect = select_text.get_rect(center=(SCREEN_WIDTH / 2, 50))
    instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))

    # Blit the text onto the screen
    screen.blit(select_text, select_rect)
    screen.blit(instruction_text, instruction_rect)
    screen.blit(back_text, back_rect)

    # Display the ship options in a grid layout
    ship_rects = []

    # Grid settings
    num_columns = 12
    spacing_x = 100  # Horizontal spacing between ships
    spacing_y = 90  # Vertical spacing between ships

    # Calculate starting positions
    total_columns = min(num_columns, len(player_assets))
    total_rows = (len(player_assets) + num_columns - 1) // num_columns

    grid_width = (total_columns - 1) * spacing_x
    grid_height = (total_rows - 1) * spacing_y

    start_x = (SCREEN_WIDTH - grid_width) / 2
    start_y = (SCREEN_HEIGHT - grid_height) / 2 + 25

    for index, ship_image in enumerate(player_assets):
        row = index // num_columns
        col = index % num_columns

        x_position = start_x + col * spacing_x
        y_position = start_y + row * spacing_y

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
            if event.key == pygame.K_RETURN:
                # Go back to the start screen
                return "start", selected_ship_index, player_assets[selected_ship_index]
            elif event.key == pygame.K_RIGHT:
                # Move selection right
                if (selected_ship_index % num_columns) < (num_columns - 1):
                    if selected_ship_index + 1 < len(player_assets):
                        selected_ship_index += 1
                else:
                    # Wrap to the start of the next row if applicable
                    if selected_ship_index + 1 < len(player_assets):
                        selected_ship_index += 1
            elif event.key == pygame.K_LEFT:
                # Move selection left
                if (selected_ship_index % num_columns) > 0:
                    selected_ship_index -= 1
            elif event.key == pygame.K_DOWN:
                # Move selection down
                if selected_ship_index + num_columns < len(player_assets):
                    selected_ship_index += num_columns
            elif event.key == pygame.K_UP:
                # Move selection up
                if selected_ship_index - num_columns >= 0:
                    selected_ship_index -= num_columns


    return "ship_select", selected_ship_index, player_assets[selected_ship_index]
