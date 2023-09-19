import loadingFunctions,sceneDraw,animator,globalVar

def beforeFirstLoadingLogic():
    if globalVar.sceneTimer == 0:
        loadingFunctions.firstLoadingSceneAssetLoad()
        globalVar.sceneTimer= globalVar.sceneTimer + 1
    elif loadingFunctions.testFirstLoadingSceneAssetLoad():
        globalVar.sceneTimer = 0
        globalVar.currentUpdateBlock = firstLoadingLogic
        globalVar.currentDrawBlock = sceneDraw.firstLoadingDraw
    else: globalVar.sceneTimer= globalVar.sceneTimer + 1

def firstLoadingLogic():
    
    if globalVar.sceneTimer <= 30:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[2])
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[1])
    elif globalVar.sceneTimer < 360:
        animator.pointLinerAnimator(globalVar.objectPool[0],globalVar.animationPool[2])
    elif globalVar.sceneTimer == 360:
        globalVar.objectPool[2][6][4] = 0
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[0])
    elif globalVar.sceneTimer >= 360:
        animator.pointLinerAnimator(globalVar.objectPool[2],globalVar.animationPool[0])

    globalVar.sceneTimer = globalVar.sceneTimer + 1