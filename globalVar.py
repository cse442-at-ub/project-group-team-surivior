import threading,os,pygame

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
keystone_activation = None

ITEM_BAR_HEIGHT = 100
ITEM_WIDTH = 80  # Width of each item including margin
MARGIN = 10

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame window
pygame.display.set_mode((1, 1))
# Load your item images
imagePathArray = []
for i in range(0,9):
    imagePathArray.append('asset/items/img'+str(i)+'.png')
    
itemPool = [None] * len(imagePathArray)

for i in range(0,len(imagePathArray)):
    itemPool[i] = pygame.image.load(imagePathArray[i])
    itemPool[i] = pygame.Surface.convert_alpha(itemPool[i]) 

imagePathArray = None

# Initial empty list of items in the item bar
item_bar_list = [0,1,2,3,4,5,6,7,8]

pygame.display.quit()
screen = None
