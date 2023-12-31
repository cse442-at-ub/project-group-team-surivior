import pygame
def inputload():
    inputContainer = {}
    inputContainer["currentCommand"] = {}
    inputContainer["commandState"] = {}
    inputContainer["cursorLocation"] = {}

    inputContainer["keyList"] = [pygame.K_q,pygame.K_w,pygame.K_e,pygame.K_r,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_1,pygame.K_2,pygame.K_3]
    inputContainer["commandList"] = ["Q","W","E","R","S","D","F","1","2","3","leftClick","rightClick","Mid"]
    
    for i in range(0,13):
        inputContainer["commandState"][i] = "Released"
        inputContainer["currentCommand"][i] = 0

    return inputContainer

def getCurrentCommand(inputContainer):
    for i in range(0,10):
        if pygame.key.get_pressed()[inputContainer["keyList"][i]]:
            inputContainer["currentCommand"][i] = 1
        else: 
            inputContainer["currentCommand"][i] = 0
    m_left, m_mid, m_right = pygame.mouse.get_pressed()
    inputContainer["currentCommand"][10] = int(m_left)
    inputContainer["currentCommand"][11] = int(m_mid)
    inputContainer["currentCommand"][12] = int(m_right)

def inputStateMachine(inputContainer):
    for i in range(0,13):
        match inputContainer["commandState"][i]:
            case "Released":
                if inputContainer["currentCommand"][i] == 1: 
                    inputContainer["commandState"][i] = "Pressing"
            case "Releasing":
                if inputContainer["currentCommand"][i] == 1: 
                    inputContainer["commandState"][i] = "Pressing"
                else:
                    inputContainer["commandState"][i] = "Released"
            case "Pressing":
                if inputContainer["currentCommand"][i] == 1: 
                    inputContainer["commandState"][i] = "Holding"
                else:
                    inputContainer["commandState"][i] = "Releasing"
            case "Holding":
                if inputContainer["currentCommand"][i] == 0: 
                    inputContainer["commandState"][i] = "Releasing"
                    
def inputUpdate(inputContainer):
    getCurrentCommand(inputContainer)
    inputStateMachine(inputContainer)