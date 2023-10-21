import pygame,globalVar

def drawBlack(object):
    x_win, y_win = globalVar.screen.get_size()
    s = pygame.Surface((x_win,y_win))
    s.set_alpha(object[4])
    s.fill((0,0,0))
    globalVar.screen.blit(s, (0, 0))

def drawBlack4Start():
    s = pygame.Surface((1600,900))
    s.set_alpha(1)
    s.fill((0,0,0))
    globalVar.screen.blit(s, (0, 0))

def drawBlackBlock(object,w,h):
    x = object[0]
    y = object[1]
    x_win, y_win = globalVar.screen.get_size()
    s = pygame.Surface((w*x_win/1600,h*y_win/900))
    s.set_alpha(object[4])
    s.fill((0,0,0))
    globalVar.screen.blit(s,  (x*x_win/1600, y*y_win/900))

def drawOneImageObject(frame,object,screen):
    x = object[0]
    y = object[1]
    x_win, y_win = screen.get_size()
    x_img, y_img = frame.get_size()
    image = pygame.transform.scale(frame, (x_img*x_win/1600,y_img*y_win/900))
    image.set_alpha(object[4])
    screen.blit(image, (x*x_win/1600, y*y_win/900))

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def drawArrayImageObject(frames,object,screen):
    x = object[0]
    y = object[1]
    frameNum = object[5]
    frame = frames[frameNum]
    x_win, y_win = screen.get_size()
    x_img, y_img = frame.get_size()
    image = pygame.transform.scale(frame, (x_img*x_win/1600,y_img*y_win/900))
    image.set_alpha(object[4])
    screen.blit(image, (x*x_win/1600, y*y_win/900))

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
    
    charFrameArray = []
    for i  in range(0,9):
        charFrameArray.append(globalVar.assetPool[i+39])

    drawOneImageObject(globalVar.assetPool[32],globalVar.objectPool[53],globalVar.screen)

    drawOneImageObject(globalVar.assetPool[33],globalVar.objectPool[47],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[33],globalVar.objectPool[48],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[33],globalVar.objectPool[49],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[33],globalVar.objectPool[50],globalVar.screen)

    drawOneImageObject(globalVar.assetPool[35],globalVar.objectPool[51],globalVar.screen) ## change 2 array
    drawOneImageObject(globalVar.assetPool[36],globalVar.objectPool[52],globalVar.screen)

    drawOneImageObject(globalVar.assetPool[30],globalVar.objectPool[44],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[22],globalVar.objectPool[43],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[23],globalVar.objectPool[42],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[18],globalVar.objectPool[41],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[24],globalVar.objectPool[40],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[19],globalVar.objectPool[39],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[27],globalVar.objectPool[38],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[26],globalVar.objectPool[37],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[28],globalVar.objectPool[36],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[20],globalVar.objectPool[35],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[31],globalVar.objectPool[33],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[29],globalVar.objectPool[32],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[21],globalVar.objectPool[31],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[48],globalVar.objectPool[30],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[21],globalVar.objectPool[29],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[17],globalVar.objectPool[28],globalVar.screen)
    
    plsFrameArray = [globalVar.assetPool[25],globalVar.assetPool[37],globalVar.assetPool[38]]
    drawArrayImageObject(plsFrameArray,globalVar.objectPool[34],globalVar.screen)

    drawOneImageObject(globalVar.assetPool[49],globalVar.objectPool[45],globalVar.screen)
    drawOneImageObject(globalVar.assetPool[34],globalVar.objectPool[46],globalVar.screen)
    drawArrayImageObject(charFrameArray,globalVar.objectPool[27],globalVar.screen)

    drawBlack(globalVar.objectPool[0])