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

# Initialize Pygame window
pygame.display.set_mode((1, 1))
# Load your item images
imagePathArray = []
for i in range(0,25):
    imagePathArray.append('asset/items/img'+str(i)+'.png')
    
itemPool = [None] * len(imagePathArray)

for i in range(0,len(imagePathArray)):
    itemPool[i] = pygame.image.load(imagePathArray[i])
    itemPool[i] = pygame.Surface.convert_alpha(itemPool[i]) 

imagePathArray = None

# Initial empty list of items in the item bar
item_bar_list = [0,1,2,3,4,5,6,7,8,9,10]

pygame.display.quit()
screen = None

if 'Lethal_Tempo' in globals() and 'Conqueror' in globals() and 'Dark_Harvest' in globals() and 'Grasp_of_the_Undying' in globals():
    print("Rune Keystone classes are available in globalVar.py")
else:
    print("Rune Keystone classes are not available in globalVar.py")