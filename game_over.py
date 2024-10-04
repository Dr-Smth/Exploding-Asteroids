import pygame
import sys
from constants import *

def handle_game_over_state(screen, font, events, player_score, high_score):
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
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart the game
                return "running", max(player_score, high_score)
            elif event.key ==pygame.K_m:
                # Returns to start screen
                return "start", max(player_score, high_score)
            elif event.key == pygame.K_q:
                # Quit the game
                pygame.quit()
                sys.exit()

    return "game_over", high_score