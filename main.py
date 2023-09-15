import pygame,sys,threading

pygame.init()
try:
    saveDataFile = open("saveFile.txt", "r")
except:
    saveDataFile = open("saveFile.txt", "w")
    saveDataFile = open("saveFile.txt", "r")
codeString = saveDataFile.read()

if codeString == '':
    saveDataFile = open("saveFile.txt", "w")
    saveDataFile.write("res_w = 1600 \n")
    saveDataFile.write("res_h = 900 \n")
    saveDataFile.write("BGMVolume = 5 \n")
    saveDataFile.write("SFXVolume = 5 \n")
    saveDataFile.close()
    res_w = 1600 
    res_h = 900 
    BGMVolume = 5
    SFXVolume = 5
else:
    exec(codeString)

screen = pygame.display.set_mode((res_w,res_h))
pygame.display.set_caption('ver0.001')
clock = pygame.time.Clock()

currentUpdateBlock = None
currentDrawBlock = None

subStateMachineArray = {}

objectPool = {}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)