import pygame
import sys
from constants import *

def handle_start_state(screen, font, events, high_score):
    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Larger fonts size for start text
    v_large_font = pygame.font.SysFont("Arial", 108)
    large_font = pygame.font.SysFont("Arial", 54)
    medium_font = pygame.font.SysFont("Arial", 36)

    # Render the game title, instructions, and high score
    title_text = v_large_font.render("'Sploding Asteroids !!!", True, (255, 140, 0))
    instruction_text = large_font.render("Press ENTER to Start", True, (192, 192, 192))
    select_ship_text = font.render("Press S to Select Your Ship", True, (192, 192, 192))
    reset_save_text = font.render("Press R to reset Save File", True, (192, 192, 192))
    quit_text = font.render("Press Q to Quit Game", True, (192, 192, 192))
    high_score_text = medium_font.render(f"High Score: {high_score}", True, (255, 140, 0))

    # Get rectangles for positioning
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200))
    instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    select_ship_rect = select_ship_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
    reset_save_text_rect = reset_save_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150))
    quit_text_rect = quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))
    high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 300))

    # Blit the text onto the screen
    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
    screen.blit(select_ship_text, select_ship_rect)
    screen.blit(reset_save_text, reset_save_text_rect)
    screen.blit(quit_text, quit_text_rect)
    screen.blit(high_score_text, high_score_rect)

    # Handle events on start screen
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Start the game
                return "running"
            elif event.key == pygame.K_s:
                # Go to ship selection screen
                return "ship_select"
            elif event.key == pygame.K_r:
                #reset save file
                pass
            elif event.key == pygame.K_q:
                # Quit the game
                pygame.quit()
                sys.exit()

    return "start"