import loadingFunctions,sceneDraw,animator,globalVar,threading,pygame,button,mouse_movement

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
        stratSceneMusicLogic()
        stratSceneFIDocAndExitTextLogic()
        stratSceneFIConfigAndNewgameTextLogic()
        stratSceneFIcontinueTextLogic()
        stratSceneFIIntroTextLogic()
        stratSceneFITitleLogic()
        stratSceneFITitleShdwLogic()
        stratSceneFICharCover12Logic()
        stratSceneFICharCover34Logic()
        stratSceneFICharCover5Logic()
    if globalVar.sceneTimer == 200:
        b_Document = button.Button("Document",(69,795),globalVar.screen)
        b_NewGame = button.Button("NewGame",(396,795),globalVar.screen)
        b_Continue = button.Button("Continue",(716,795),globalVar.screen)
        b_Config = button.Button("Config",(1052,795),globalVar.screen)
        b_Config.button = pygame.rect.Rect((b_Config.pos[0], b_Config.pos[1]), (130, 30))
        b_Exit = button.Button("Exit",(1348,795),globalVar.screen)
        globalVar.buttons = [b_Document, b_NewGame, b_Continue, b_Config, b_Exit]
        
    if globalVar.sceneTimer > 200:
        if globalVar.buttons[1].check_clicked(): #b_NewGame
            globalVar.currentUpdateBlock = mouse_movement.game()
        if globalVar.buttons[4].check_clicked(): #b_Exit
            pygame.quit()
        
        
    globalVar.sceneTimer = globalVar.sceneTimer + 1

def startSceneFIBlackSceneLogic():
    if globalVar.sceneTimer < 120:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[0])
def stratSceneFIDocAndExitTextLogic():
    if globalVar.sceneTimer >= 120 and globalVar.sceneTimer < 160 :
        animator.pointLinerAnimator(globalVar.objectPool[3],globalVar.animationPool[1])
        animator.pointLinerAnimator(globalVar.objectPool[4],globalVar.animationPool[1])
def stratSceneFIConfigAndNewgameTextLogic():
    if globalVar.sceneTimer >= 100 and globalVar.sceneTimer < 140 :
        animator.pointLinerAnimator(globalVar.objectPool[5],globalVar.animationPool[1])
        animator.pointLinerAnimator(globalVar.objectPool[7],globalVar.animationPool[1])
def stratSceneFIcontinueTextLogic():
    if globalVar.sceneTimer >= 80 and globalVar.sceneTimer < 120 :
        animator.pointLinerAnimator(globalVar.objectPool[6],globalVar.animationPool[1])
def stratSceneFIIntroTextLogic():
    if globalVar.sceneTimer >= 80 and globalVar.sceneTimer < 160 :
        animator.pointLinerAnimator(globalVar.objectPool[8],globalVar.animationPool[3])
        animator.pointLinerAnimator(globalVar.objectPool[8],globalVar.animationPool[2])
def stratSceneFITitleLogic():
    if globalVar.sceneTimer >= 20 and globalVar.sceneTimer < 100 :
        animator.pointLinerAnimator(globalVar.objectPool[9],globalVar.animationPool[4])
        animator.pointLinerAnimator(globalVar.objectPool[9],globalVar.animationPool[2])
def stratSceneFITitleShdwLogic():
    if globalVar.sceneTimer >= 50 and globalVar.sceneTimer < 130 :
        animator.pointLinerAnimator(globalVar.objectPool[10],globalVar.animationPool[5])
        animator.pointLinerAnimator(globalVar.objectPool[10],globalVar.animationPool[2])
def stratSceneFICharCover12Logic():
    if globalVar.sceneTimer >= 130 and globalVar.sceneTimer < 190 :
        animator.pointLinerAnimator(globalVar.objectPool[11],globalVar.animationPool[6])
        animator.pointLinerAnimator(globalVar.objectPool[12],globalVar.animationPool[6])
def stratSceneFICharCover34Logic():
    if globalVar.sceneTimer >= 110 and globalVar.sceneTimer < 170 :
        animator.pointLinerAnimator(globalVar.objectPool[13],globalVar.animationPool[6])
        animator.pointLinerAnimator(globalVar.objectPool[14],globalVar.animationPool[6])
def stratSceneFICharCover5Logic():
    if globalVar.sceneTimer >= 90 and globalVar.sceneTimer < 150 :
        animator.pointLinerAnimator(globalVar.objectPool[15],globalVar.animationPool[6])
def stratSceneMusicLogic():
    if globalVar.sceneTimer == 22:
        pygame.mixer.music.load('asset/bgm/StartBGM.wav')
        pygame.mixer.music.play()