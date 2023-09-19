import sys,loadingFunctions,sceneDraw,animator

def beforeFirstLoadingLogic(updateArguPack,drawArguPack):
    sceneTimer = updateArguPack[0]
    currentUpdateBlock = updateArguPack[1]
    currentDrawBlock = updateArguPack[2]
    assetPool = updateArguPack[3]
    objectPool = updateArguPack[4]
    imageThread = updateArguPack[5]
    animationPool = updateArguPack[6]

    if sceneTimer[0] == 0:
        loadingFunctions.firstLoadingSceneAssetLoad(assetPool,imageThread,objectPool,animationPool)
        sceneTimer[0] = sceneTimer[0] + 1
    elif loadingFunctions.testFirstLoadingSceneAssetLoad(imageThread):
        updateArguPack = [sceneTimer,currentUpdateBlock,currentDrawBlock,assetPool,objectPool,imageThread,animationPool]
        sceneTimer[0] = 0
        currentUpdateBlock[0] = firstLoadingLogic
        currentDrawBlock[0] = sceneDraw.firstLoadingDraw

def firstLoadingLogic(updateArguPack,drawArguPack):
    sceneTimer = updateArguPack[0]
    objectPool = updateArguPack[4]
    animationPool = updateArguPack[6]
    
    if sceneTimer[0] < 30:
        animator.pointLinerAnimator(objectPool[8],animationPool[1])
        animator.pointLinerAnimator(objectPool[0],animationPool[2])
        animator.pointLinerAnimator(objectPool[1],animationPool[2])
        animator.pointLinerAnimator(objectPool[2],animationPool[2])
        animator.pointLinerAnimator(objectPool[3],animationPool[2])
        animator.pointLinerAnimator(objectPool[4],animationPool[2])
        animator.pointLinerAnimator(objectPool[5],animationPool[2])
        animator.pointLinerAnimator(objectPool[6],animationPool[2])
    elif sceneTimer[0] < 360:
        animator.pointLinerAnimator(objectPool[0],animationPool[2])
        animator.pointLinerAnimator(objectPool[1],animationPool[2])
        animator.pointLinerAnimator(objectPool[2],animationPool[2])
        animator.pointLinerAnimator(objectPool[3],animationPool[2])
        animator.pointLinerAnimator(objectPool[4],animationPool[2])
        animator.pointLinerAnimator(objectPool[5],animationPool[2])
        animator.pointLinerAnimator(objectPool[6],animationPool[2])
    elif sceneTimer >= 360:
        animator.pointLinerAnimator(objectPool[8],animationPool[0])
        animator.pointLinerAnimator(objectPool[0],animationPool[2])
        animator.pointLinerAnimator(objectPool[1],animationPool[2])
        animator.pointLinerAnimator(objectPool[2],animationPool[2])
        animator.pointLinerAnimator(objectPool[3],animationPool[2])
        animator.pointLinerAnimator(objectPool[4],animationPool[2])
        animator.pointLinerAnimator(objectPool[5],animationPool[2])
        animator.pointLinerAnimator(objectPool[6],animationPool[2])

    sceneTimer[0] = sceneTimer[0] + 1