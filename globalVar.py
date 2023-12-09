import threading,os,pygame
from item_synthesis import check_synthesis_item, display_synthesizable_items

pygame.init()

currentUpdateBlock = None
currentDrawBlock = None

subStateMachineArray = {}

objectPool = []
animationPool = []
assetPool = []
imageThread = threading.Thread()
sceneTimer = 0
inputSystem = []
itemPool = []

res_w = 0 
res_h = 0 
BGMVolume = 0
SFXVolume = 0
score = 0
scoreboard = None

ITEM_BAR_HEIGHT = 100
ITEM_WIDTH = 80  # Width of each item including margin
MARGIN = 10

# Colors
WHITE = (255, 255, 255)

