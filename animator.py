def pointLinerAnimator(object,animation):
    # -- defultObject = {0,0,0,0,0}
    # -- defultObject[6] = {0,0,0,0,0}
    # -- defultObject[7] = {0,0,0,0,0}
    
    # -- defultAnimation = {}
    # ---- defultAnimation[x][1]表示当前点位置，defultAnimation[x][2]表示下一个点所在时间。
    # ---- defultAnimation[x][1]is current point value，defultAnimation[x][2]is next point time。
    # -- defultAnimation[0] = {0,9}
    # -- defultAnimation[9] = {23,12}
    # -- defultAnimation[12] = {2,0}
    # -- defultAnimation["prpty"] = 1
    # -- defultAnimation["length"] = 12
    # -- defultAnimation["loopType"] = "loop"

    if object[6][animation["prpty"]] >= animation["length"] and animation["loopType"] == "loop" :
        object[6][animation["prpty"]] = 0

    thisPLT = object[6][animation["prpty"]]

    if thisPLT in animation.keys() == False:
        nextTime = animation[thisPLT][1]
        nextValue = animation[nextTime][0]
        currentTime = thisPLT
        currentValue = animation[thisPLT][0]

        object[7][animation["prpty"]] = (nextValue - currentValue)/(nextTime - currentTime)

    # finalDelta = object[7][animation["prpty"]] + outerEffect[animation["prpty"]]
    finalDelta = object[7][animation["prpty"]]
    if animation["prpty"] == 5:
        finalDelta = int(finalDelta)

    if object[6][animation["prpty"]] < animation["length"] :
        object[animation["prpty"]] =  object[animation["prpty"]] + finalDelta
        object[6][animation["prpty"]] = object[6][animation["prpty"]] + 1