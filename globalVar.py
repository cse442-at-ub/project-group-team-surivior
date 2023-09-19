import threading

currentUpdateBlock = None
currentDrawBlock = None

subStateMachineArray = {}

objectPool = []
animationPool = []
assetPool = []
imageThread = threading.Thread()
sceneTimer = 0

res_w = 0 
res_h = 0 
BGMVolume = 0
SFXVolume = 0

screen = None