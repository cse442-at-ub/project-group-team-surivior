def pointLinerAnimator(object,animation,outerEffect):
    # -- defultObject = {0,0,0,0,0}
    # -- defultObject["PLT"] = {0,0,0,0,0}
    # -- defultObject["PLD"] = {0,0,0,0,0}
    
    # -- defultAnimation = {}
    # ---- defultAnimation[x][1]表示当前点位置，defultAnimation[x][2]表示下一个点所在时间。
    # ---- defultAnimation[x][1]is current point value，defultAnimation[x][2]is next point time。
    # -- defultAnimation[0] = {0,9}
    # -- defultAnimation[9] = {23,12}
    # -- defultAnimation[12] = {2,0}
    # -- defultAnimation["prpty"] = 1
    # -- defultAnimation["length"] = 12
    # -- defultAnimation["loopType"] = "loop"

    if object["PLT"][animation["prpty"]] >= animation["length"] and animation["loopType"] == "loop" :
        object["PLT"][animation["prpty"]] = 0

    thisPLT = object["PLT"][animation["prpty"]]

    if animation[thisPLT] != None :
        nextTime = animation[thisPLT][2]
        nextValue = animation[nextTime][1]
        currentTime = thisPLT
        currentValue = animation[thisPLT][1]

        object["PLD"][animation["prpty"]] = (nextValue - currentValue)/(nextTime - currentTime)

    finalDelta = object["PLD"][animation["prpty"]] + outerEffect[animation["prpty"]]
    finalDelta = object["PLD"][animation["prpty"]]

    if object["PLT"][animation["prpty"]] < animation["length"] :
        object[animation["prpty"]] =  object[animation["prpty"]] + finalDelta
        object["PLT"][animation["prpty"]] = object["PLT"][animation["prpty"]] + 1
