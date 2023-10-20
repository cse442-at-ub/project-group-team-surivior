import os
import random
import math
import pygame
import globalVar,button
from os import listdir
from os.path import isfile, join

pygame.init()

# caption and icon
pygame.display.set_caption("Survivor")
# icon = pygame.image.load("FILE_NAME")
# pygame.display.set_icon(icon)

MAP_COLOR = (127, 127, 127) # map background color 地图背景颜色
globalVar.res_w = 1600
globalVar.res_h = 900
WIDTH, HEIGHT = globalVar.res_w, globalVar.res_h # window size 游戏窗口尺寸
WHITE = (255, 255, 255)
bg_img_name = "tile.png"

FPS = 60 # 每秒60帧
PLAYER_VEL = 3 #player speed 玩家移动速度

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background():
    background_img = pygame.image.load(join("asset","background",bg_img_name))
    width, height = background_img.get_width(), background_img.get_height()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    
    return tiles, background_img

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

# player
# playerIMG = pygame.image.load('FILE_NAME')
playerIMG = pygame.Rect(50, 50, 30, 30) # use rectangle for now
playerX = 500
playerY = 400

# def player():
#     window.blit(playerIMG,(playerX,playerY))
    
def main(window):
    clock = pygame.time.Clock()
    tiles, bg_image  = get_background()

    # Variables for tracking player movement
    moving = False
    target_x, target_y = playerIMG.centerx, playerIMG.centery

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # check if mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    target_x, target_y = pygame.mouse.get_pos()
                    moving = True

        # Calculate the direction vector from player to target
        dx, dy = target_x - playerIMG.centerx, target_y - playerIMG.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if moving and distance > 0:
            # Normalize the direction vector
            dx /= distance
            dy /= distance

            # Move the player in the direction
            playerIMG.x += dx * PLAYER_VEL
            playerIMG.y += dy * PLAYER_VEL
   
        draw(window, tiles, bg_image) # upload background
        
        # Draw the character
        pygame.draw.rect(window, (0, 0, 255), playerIMG)

        b = button.Button("exit",(0,0),window) #initialize a button
        b.draw() #visualize button
        if b.check_clicked(): #if mouse collide and clicked the button
            pygame.quit()
            
        pygame.display.update()
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)