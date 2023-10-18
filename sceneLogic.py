import loadingFunctions,sceneDraw,animator,globalVar,threading,button,pygame,inputSys

def beforeFirstLoadingLogic():
    if globalVar.sceneTimer == 0:
        loadingFunctions.firstLoadingSceneAssetLoad()
        globalVar.sceneTimer= globalVar.sceneTimer + 1
    elif loadingFunctions.testFirstLoadingSceneAssetLoad():
        globalVar.sceneTimer = 0
        globalVar.currentUpdateBlock = disclaimerLogic
        globalVar.currentDrawBlock = sceneDraw.disclaimerDraw
    else: globalVar.sceneTimer= globalVar.sceneTimer + 1

def disclaimerLogic():
    if globalVar.sceneTimer <= 30:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[2])
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[1])
    elif globalVar.sceneTimer < 360:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[2])
    elif globalVar.sceneTimer == 360:
        globalVar.objectPool[2][6][4] = 0
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[0])
    elif globalVar.sceneTimer >= 360 and globalVar.sceneTimer < 420:
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[0])
    elif globalVar.sceneTimer >= 420:
        globalVar.currentUpdateBlock = startScenenLogic 
        globalVar.currentDrawBlock = sceneDraw.drawBlack4Start
        globalVar.sceneTimer = -2
        
    globalVar.sceneTimer= globalVar.sceneTimer + 1

def startScenenLogic():
    if globalVar.sceneTimer == -1:
        globalVar.objectPool = []
        globalVar.animationPool = []
        globalVar.assetPool = []
        globalVar.imageThread = threading.Thread()
        loadingFunctions.startSceneAssetLoading()
        globalVar.currentDrawBlock = sceneDraw.startScenenDraw

    if globalVar.sceneTimer < 200 and globalVar.sceneTimer > 0:
        startSceneFIBlackSceneLogic()
        startSceneMusicLogic()
        startSceneFIDocAndExitTextLogic()
        startSceneFIConfigAndNewgameTextLogic()
        startSceneFIcontinueTextLogic()
        startSceneFIIntroTextLogic()
        startSceneFITitleLogic()
        startSceneFITitleShdwLogic()
        startSceneFICharCover12Logic()
        startSceneFICharCover34Logic()
        startSceneFICharCover5Logic()
        startScenePlsTextFlashInLogic()

    if globalVar.sceneTimer == 200:
        b_Document = button.Button("Document",(0,755),globalVar.screen)
        b_NewGame = button.Button("NewGame",(320,755),globalVar.screen)
        b_Continue = button.Button("Continue",(640,755),globalVar.screen)
        b_Config = button.Button("Config",(960,755),globalVar.screen)
        # b_Config.button = pygame.rect.Rect((b_Config.pos[0], b_Config.pos[1]), (130, 30))
        b_Exit = button.Button("Exit",(1280,755),globalVar.screen)
        globalVar.buttons = [b_Document, b_NewGame, b_Continue, b_Config, b_Exit]
        globalVar.subState = [None]*5
        globalVar.subState[0] = "flashIn"
        globalVar.subState[1] = 2
        globalVar.subState[2] = "unclicked"

    if globalVar.sceneTimer >= 200:
        selectSubInStartSceneStateMachine()
        
    globalVar.sceneTimer = globalVar.sceneTimer + 1

def startSceneFIBlackSceneLogic():
    if globalVar.sceneTimer < 120:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[0])
def startSceneFIDocAndExitTextLogic():
    if globalVar.sceneTimer >= 120 and globalVar.sceneTimer < 160 :
        animator.pointLinerAnimator(globalVar.objectPool[3],globalVar.animationPool[1])
        animator.pointLinerAnimator(globalVar.objectPool[4],globalVar.animationPool[1])
def startSceneFIConfigAndNewgameTextLogic():
    if globalVar.sceneTimer >= 100 and globalVar.sceneTimer < 140 :
        animator.pointLinerAnimator(globalVar.objectPool[5],globalVar.animationPool[1])
        animator.pointLinerAnimator(globalVar.objectPool[7],globalVar.animationPool[1])
def startSceneFIcontinueTextLogic():
    if globalVar.sceneTimer >= 80 and globalVar.sceneTimer < 120 :
        animator.pointLinerAnimator(globalVar.objectPool[6],globalVar.animationPool[1])
def startSceneFIIntroTextLogic():
    if globalVar.sceneTimer >= 80 and globalVar.sceneTimer < 160 :
        animator.pointLinerAnimator(globalVar.objectPool[8],globalVar.animationPool[3])
        animator.pointLinerAnimator(globalVar.objectPool[8],globalVar.animationPool[2])
def startSceneFITitleLogic():
    if globalVar.sceneTimer >= 20 and globalVar.sceneTimer < 100 :
        animator.pointLinerAnimator(globalVar.objectPool[9],globalVar.animationPool[4])
        animator.pointLinerAnimator(globalVar.objectPool[9],globalVar.animationPool[2])
def startSceneFITitleShdwLogic():
    if globalVar.sceneTimer >= 50 and globalVar.sceneTimer < 130 :
        animator.pointLinerAnimator(globalVar.objectPool[10],globalVar.animationPool[5])
        animator.pointLinerAnimator(globalVar.objectPool[10],globalVar.animationPool[2])
def startSceneFICharCover12Logic():
    if globalVar.sceneTimer >= 130 and globalVar.sceneTimer < 190 :
        animator.pointLinerAnimator(globalVar.objectPool[11],globalVar.animationPool[6])
        animator.pointLinerAnimator(globalVar.objectPool[12],globalVar.animationPool[6])
def startSceneFICharCover34Logic():
    if globalVar.sceneTimer >= 110 and globalVar.sceneTimer < 170 :
        animator.pointLinerAnimator(globalVar.objectPool[13],globalVar.animationPool[6])
        animator.pointLinerAnimator(globalVar.objectPool[14],globalVar.animationPool[6])
def startSceneFICharCover5Logic():
    if globalVar.sceneTimer >= 90 and globalVar.sceneTimer < 150 :
        animator.pointLinerAnimator(globalVar.objectPool[15],globalVar.animationPool[6])
def startScenePlsTextFlashInLogic():
    if globalVar.sceneTimer >= 130 and globalVar.sceneTimer < 190 :
        animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[7])
def startSceneMusicLogic():
    if globalVar.sceneTimer == 22:
        pygame.mixer.music.load('asset/bgm/StartBGM.wav')
        pygame.mixer.music.play()

def selectSubInStartSceneStateMachine():
    match globalVar.subState[0]:
        case "static":
            for i in range(0,5):
                if globalVar.buttons[i].check_collided() and globalVar.subState[1] != i: 
                    globalVar.subState[0] = "flashOut"
                    globalVar.subState[1] = i
                    globalVar.objectPool[1][4] = 255
                    globalVar.objectPool[1][6][4] = 0
            if globalVar.inputSystem["commandState"][10] == "Pressing" and globalVar.buttons[1].check_collided():
                globalVar.subState[0] = "clickedFlashIn"
                globalVar.objectPool[1][4] = 1
                globalVar.objectPool[1][0] = globalVar.ssv[0][globalVar.subState[1]]
                globalVar.objectPool[1][6][4] = 0
                for i in range(0,54):
                    globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                    globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                globalVar.sceneTimer = 299
        case "flashOut":
            animator.pointLinerAnimator(globalVar.objectPool[1],globalVar.animationPool[19])
            if globalVar.objectPool[1][6][4] >= globalVar.animationPool[19]["length"]:
                globalVar.subState[0] = "flashIn"
                globalVar.objectPool[1][4] = 0
                globalVar.objectPool[1][0] = globalVar.ssv[0][globalVar.subState[1]]
                globalVar.objectPool[1][6][4] = 0
            for i in range(0,5):
                if globalVar.buttons[i].check_collided() and globalVar.subState[1] != i: 
                    globalVar.subState[1] = i
            if globalVar.inputSystem["commandState"][10] == "Pressing" and globalVar.buttons[1].check_collided():
                globalVar.subState[0] = "clickedFlashIn"
                globalVar.objectPool[1][4] = 1
                globalVar.objectPool[1][0] = globalVar.ssv[0][globalVar.subState[1]]
                globalVar.objectPool[1][6][4] = 0
                for i in range(0,54):
                    globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                    globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                globalVar.sceneTimer = 299
        case "flashIn":
            animator.pointLinerAnimator(globalVar.objectPool[1],globalVar.animationPool[18])
            if globalVar.objectPool[1][6][4] >= globalVar.animationPool[18]["length"]:
                globalVar.subState[0] == "static"
                globalVar.objectPool[1][4] = 255
            for i in range(0,5):
                if globalVar.buttons[i].check_collided() and globalVar.subState[1] != i: 
                    globalVar.subState[0] = "flashOut"
                    globalVar.subState[1] = i
                    globalVar.objectPool[1][4] = 255
                    globalVar.objectPool[1][6][4] = 0
            if globalVar.inputSystem["commandState"][10] == "Pressing" and globalVar.buttons[1].check_collided():
                globalVar.subState[0] = "clickedFlashIn"
                globalVar.objectPool[1][4] = 1
                globalVar.objectPool[1][0] = globalVar.ssv[0][globalVar.subState[1]]
                globalVar.objectPool[1][6][4] = 0
                for i in range(0,54):
                    globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                    globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                globalVar.sceneTimer = 299
        case "clickedFlashIn":
            if globalVar.sceneTimer < 315:
                for i in range(3,11):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[20])
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[21])
                animator.pointLinerAnimator(globalVar.objectPool[11],globalVar.animationPool[23])
                animator.pointLinerAnimator(globalVar.objectPool[12],globalVar.animationPool[23])
                animator.pointLinerAnimator(globalVar.objectPool[13],globalVar.animationPool[24])
                animator.pointLinerAnimator(globalVar.objectPool[14],globalVar.animationPool[24])
                animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[20])
                animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[21])
                animator.pointLinerAnimator(globalVar.objectPool[53],globalVar.animationPool[22])
                animator.pointLinerAnimator(globalVar.objectPool[20],globalVar.animationPool[25])
            if globalVar.sceneTimer == 315:
                for i in range(0,54):
                    globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                    globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                for i in range(46,53):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[7])
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[7])
                animator.pointLinerAnimator(globalVar.objectPool[27],globalVar.animationPool[7])
                animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[7])
                globalVar.objectPool[34][5] = 1
            if globalVar.sceneTimer > 315 and globalVar.sceneTimer < 335:
                for i in range(46,53):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[7])
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[7])
                animator.pointLinerAnimator(globalVar.objectPool[27],globalVar.animationPool[7])
                animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[7])

            if globalVar.sceneTimer > 335:
                if globalVar.inputSystem["commandState"][6] == "Pressing":
                    globalVar.subState[0] = "customFlashIn"
                    globalVar.objectPool[34][5] = 0
                    for i in range(0,54):
                        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                        globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                    globalVar.sceneTimer = 299
        case "customFlashIn":
            if globalVar.sceneTimer < 340:
                for i in range(28,45):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[8])
            if globalVar.sceneTimer >= 340:
                if globalVar.inputSystem["commandState"][6] == "Pressing":
                    globalVar.subState[0] = "mapFlashIn"
                    for i in range(0,54):
                        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                        globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                    globalVar.sceneTimer = 299
        case "mapFlashIn":
            if globalVar.sceneTimer < 340:
                for i in range(28,45):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[8])
            if globalVar.sceneTimer >= 340:
                if globalVar.inputSystem["commandState"][6] == "Pressing":
                    globalVar.subState[0] = "mapFlashIn"
                    for i in range(0,54):
                        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                        globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                    globalVar.sceneTimer = 299