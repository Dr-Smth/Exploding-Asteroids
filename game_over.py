import pygame
import sys
from constants import *

def handle_game_over_state(screen, font, events, player_score, asteroid_kill_score, asteroid_kills, high_score):
    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    survival_time_score = player_score - asteroid_kill_score

    # Larger fonts size for the game over text
    v_large_font = pygame.font.SysFont("Arial", 144)
    large_font = pygame.font.SysFont("Arial", 54)
    medium_font = pygame.font.SysFont("Arial", 36)

    # Render the game over text
    game_over_text = v_large_font.render("Game Over !!!", True, (255, 0, 0))

    well_done_text = large_font.render("New High Score !!!", True, (255, 140, 0))

    score_text = medium_font.render(f"Final Score:                     {player_score}", True, (192, 192, 192))
    asteroid_kills_text = medium_font.render(f"Asteroids 'Sploded:     {asteroid_kills}", True, (192, 192, 192))
    asteroid_kill_score_text = medium_font.render(f"'Splosion Score:             {asteroid_kill_score}", True, (192, 192, 192))
    survival_time_score_text = medium_font.render(f"Survival Time Score:    {survival_time_score}", True, (192, 192, 192))

    restart_text = font.render("Press R to Restart, M for Menu, or Q to Quit", True, (192, 192, 192))

    # Get rectangles for positioning
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200))

    well_done_rect = well_done_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))

    score_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 + 50))
    asteroid_kills_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 + 100))
    asteroid_kills_score_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 + 150))
    survival_time_score_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 + 200))

    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 300))

    # Blit the text onto the screen
    screen.blit(game_over_text, game_over_rect)

    if player_score > high_score:
        screen.blit(well_done_text, well_done_rect)

    screen.blit(score_text, score_rect)
    screen.blit(asteroid_kills_text, asteroid_kills_rect)
    screen.blit(asteroid_kill_score_text, asteroid_kills_score_rect)
    screen.blit(survival_time_score_text, survival_time_score_rect)

    screen.blit(restart_text, restart_rect)

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