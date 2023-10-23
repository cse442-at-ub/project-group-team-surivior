import pygame
import math
pygame.init()
character = pygame.Rect(200, 200, 30, 30)
character_x, character_y = pygame.mouse.get_pos()
character = pygame.Rect(200, 200, 30, 30)
dx, dy = character_x - character.centerx, character_y - character.centery
distance = math.sqrt(dx ** 2 + dy ** 2)