import pygame

def drawBlack(drawArguPack):
    screen = drawArguPack[0]
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(1600, 900, 0, 0))

def drawOneImageObject(frame,object,screen):
    x = object[0]
    y = object[1]
    rota_frame = pygame.transform.rotate(frame,object[3])
    rota_frame.set_alpha(object[4])
    screen.blit(rota_frame, (x, y))

def drawArrayImageObject(frames,object,screen):
    x = object[0]
    y = object[1]
    frameNum = object[5]
    rota_frame = pygame.transform.rotate(frames[frameNum],object[3])
    rota_frame.set_alpha(object[4])
    screen.blit(rota_frame, (x, y))

def firstLoadingDraw(drawArguPack):
    assetPool = drawArguPack[2]
    objectPool = drawArguPack[1]
    screen = drawArguPack[0]

    # objectPool[0] = [764,388,1,15,255,0,None,None]
    # objectPool[1] = [860,394,1,87,255,0,None,None]
    # objectPool[2] = [870,495,1,159,255,0,None,None]
    # objectPool[3] = [783,543,1,231,255,0,None,None]
    # objectPool[4] = [707,467,1,303,255,0,None,None]
    # objectPool[5] = [754,380,1,15,255,0,None,None]
    # objectPool[6] = [863,406,1,95,255,0,None,None]
    # objectPool[7] = [90,540,1,0,255,0,None,None]
    # objectPool[8] = [0,0,1,0,255,0,None,None]

    #     imagePathArray.append('asset/loadingScene/loadTextFile.png')
    # for i in range(0,30):
    #     imagePathArray.append('asset/loadingScene/loadingAnimationAsset/'+str(i)+'.png')
    # for image_path in imagePathArray:
    #     thread = threading.Thread(target=lambda p=image_path: assetPool.append(load_image(p)))
    #     imageThread.append(thread)
    #     thread.start()

    drawArrayImageObject(assetPool[1:31],objectPool[0],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[1],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[2],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[3],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[4],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[5],screen)
    drawArrayImageObject(assetPool[1:31],objectPool[6],screen)
    drawOneImageObject(assetPool[0],objectPool[7],screen)

    screen.blit(assetPool[2], (objectPool[7][0], objectPool[7][1]))

    # s = pygame.Surface((1600,900))
    # s.set_alpha(drawArguPack[1][8][4])
    # s.fill((0,0,0))
    # drawArguPack[0].blit(s, (0, 0))