import pygame
import math

def game():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    ENEMY_SPEED = 1
    CHARACTER_SPEED = 3  
    FPS = 60  

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PINK= (255, 0, 255)  # RGB color code for pink
    CYAN = (0, 255, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Character Chases Red Square")

    enemy = pygame.Rect(50, 50, 30, 30)  # blue square
    character = pygame.Rect(200, 200, 30, 30)  # red square

    moving = False
    health = 20  # Character's initial health
    damage = 10  # Initial damage dealt by the enemy
    attack_timer = 0  # Timer for enemy attack
    color_change_timer = 0  # Timer for character color change
    color_change_timer_heal = 0

    clock = pygame.time.Clock() 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    character_x, character_y = pygame.mouse.get_pos()
                    moving = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and health < 20:  # Heal when 'R' key is pressed and health is less than 20
                    health += 10
                    color_change_timer_heal = int(0.1 * FPS)  # Set color change timer to 0.1 seconds when healing
                    character_color = CYAN  # Character turns green while healing
                
        if moving:
            dx, dy = character_x - character.centerx, character_y - character.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance > 0:
                dx /= distance
                dy /= distance

                character.x += dx * CHARACTER_SPEED
                character.y += dy * CHARACTER_SPEED

        dx, dy = character.centerx - enemy.centerx, character.centery - enemy.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if health > 0 and distance <= 15 and attack_timer <= 0:  
            health -= damage  # Reduce character's health
            attack_timer = FPS  # Set the attack timer to 1 second (FPS frames)
            color_change_timer = int(0.1 * FPS)  # Set color change timer to 0.1 seconds

        attack_timer = max(0, attack_timer - 1)  # Decrease the attack timer
        color_change_timer = max(0, color_change_timer - 1)  # Decrease the color change timer
        color_change_timer_heal = max(0, color_change_timer_heal - 1)  # Decrease the color change timer

        if color_change_timer > 0:
            character_color = GREEN  # Character turns green for 0.1 seconds after being attacked
        elif color_change_timer_heal > 0:
            character_color = CYAN  # Character turns green for 0.1 seconds after being attacked

        elif health <= 0:
            character_color = PINK  # Character turns pink when health reaches 0
        else:
            character_color = RED  # Character remains red if not attacked

        if distance > 0:
            dx /= distance
            dy /= distance

            enemy.x += dx * ENEMY_SPEED
            enemy.y += dy * ENEMY_SPEED

        screen.fill(WHITE)

        pygame.draw.rect(screen, character_color, character)
        pygame.draw.rect(screen, BLUE, enemy)

        pygame.display.flip()

        clock.tick(FPS) 

    pygame.quit()