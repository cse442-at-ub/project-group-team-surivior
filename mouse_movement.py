import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
CHARACTER_SPEED = 2

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Follows Mouse")

character = pygame.Rect(50, 50, 30, 30)

# Variables for tracking character movement
moving = False
target_x, target_y = character.centerx, character.centery

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                target_x, target_y = pygame.mouse.get_pos()
                moving = True

    # Calculate the direction vector from character to target
    dx, dy = target_x - character.centerx, target_y - character.centery
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if moving and distance > 0:
        # Normalize the direction vector
        dx /= distance
        dy /= distance

        # Move the character in the direction
        character.x += dx * CHARACTER_SPEED
        character.y += dy * CHARACTER_SPEED

    # Clear the screen
    screen.fill(WHITE)

    # Draw the character
    pygame.draw.rect(screen, (0, 0, 255), character)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
