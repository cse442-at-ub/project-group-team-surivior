import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
ENEMY_SPEED = 1
CHARACTER_SPEED = 2  # Adjust the target's movement speed
FPS = 60  # Set the desired frames per second

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Chases Red Square")

enemy = pygame.Rect(50, 50, 30, 30)  # blue square
character = pygame.Rect(200, 200, 30, 30)  # red square

moving = False

# clock = pygame.time.Clock()  # Create a clock object

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                character_x, character_y = pygame.mouse.get_pos()
                moving = True

    if moving:
        # Calculate the direction vector from ENEMY to target
        dx, dy = character_x - character.centerx, character_y - character.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            # Normalize the direction vector
            dx /= distance
            dy /= distance

            # Move the target (red square) towards the clicked position
            character.x += dx * CHARACTER_SPEED
            character.y += dy * CHARACTER_SPEED

    # Calculate the direction vector from enemy to character
    dx, dy = character.centerx - enemy.centerx, character.centery - enemy.centery
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance > 0:
        dx /= distance
        dy /= distance

        # Move the character in the direction
        enemy.x += dx * ENEMY_SPEED
        enemy.y += dy * ENEMY_SPEED

    screen.fill(WHITE)

    # Draw the squares
    pygame.draw.rect(screen, RED, character)
    pygame.draw.rect(screen, BLUE, enemy)

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)  # Control the frame rate

pygame.quit()
