import loadingFunctions,sceneDraw,animator,globalVar,threading,button,pygame,Sound,math,score

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
        x_win, y_win = globalVar.screen.get_size()
        b_Document = button.Button("Document",(0*x_win/1600,755*y_win/900),globalVar.screen)
        b_NewGame = button.Button("NewGame",(320*x_win/1600,755*y_win/900),globalVar.screen)
        b_Continue = button.Button("Continue",(640*x_win/1600,755*y_win/900),globalVar.screen)
        b_Config = button.Button("Config",(960*x_win/1600,755*y_win/900),globalVar.screen)
        b_Exit = button.Button("Exit",(1280*x_win/1600,755*y_win/900),globalVar.screen)
        globalVar.buttons = [b_Document, b_NewGame, b_Continue, b_Config, b_Exit]
        globalVar.subState = [None]*5
        globalVar.subState[0] = "flashIn"
        globalVar.subState[1] = 2
        globalVar.subState[2] = "unclicked"

    if globalVar.sceneTimer > 200:
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
        Sound.play_music('asset/bgm/StartBGM.wav')
        

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
            if globalVar.buttons[4].check_clicked(): #b_Exit
                pygame.quit()
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
            if globalVar.buttons[4].check_clicked(): #b_Exit
                pygame.quit()
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
            if globalVar.buttons[4].check_clicked(): #b_Exit
                pygame.quit()
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
                animator.pointLinerAnimator(globalVar.objectPool[27],globalVar.animationPool[7])
                animator.pointLinerAnimator(globalVar.objectPool[34],globalVar.animationPool[7])
                globalVar.objectPool[34][5] = 1
            if globalVar.sceneTimer > 315 and globalVar.sceneTimer < 335:
                for i in range(46,53):
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
                for i in range(28,34):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[8])
                for i in range(35,45):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[8])
            if globalVar.sceneTimer >= 340:
                if globalVar.inputSystem["commandState"][6] == "Pressing":
                    globalVar.subState[0] = "mapFlashIn"
                    for i in range(0,54):
                        globalVar.objectPool[i][6] = [0,0,0,0,0,0]
                        globalVar.objectPool[i][7] = [0,0,0,0,0,0]
                    globalVar.sceneTimer = 299
        case "mapFlashIn":
            if globalVar.sceneTimer < 420:
                animator.pointLinerAnimator(globalVar.objectPool[11],globalVar.animationPool[26])
                animator.pointLinerAnimator(globalVar.objectPool[12],globalVar.animationPool[26])
                animator.pointLinerAnimator(globalVar.objectPool[13],globalVar.animationPool[27])
                animator.pointLinerAnimator(globalVar.objectPool[14],globalVar.animationPool[27])
                animator.pointLinerAnimator(globalVar.objectPool[15],globalVar.animationPool[28])
                animator.pointLinerAnimator(globalVar.objectPool[27],globalVar.animationPool[15])
                for i in range(28,45):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[9])
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[10])
                animator.pointLinerAnimator(globalVar.objectPool[45],globalVar.animationPool[16])
                animator.pointLinerAnimator(globalVar.objectPool[45],globalVar.animationPool[17])
                animator.pointLinerAnimator(globalVar.objectPool[46],globalVar.animationPool[15])
                for i in range(47,53):
                    animator.pointLinerAnimator(globalVar.objectPool[i],globalVar.animationPool[9])

            if globalVar.sceneTimer >= 420:
                Sound.change_music('asset/bgm/GameBGM.wav')
                globalVar.subStateMachineArray = {}
                globalVar.objectPool = []
                globalVar.buttons = []
                globalVar.animationPool = []
                globalVar.assetPool = []
                globalVar.sceneTimer = 0
                loadingFunctions.ingameAssetLoad()
                globalVar.health = 10  # Character's initial health
                globalVar.damage = 1  # Initial damage dealt by the enemy
                globalVar.attack_timer = 0  # Timer for enemy attack
                globalVar.color_change_timer = 0  # Timer for character color change
                globalVar.color_change_timer_heal = 0
                globalVar.currentUpdateBlock = ingameScene
                globalVar.currentDrawBlock = sceneDraw.ingameDraw
                globalVar.character_x = 0
                globalVar.character_y = 0
                globalVar.charMoving = False
                globalVar.enemyMoving = False
                globalVar.fps = 180
                globalVar.enemyHealth = 5 # enemy's health
                globalVar.kill_timer = 0 # timer for character

def ingameScene():
    globalVar.scoreboard = score.ScoreBoard()
    if globalVar.inputSystem["commandState"][10] == "Pressing":  
        globalVar.character_x, globalVar.character_y = pygame.mouse.get_pos()
        x_win, y_win = globalVar.screen.get_size()
        globalVar.character_x = globalVar.character_x/x_win*1600
        globalVar.character_y = globalVar.character_y/y_win*900
        globalVar.charMoving = True


    if globalVar.inputSystem["commandState"][3] == "Pressing" and globalVar.health < 10: # press R to heal
        if globalVar.fps >= 180:   
            globalVar.health += 1
            globalVar.fps = 0

    if globalVar.fps < 300:
        globalVar.fps += 1

    if globalVar.charMoving:
        dx, dy = globalVar.character_x - (globalVar.objectPool[0][0]+30), globalVar.character_y - (globalVar.objectPool[0][1]+80)
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if abs(dx) <= 3 and abs(dy) <= 3:
            globalVar.charMoving = False

        if distance > 0:
            dx /= distance
            dy /= distance

            globalVar.objectPool[0][0]+= dx * 3
            globalVar.objectPool[0][1] += dy * 3
            globalVar.objectPool[1][0]+= dx * 3
            globalVar.objectPool[1][1] += dy * 3

    dx, dy = (globalVar.objectPool[0][0]+30) - (globalVar.objectPool[2][0]+60), (globalVar.objectPool[0][1]+80) - (globalVar.objectPool[2][1]+90)
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if abs(dx) > 3 and abs(dy) > 3:
        globalVar.enemyMoving = True
    
    if globalVar.enemyMoving:
        if globalVar.enemyHealth > 0 and globalVar.enemyHealth < 5:
            if globalVar.fps >= 240:   
                globalVar.enemyHealth += 1
                globalVar.fps = 0
                
        if distance > 0:
            dx /= distance
            dy /= distance

            globalVar.objectPool[2][0]+= dx * 2
            globalVar.objectPool[2][1] += dy * 2
            globalVar.objectPool[3][0]+= dx * 2
            globalVar.objectPool[3][1] += dy * 2

        dx, dy = (globalVar.objectPool[0][0]+30) - (globalVar.objectPool[2][0]+60), (globalVar.objectPool[0][1]+80) - (globalVar.objectPool[2][1]+90)
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if abs(dx) > 3 and abs(dy) > 3:
            globalVar.enemyMoving = True
        
        if globalVar.health > 0 and distance <= 15 and globalVar.attack_timer <= 0 and globalVar.enemyHealth > 0:  
            globalVar.health -= globalVar.damage  # Reduce character's health
            globalVar.attack_timer = 60  # Set the attack timer to 1 second (FPS frames)
            # globalVar.color_change_timer = int(0.1 * 60)  # Set color change timer to 0.1 seconds

        globalVar.attack_timer = max(0, globalVar.attack_timer - 1)  # Decrease the attack timer
        # globalVar.color_change_timer = max(0, globalVar.color_change_timer - 1)  # Decrease the color change timer
        # globalVar.color_change_timer_heal = max(0, globalVar.color_change_timer_heal - 1)  # Decrease the color change timer
        
        if globalVar.inputSystem["commandState"][0] == "Pressing" and globalVar.enemyHealth > 0 and distance <= 20 and globalVar.kill_timer <= 0: # press Q to kill
            globalVar.enemyHealth -= 1 # reduce enemy health
            globalVar.score += 1 # increase score
            globalVar.kill_timer = 30 # Set the attack timer to 0.5 second (FPS frames)
        
        globalVar.kill_timer = max(0, globalVar.kill_timer - 1)  # Decrease the kill timer
        
    if globalVar.enemyHealth <= 0:
        globalVar.enemyMoving = False
        x_win, y_win = globalVar.screen.get_size()
        globalVar.currentUpdateBlock = endScene
        globalVar.currentDrawBlock = sceneDraw.ingameDraw
        Sound.change_music("asset/bgm/VictoryBGM.wav")
        globalVar.objectPool[5][4] = 255
        b_toStart = button.Button("start",(633*x_win/1600,510*y_win/900),globalVar.screen)
        globalVar.buttons = [b_toStart]

    if globalVar.health <= 0:
        x_win, y_win = globalVar.screen.get_size()
        globalVar.currentUpdateBlock = endScene
        globalVar.currentDrawBlock = sceneDraw.ingameDraw
        Sound.change_music("asset/bgm/Gameover.wav")
        globalVar.objectPool[5][4] = 255
        b_toStart = button.Button("start",(633*x_win/1600,510*y_win/900),globalVar.screen)
        globalVar.buttons = [b_toStart]

def endScene():
    if globalVar.inputSystem["commandState"][10] == "Pressing" and globalVar.buttons[0].check_collided():
        globalVar.score = 0
        globalVar.objectPool[5][3] = 0
        globalVar.currentUpdateBlock = startScenenLogic 
        globalVar.currentDrawBlock = sceneDraw.drawBlack4Start
        globalVar.sceneTimer = -1
