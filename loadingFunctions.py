import threading,pygame

def load_image(image_path):
    return pygame.image.load(image_path)

def firstLoadingSceneAssetLoad(assetPool,imageThread,objectPool,animationPool):
    imagePathArray = []
    imageThread = []
    imagePathArray.append('asset/loadingScene/loadTextFile.png')
    for i in range(0,30):
        imagePathArray.append('asset/loadingScene/loadingAnimationAsset/'+str(i)+'.png')
    for image_path in imagePathArray:
        thread = threading.Thread(target=lambda p=image_path: assetPool.append(load_image(p)))
        imageThread.append(thread)
        thread.start()

    objectPool[0] = [764,388,1,15,255,0,None,None]
    objectPool[1] = [860,394,1,87,255,0,None,None]
    objectPool[2] = [870,495,1,159,255,0,None,None]
    objectPool[3] = [783,543,1,231,255,0,None,None]
    objectPool[4] = [707,467,1,303,255,0,None,None]
    objectPool[5] = [754,380,1,15,255,0,None,None]
    objectPool[6] = [863,406,1,95,255,0,None,None]
    objectPool[7] = [90,540,1,0,255,0,None,None]
    objectPool[8] = [0,0,1,0,255,0,None,None]

    for i in range(0,9):
        objectPool[i][6] = [0,0,0,0,0,0]
        objectPool[i][7] = [0,0,0,0,0,0]
        
    textFlashInAnim = {}
    textFlashInAnim[0] = [0,13]
    textFlashInAnim[13] = [225*0.85,30]
    textFlashInAnim[30] = [225,0]
    textFlashInAnim["prpty"] = 4
    textFlashInAnim["length"] = 30
    textFlashInAnim["loopType"] = "const"

    textFlashOutAnim = {}
    textFlashOutAnim[0] = [225,13]
    textFlashOutAnim[13] = [225*0.85,30]
    textFlashOutAnim[30] = [0,0]
    textFlashOutAnim["prpty"] = 4
    textFlashOutAnim["length"] = 30
    textFlashOutAnim["loopType"] = "const"

    loadingIconAnim = {}
    loadingIconAnim[0] = [0,30]
    loadingIconAnim[30] = [30,90]
    loadingIconAnim[90] = [30,0]
    loadingIconAnim["prpty"] = 5
    loadingIconAnim["length"] = 90
    loadingIconAnim["loopType"] = "loop"

    animationPool[0] = textFlashInAnim
    animationPool[1] = textFlashOutAnim
    animationPool[2] = loadingIconAnim

def testFirstLoadingSceneAssetLoad(imageThread):
    # Check if all image loading threads are done
    if all(not thread.is_alive() for thread in imageThread):
        return True