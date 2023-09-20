import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("PlayerMap")

MAP_COLOR = (127, 127, 127) # 地图背景颜色
WIDTH, HEIGHT = 1000, 800 # 游戏窗口尺寸

FPS = 60 # 每秒60帧
PLAYER_VEL = 5 #玩家移动速度

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
    image = pygame.image.load(join("assets","background",name))
    width, height = image.get_width(), image.get_height()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    
    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image  = get_background("地砖.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)