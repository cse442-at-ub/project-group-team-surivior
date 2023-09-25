import pygame,globalVar

def drawBlack(object):
    s = pygame.Surface((1600,900))
    s.set_alpha(object[4])
    s.fill((0,0,0))
    globalVar.screen.blit(s, (0, 0))

def drawBlack4Start():
    s = pygame.Surface((1600,900))
    s.set_alpha(1)
    s.fill((0,0,0))
    globalVar.screen.blit(s, (0, 0))

def drawBlackBlock(object,w,h):
    s = pygame.Surface((w,h))
    s.set_alpha(object[4])
    s.fill((0,0,0))
    globalVar.screen.blit(s, (object[0], object[1]))

def drawOneImageObject(frame,object,screen):
    x = object[0]
    y = object[1]
    frame.set_alpha(object[4])
    screen.blit(frame, (x, y))

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def drawOneImageObjectInColor(frame,object,screen,newColor):
    x = object[0]
    y = object[1]
    frame = frame.copy
    frame.fill((0,0,0,255))
    frame.fill(newColor)
    screen.blit(frame, (x, y))

def drawArrayImageObject(frames,object,screen):
    x = object[0]
    y = object[1]
    frameNum = object[5]
    screen.blit(frames[frameNum], (x, y))

def disclaimerDraw():
    drawArrayImageObject(globalVar.assetPool[1:61],globalVar.objectPool[0],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[0],globalVar.objectPool[1],globalVar.screen)
    drawBlack(globalVar.objectPool[2])

def startScenenDraw():
    drawOneImageObject(globalVar.assetPool[14],globalVar.objectPool[25],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[13],globalVar.objectPool[24],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[12],globalVar.objectPool[23],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[11],globalVar.objectPool[22],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[10],globalVar.objectPool[21],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[15],globalVar.objectPool[26],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[8],globalVar.objectPool[20],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[8],globalVar.objectPool[19],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[8],globalVar.objectPool[18],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[8],globalVar.objectPool[17],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[8],globalVar.objectPool[16],globalVar.screen)
    drawBlackBlock(globalVar.objectPool[15],1600/5,900)
    drawBlackBlock(globalVar.objectPool[14],1600/5,900)
    drawBlackBlock(globalVar.objectPool[13],1600/5,900)
    drawBlackBlock(globalVar.objectPool[12],1600/5,900)
    drawBlackBlock(globalVar.objectPool[11],1600/5,900)
    # drawOneImageObjectInColor(globalVar.assetPool[9],globalVar.objectPool[10],globalVar.screen,(255, 0, 0, 255))
    drawOneImageObject(globalVar.assetPool[16],globalVar.objectPool[10],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[9],globalVar.objectPool[9],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[4],globalVar.objectPool[8],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[7],globalVar.objectPool[7],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[1],globalVar.objectPool[6],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[0],globalVar.objectPool[5],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[3],globalVar.objectPool[4],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[2],globalVar.objectPool[3],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[6],globalVar.objectPool[2],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[5],globalVar.objectPool[1],globalVar.screen)
    drawBlack(globalVar.objectPool[0])