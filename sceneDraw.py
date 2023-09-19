import pygame,globalVar

def drawBlack():
    pygame.draw.rect(globalVar.screen, (0,0,0), pygame.Rect(1600, 900, 0, 0))

def drawOneImageObject(frame,object,screen):
    x = object[0]
    y = object[1]
    screen.blit(frame, (x, y))

def drawArrayImageObject(frames,object,screen):
    x = object[0]
    y = object[1]

    frameNum = object[5]
    screen.blit(frames[frameNum], (x, y))

def firstLoadingDraw():

    drawArrayImageObject(globalVar.assetPool[1:61],globalVar.objectPool[0],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[0],globalVar.objectPool[1],globalVar.screen)

    s = pygame.Surface((1600,900))
    s.set_alpha(globalVar.objectPool[2][4])
    s.fill((0,0,0))
    globalVar.screen.blit(s, (0, 0))