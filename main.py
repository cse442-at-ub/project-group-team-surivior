import pygame,sys,threading,inputSys,sceneLogic,sceneDraw,globalVar

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
    saveDataFile.write("globalVar.res_w = 1600 \n")
    saveDataFile.write("globalVar.res_h = 900 \n")
    saveDataFile.write("globalVar.BGMVolume = 5 \n")
    saveDataFile.write("globalVar.SFXVolume = 5 \n")
    saveDataFile.close()
    globalVar.res_w = 1600 
    globalVar.res_h = 900 
    globalVar.BGMVolume = 5
    globalVar.SFXVolume = 5
else:
    exec(codeString)

globalVar.screen = pygame.display.set_mode((globalVar.res_w,globalVar.res_h),pygame.RESIZABLE)
pygame.display.set_caption('ver0.001')
clock = pygame.time.Clock()

globalVar.currentUpdateBlock = sceneLogic.beforeFirstLoadingLogic
globalVar.currentDrawBlock = sceneDraw.drawBlack4Start

globalVar.inputSystem = inputSys.inputload()

my_font = pygame.font.SysFont('Helvetica', 15)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    inputSys.inputUpdate(globalVar.inputSystem)
    globalVar.screen.fill((0,0,0))

    globalVar.currentUpdateBlock()
    globalVar.currentDrawBlock()

    inputDebuger = {}
    for i in range(0,13):
        inputDebuger[i] = my_font.render(globalVar.inputSystem["commandState"][i], False, (255, 255, 255))
        globalVar.screen.blit(inputDebuger[i], (0,i*15))

    pygame.display.update()
    clock.tick(60)