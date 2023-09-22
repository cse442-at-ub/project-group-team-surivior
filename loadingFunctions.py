import threading,pygame,globalVar


def load_image(image_path):
    for i in range(0,len(image_path)):
        globalVar.assetPool[i] = pygame.image.load(image_path[i])

def firstLoadingSceneAssetLoad():
    imagePathArray = []
    imagePathArray.append('asset/disclaimerScene/loadTextFile.png')
    for i in range(0,60):
        imagePathArray.append('asset/disclaimerScene/loadingAnimationAsset/'+str(i)+'.png')

    globalVar.assetPool = [None]*61
    pygame.mixer.music.load('asset/disclaimerScene/disclaimer.wav')
    pygame.mixer.music.play(1)
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
    textFlashInAnim[13] = [255*0.85,30]
    textFlashInAnim[30] = [255,0]
    textFlashInAnim["prpty"] = 4
    textFlashInAnim["length"] = 30
    textFlashInAnim["loopType"] = "const"

    textFlashOutAnim = {}
    textFlashOutAnim[0] = [255,13]
    textFlashOutAnim[13] = [255*0.85,30]
    textFlashOutAnim[30] = [0,0]
    textFlashOutAnim["prpty"] = 4
    textFlashOutAnim["length"] = 30
    textFlashOutAnim["loopType"] = "const"

    loadingIconAnim = {}
    loadingIconAnim[0] = [0,59]
    loadingIconAnim[59] = [59,179]
    loadingIconAnim[179] = [59,180]
    loadingIconAnim[180] = [0,0]

    # loadingIconAnim[0] = [0,59]
    # loadingIconAnim[59] = [59,60]
    # loadingIconAnim[60] = [0,0]

    loadingIconAnim["prpty"] = 5
    loadingIconAnim["length"] = 180
    loadingIconAnim["loopType"] = "loop"

    globalVar.animationPool = [None]*3

    globalVar.animationPool[0] = textFlashInAnim
    globalVar.animationPool[1] = textFlashOutAnim
    globalVar.animationPool[2] = loadingIconAnim

def startSceneAssetLoading():
    imagePathArray = []
    imagePathArray.append('asset/startScene/configText.png') #0
    imagePathArray.append('asset/startScene/continueText.png') #1
    imagePathArray.append('asset/startScene/documentText.png') #2
    imagePathArray.append('asset/startScene/exitText.png') #3
    imagePathArray.append('asset/startScene/introText.png') #4
    imagePathArray.append('asset/startScene/lowTrigMark.png') #5
    imagePathArray.append('asset/startScene/mouse.png') #6
    imagePathArray.append('asset/startScene/newGameText.png') #7
    imagePathArray.append('asset/startScene/shutters.png') #8
    imagePathArray.append('asset/startScene/titleText.png') #9
    for i in range(0,5):
        imagePathArray.append('asset/startScene/'+str(i)+'pix.png')
    imagePathArray.append('asset/startScene/blocker.png')
    imagePathArray.append('asset/startScene/titleTextRed.png')

    globalVar.assetPool = [None]*17
    # pygame.mixer.music.load('asset/disclaimerScene/disclaimer.wav')
    # pygame.mixer.music.play(1)
    for i in range(0,len(imagePathArray)):
        globalVar.assetPool[i] = pygame.image.load(imagePathArray[i])
        globalVar.assetPool[i] = pygame.Surface.convert_alpha(globalVar.assetPool[i]) 

    globalVar.objectPool = [None]*27

    globalVar.objectPool[0] = [0,0,1,0,255,0,None,None] #black screen
    globalVar.objectPool[1] = [795,835,1,0,0,0,None,None] #lowTrig
    globalVar.objectPool[2] = [0,0,1,0,0,0,None,None] #mouse
    globalVar.objectPool[3] = [72,800,1,0,0,0,None,None] #documentText
    globalVar.objectPool[4] = [1352,800,1,0,0,0,None,None] #exitText
    globalVar.objectPool[5] = [1060,800,1,0,0,0,None,None] #configText
    globalVar.objectPool[6] = [725,800,1,0,0,0,None,None] #continueText
    globalVar.objectPool[7] = [400,800,1,0,0,0,None,None] #newGameText
    globalVar.objectPool[8] = [610,610,1,0,0,0,None,None] #introText
    globalVar.objectPool[9] = [395,455,1,0,0,0,None,None] #titleText
    globalVar.objectPool[10] = [395,465,1,0,0,0,None,None] #titleTextShodw
    globalVar.objectPool[11] = [0,0,1,0,255,0,None,None] #CharCover 1
    globalVar.objectPool[12] = [1280,0,1,0,255,0,None,None] #CharCover 2
    globalVar.objectPool[13] = [320,0,1,0,255,0,None,None] #CharCover 3
    globalVar.objectPool[14] = [960,0,1,0,255,0,None,None] #CharCover 4
    globalVar.objectPool[15] = [640,0,1,0,255,0,None,None] #CharCover 5
    globalVar.objectPool[16] = [0,0,1,0,255,0,None,None] #CharShutter 1
    globalVar.objectPool[17] = [320,0,1,0,255,0,None,None] #CharShutter 2
    globalVar.objectPool[18] = [1280,0,1,0,255,0,None,None] #CharShutter 3
    globalVar.objectPool[19] = [960,0,1,0,255,0,None,None] #CharShutter 4
    globalVar.objectPool[20] = [640,0,1,0,255,0,None,None] #CharShutter 5
    globalVar.objectPool[21] = [640,150,1,0,255,0,None,None] #Char1
    globalVar.objectPool[22] = [960,150,1,0,255,0,None,None] #Char2
    globalVar.objectPool[23] = [1280,150,1,0,255,0,None,None] #Char3
    globalVar.objectPool[24] = [0,150,1,0,255,0,None,None] #Char4
    globalVar.objectPool[25] = [320,150,1,0,255,0,None,None] #Char5
    globalVar.objectPool[26] = [0,0,1,0,255,0,None,None] #BlockLineBTWChar

    for i in range(0,26):
        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
        globalVar.objectPool[i][7] = [0,0,0,0,0,0]

    backScreenFlashInAnim = {}
    backScreenFlashInAnim[0] = [255,20]
    backScreenFlashInAnim[20] = [225*0.43,40]
    backScreenFlashInAnim[40] = [225*0.21,60]
    backScreenFlashInAnim[60] = [225*0.11,120]
    backScreenFlashInAnim[120] = [0,0]
    backScreenFlashInAnim["prpty"] = 4
    backScreenFlashInAnim["length"] = 120
    backScreenFlashInAnim["loopType"] = "const"

    selectionFlashInAnim = {}
    selectionFlashInAnim[0] = [0,5]
    selectionFlashInAnim[5] = [225*0.48,10]
    selectionFlashInAnim[10] = [225*0.68,20]
    selectionFlashInAnim[20] = [225*0.89,30]
    selectionFlashInAnim[30] = [225*0.98,40]
    selectionFlashInAnim[40] = [225,0]
    selectionFlashInAnim["prpty"] = 4
    selectionFlashInAnim["length"] = 40
    selectionFlashInAnim["loopType"] = "const"

    titleAndSubTransFlashInAnim = {}
    titleAndSubTransFlashInAnim[0] = [0,5]
    titleAndSubTransFlashInAnim[5] = [225*0.30,15]
    titleAndSubTransFlashInAnim[15] = [225*0.59,25]
    titleAndSubTransFlashInAnim[25] = [225*0.75,35]
    titleAndSubTransFlashInAnim[35] = [225*0.85,50]
    titleAndSubTransFlashInAnim[50] = [225*0.94,80]
    titleAndSubTransFlashInAnim[80] = [225,0]
    titleAndSubTransFlashInAnim["prpty"] = 4
    titleAndSubTransFlashInAnim["length"] = 80
    titleAndSubTransFlashInAnim["loopType"] = "const"

    subYmoveFlashInAnim = {}
    subYmoveFlashInAnim[0] = [610,5]
    subYmoveFlashInAnim[5] = [620,15]
    subYmoveFlashInAnim[15] = [629,25]
    subYmoveFlashInAnim[25] = [633,35]
    subYmoveFlashInAnim[35] = [636,50]
    subYmoveFlashInAnim[50] = [638,80]
    subYmoveFlashInAnim[80] = [640,0]
    subYmoveFlashInAnim["prpty"] = 1
    subYmoveFlashInAnim["length"] = 80
    subYmoveFlashInAnim["loopType"] = "const"

    titleYmoveFlashInAnim = {}
    titleYmoveFlashInAnim[0] = [455,2]
    titleYmoveFlashInAnim[2] = [458,5]
    titleYmoveFlashInAnim[5] = [459,15]
    titleYmoveFlashInAnim[15] = [462,25]
    titleYmoveFlashInAnim[25] = [463,35]
    titleYmoveFlashInAnim[35] = [464,50]
    titleYmoveFlashInAnim[50] = [464.5,80]
    titleYmoveFlashInAnim[80] = [465,0]
    titleYmoveFlashInAnim["prpty"] = 1
    titleYmoveFlashInAnim["length"] = 80
    titleYmoveFlashInAnim["loopType"] = "const"

    titleShadwYmoveFlashInAnim = {}
    titleShadwYmoveFlashInAnim[0] = [465,2]
    titleShadwYmoveFlashInAnim[2] = [468,5]
    titleShadwYmoveFlashInAnim[5] = [469,15]
    titleShadwYmoveFlashInAnim[15] = [472,25]
    titleShadwYmoveFlashInAnim[25] = [473,35]
    titleShadwYmoveFlashInAnim[35] = [474,50]
    titleShadwYmoveFlashInAnim[50] = [474.5,80]
    titleShadwYmoveFlashInAnim[80] = [475,0]
    titleShadwYmoveFlashInAnim["prpty"] = 1
    titleShadwYmoveFlashInAnim["length"] = 80
    titleShadwYmoveFlashInAnim["loopType"] = "const"

    charCoverFlashOutAnim = {}
    charCoverFlashOutAnim[0] = [225,7]
    charCoverFlashOutAnim[7] = [225*0.96,15]
    charCoverFlashOutAnim[15] = [225*0.84,30]
    charCoverFlashOutAnim[30] = [225*0.5,45]
    charCoverFlashOutAnim[45] = [225*0.16,53]
    charCoverFlashOutAnim[53] = [225*0.04,60]
    charCoverFlashOutAnim[60] = [0,0]
    charCoverFlashOutAnim["prpty"] = 4
    charCoverFlashOutAnim["length"] = 60
    charCoverFlashOutAnim["loopType"] = "const"

    globalVar.animationPool = [None]*7

    globalVar.animationPool[0] = backScreenFlashInAnim
    globalVar.animationPool[1] = selectionFlashInAnim
    globalVar.animationPool[2] = titleAndSubTransFlashInAnim
    globalVar.animationPool[3] = subYmoveFlashInAnim
    globalVar.animationPool[4] = titleYmoveFlashInAnim
    globalVar.animationPool[5] = titleShadwYmoveFlashInAnim
    globalVar.animationPool[6] = charCoverFlashOutAnim

def testFirstLoadingSceneAssetLoad():
    # Check if all image loading threads are done
    if not globalVar.imageThread.is_alive():
        return True