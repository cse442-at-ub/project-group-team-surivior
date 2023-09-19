import threading,pygame,globalVar


def load_image(image_path):
    for i in range(0,len(image_path)):
        globalVar.assetPool[i] = pygame.image.load(image_path[i])

def firstLoadingSceneAssetLoad():
    imagePathArray = []
    imagePathArray.append('asset/loadingScene/loadTextFile.png')
    for i in range(0,60):
        imagePathArray.append('asset/loadingScene/loadingAnimationAsset/'+str(i)+'.png')

    globalVar.assetPool = [None]*61
    for i in range(0,len(imagePathArray)):
        globalVar.assetPool[i] = pygame.image.load(imagePathArray[i])
        globalVar.assetPool[i] = pygame.Surface.convert_alpha(globalVar.assetPool[i]) 
    globalVar.objectPool = [None]*3

    globalVar.objectPool[0] = [700,350,1,15,255,0,None,None]
    globalVar.objectPool[1] = [90,540,1,0,255,0,None,None]
    globalVar.objectPool[2] = [0,0,1,0,255,0,None,None]

    for i in range(0,3):
        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
        globalVar.objectPool[i][7] = [0,0,0,0,0,0]
        
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
    loadingIconAnim[0] = [0,59]
    loadingIconAnim[59] = [59,178]
    loadingIconAnim[178] = [59,179]
    loadingIconAnim[179] = [0,0]
    loadingIconAnim["prpty"] = 5
    loadingIconAnim["length"] = 180
    loadingIconAnim["loopType"] = "loop"

    globalVar.animationPool = [None]*3

    globalVar.animationPool[0] = textFlashInAnim
    globalVar.animationPool[1] = textFlashOutAnim
    globalVar.animationPool[2] = loadingIconAnim

def testFirstLoadingSceneAssetLoad():
    # Check if all image loading threads are done
    if not globalVar.imageThread.is_alive():
        return True