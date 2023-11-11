import threading
from rune_keystone import Lethal_Tempo, Conqueror, Dark_Harvest, Grasp_of_the_Undying

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

if 'Lethal_Tempo' in globals() and 'Conqueror' in globals() and 'Dark_Harvest' in globals() and 'Grasp_of_the_Undying' in globals():
    print("Rune Keystone classes are available in goldVar.py")
else:
    print("Rune Keystone classes are not available in goldVar.py")