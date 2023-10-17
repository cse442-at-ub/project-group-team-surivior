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

    imagePathArray.append('asset/startScene/BPISText.png') #17
    imagePathArray.append('asset/startScene/drBladImage.png') #18
    imagePathArray.append('asset/startScene/drBladText.png') #19
    imagePathArray.append('asset/startScene/eRightMark.png') #20
    imagePathArray.append('asset/startScene/grayBox.png') #21
    imagePathArray.append('asset/startScene/horiBlock.png') #22
    imagePathArray.append('asset/startScene/ltKeystoneImage.png') #23
    imagePathArray.append('asset/startScene/ltKeystoneText.png') #24
    imagePathArray.append('asset/startScene/plsText.png') #25
    imagePathArray.append('asset/startScene/prRuneImage.png') #26
    imagePathArray.append('asset/startScene/prRuneText.png') #27
    imagePathArray.append('asset/startScene/qLeftMark.png') #28
    imagePathArray.append('asset/startScene/sDownMark.png') #29
    imagePathArray.append('asset/startScene/vertBlock.png') #30
    imagePathArray.append('asset/startScene/wUpperMark.png') #31
    imagePathArray.append('asset/startScene/blackEdge.png') #32
    imagePathArray.append('asset/startScene/lock.png') #33
    imagePathArray.append('asset/startScene/charShdw.png') #34
    imagePathArray.append('asset/startScene/yssoText.png') #35
    imagePathArray.append('asset/startScene/fConfirmText.png') #36

    for i in range(0,9):
        imagePathArray.append('asset/startScene/CharFrame/ys/'+str(i)+'.png') #44

    globalVar.assetPool = [None]*45
    # pygame.mixer.music.load('asset/disclaimerScene/disclaimer.wav')
    # pygame.mixer.music.play(1)
    for i in range(0,len(imagePathArray)):
        globalVar.assetPool[i] = pygame.image.load(imagePathArray[i])
        globalVar.assetPool[i] = pygame.Surface.convert_alpha(globalVar.assetPool[i]) 

    globalVar.objectPool = [None]*45

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

    globalVar.objectPool[27] = [770,600,1,0,0,0,None,None] #charIdle
    globalVar.objectPool[28] = [1173,480,1,0,0,0,None,None] #BPISText
    globalVar.objectPool[29] = [1128,445,1,0,0,0,None,None] #grayBox1
    globalVar.objectPool[30] = [1173,235,1,0,0,0,None,None] #DRISText
    globalVar.objectPool[31] = [1128,200,1,0,0,0,None,None] #grayBox2
    globalVar.objectPool[32] = [457,626,1,0,0,0,None,None] #sDownMark
    globalVar.objectPool[33] = [457,533,1,0,0,0,None,None] #wUpperMark
    globalVar.objectPool[34] = [110,90,1,0,0,0,None,None] #plsText
    globalVar.objectPool[35] = [270,575,1,0,0,0,None,None] #eRightMark
    globalVar.objectPool[36] = [104,575,1,0,0,0,None,None] #qLeftMark
    globalVar.objectPool[37] = [166,214,1,0,0,0,None,None] #prRuneImage
    globalVar.objectPool[38] = [169,295,1,0,0,0,None,None] #prRuneText
    globalVar.objectPool[39] = [152,630,1,0,0,0,None,None] #drBladText
    globalVar.objectPool[40] = [154,463,1,0,0,0,None,None] #ltKeystoneText
    globalVar.objectPool[41] = [165,543,1,0,0,0,None,None] #drBladImage
    globalVar.objectPool[42] = [157,368,1,0,0,0,None,None] #ltKeystoneImage
    globalVar.objectPool[43] = [-17,530,1,0,0,0,None,None] #horiBlock
    globalVar.objectPool[44] = [125,180,1,0,0,0,None,None] #vertBlock

    globalVar.objectPool[45] = [0,0,1,0,0,0,None,None] #map

    globalVar.objectPool[46] = [750,408,1,0,0,0,None,None] #charShdw
    globalVar.objectPool[47] = [132,408,1,0,0,0,None,None] #lock1
    globalVar.objectPool[48] = [452,408,1,0,0,0,None,None] #lock2
    globalVar.objectPool[49] = [1097,408,1,0,0,0,None,None] #lock3
    globalVar.objectPool[50] = [1414,408,1,0,0,0,None,None] #lock4

    globalVar.objectPool[51] = [762,783,1,0,0,0,None,None] #charNameText
    globalVar.objectPool[52] = [1370,830,1,0,0,0,None,None] #fConfirm

    for i in range(0,53):
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

    charFlashInAnim = {}
    charFlashInAnim[0] = [0,5]
    charFlashInAnim[5] = [225*0.16,10]
    charFlashInAnim[10] = [225*0.5,15]
    charFlashInAnim[15] = [225*0.84,20]
    charFlashInAnim[20] = [225*1,0]
    charFlashInAnim["prpty"] = 4
    charFlashInAnim["length"] = 20
    charFlashInAnim["loopType"] = "const"

    customMenuFlashInAnim = {}
    customMenuFlashInAnim[0] = [0,10]
    customMenuFlashInAnim[10] = [225*0.27,20]
    customMenuFlashInAnim[20] = [225*0.63,30]
    customMenuFlashInAnim[30] = [225*0.90,40]
    customMenuFlashInAnim[40] = [225*1,0]
    customMenuFlashInAnim["prpty"] = 4
    customMenuFlashInAnim["length"] = 40
    customMenuFlashInAnim["loopType"] = "const"

    customMenuFlashOutTransAnim = {}
    customMenuFlashOutTransAnim[0] = [1,5]
    customMenuFlashOutTransAnim[5] = [225*0.74,15]
    customMenuFlashOutTransAnim[15] = [225*0.63,35]
    customMenuFlashOutTransAnim[35] = [225*0.90,55]
    customMenuFlashOutTransAnim[55] = [225*1,75]
    customMenuFlashOutTransAnim[75] = [225*1,100]
    customMenuFlashOutTransAnim[100] = [225*1,120]
    customMenuFlashOutTransAnim[120] = [225*1,0]
    customMenuFlashOutTransAnim["prpty"] = 4
    customMenuFlashOutTransAnim["length"] = 120
    customMenuFlashOutTransAnim["loopType"] = "const"

    customMenuFlashOutYAnim = {}
    customMenuFlashOutYAnim[0] = [445,120]
    customMenuFlashOutYAnim[120] = [535,0]
    customMenuFlashOutYAnim["prpty"] = 2
    customMenuFlashOutYAnim["length"] = 120
    customMenuFlashOutYAnim["loopType"] = "const"

    charPixfadeAnim1 = {}
    charPixfadeAnim1[0] = [255*0.75,5]
    charPixfadeAnim1[5] = [255*1,10]
    charPixfadeAnim1[10] = [255*1,0]
    charPixfadeAnim1["prpty"] = 4
    charPixfadeAnim1["length"] = 10
    charPixfadeAnim1["loopType"] = "const"

    charPixfadeAnim2 = {}
    charPixfadeAnim2[0] = [255*0.25,5]
    charPixfadeAnim2[5] = [255*0.75,10]
    charPixfadeAnim2[10] = [255*1,0]
    charPixfadeAnim2["prpty"] = 4
    charPixfadeAnim2["length"] = 10
    charPixfadeAnim2["loopType"] = "const"

    charPixfadeAnim3 = {}
    charPixfadeAnim3[0] = [255*0,5]
    charPixfadeAnim3[5] = [255*0,10]
    charPixfadeAnim3[10] = [255*1,0]
    charPixfadeAnim3["prpty"] = 4
    charPixfadeAnim3["length"] = 10
    charPixfadeAnim3["loopType"] = "const"

    charNameFadeAnim = {}
    charNameFadeAnim[0] = [255,20]
    charNameFadeAnim[20] = [255*0.2,40]
    charNameFadeAnim[40] = [0,0]
    charNameFadeAnim["prpty"] = 4
    charNameFadeAnim["length"] = 40
    charNameFadeAnim["loopType"] = "const"

    charMoveInYAnim = {}
    charMoveInYAnim[0] = [600,25]
    charMoveInYAnim[25] = [580,50]
    charMoveInYAnim[50] = [536,75]
    charMoveInYAnim[75] = [483,100]
    charMoveInYAnim[100] = [442,120]
    charMoveInYAnim[120] = [430,0]
    charMoveInYAnim["prpty"] = 2
    charMoveInYAnim["length"] = 120
    charMoveInYAnim["loopType"] = "const"

    mapMoveInYAnim = {}
    mapMoveInYAnim[0] = [105,25]
    mapMoveInYAnim[25] = [120,50]
    mapMoveInYAnim[50] = [156,75]
    mapMoveInYAnim[75] = [197,100]
    mapMoveInYAnim[100] = [230,120]
    mapMoveInYAnim[120] = [240,0]
    mapMoveInYAnim["prpty"] = 2
    mapMoveInYAnim["length"] = 120
    mapMoveInYAnim["loopType"] = "const"

    mapFlashInAnim = {}
    mapFlashInAnim[0] = [0,25]
    mapFlashInAnim[25] = [11,50]
    mapFlashInAnim[50] = [38,75]
    mapFlashInAnim[75] = [68,100]
    mapFlashInAnim[100] = [93,120]
    mapFlashInAnim[120] = [100,0]
    mapFlashInAnim["prpty"] = 4
    mapFlashInAnim["length"] = 120
    mapFlashInAnim["loopType"] = "const"

    globalVar.animationPool = [None]*7

    globalVar.animationPool[0] = backScreenFlashInAnim
    globalVar.animationPool[1] = selectionFlashInAnim
    globalVar.animationPool[2] = titleAndSubTransFlashInAnim
    globalVar.animationPool[3] = subYmoveFlashInAnim
    globalVar.animationPool[4] = titleYmoveFlashInAnim
    globalVar.animationPool[5] = titleShadwYmoveFlashInAnim
    globalVar.animationPool[6] = charCoverFlashOutAnim

    globalVar.animationPool[7] = charFlashInAnim
    globalVar.animationPool[8] = customMenuFlashInAnim
    globalVar.animationPool[9] = customMenuFlashOutTransAnim
    globalVar.animationPool[10] = customMenuFlashOutYAnim
    globalVar.animationPool[11] = charPixfadeAnim1
    globalVar.animationPool[12] = charPixfadeAnim2
    globalVar.animationPool[13] = charPixfadeAnim3
    globalVar.animationPool[14] = charNameFadeAnim
    globalVar.animationPool[15] = charMoveInYAnim
    globalVar.animationPool[16] = mapMoveInYAnim
    globalVar.animationPool[17] = mapFlashInAnim

def testFirstLoadingSceneAssetLoad():
    # Check if all image loading threads are done
    if not globalVar.imageThread.is_alive():
        return True