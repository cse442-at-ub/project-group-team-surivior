import pygame,sys,threading,inputSys

# use python -m PyInstaller main.py to pack this floder into exe file

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
inputSystem = inputSys.inputload()

my_font = pygame.font.SysFont('Helvetica', 15)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    inputSys.inputUpdate(inputSystem)
    
    screen.fill((0,0,0))

    inputDebuger = {}
    for i in range(0,12):
        inputDebuger[i] = my_font.render(inputSystem["commandState"][i], False, (255, 255, 255))
        screen.blit(inputDebuger[i], (0,i*15))
    pygame.display.update()
    clock.tick(60)