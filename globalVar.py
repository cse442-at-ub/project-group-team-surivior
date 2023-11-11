import threading,os,pygame
from item_synthesis import check_synthesis_item, display_synthesizable_items

pygame.init()

currentUpdateBlock = None
currentDrawBlock = None

subStateMachineArray = {}

objectPool = []
buttons = []
ssv = []
subState = []
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

ITEM_BAR_HEIGHT = 100
ITEM_WIDTH = 80  # Width of each item including margin
MARGIN = 10

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame window
pygame.display.set_mode((1, 1))
# Load your item images
imagePathArray = []
imagePathArray.append('asset/items/Agility_Cloak.png') #0
imagePathArray.append('asset/items/Amplifying_Tome.png') #1
imagePathArray.append('asset/items/Cloth_Armor.png') #2
imagePathArray.append('asset/items/Dagger.png') #3
imagePathArray.append('asset/items/Long_Sword.png') #4
imagePathArray.append('asset/items/Magic_Mantle.png') #5
imagePathArray.append('asset/items/Rudy_Crystal.png') #6
imagePathArray.append('asset/items/Boots.png') #7
imagePathArray.append('asset/items/Berserkers_Greaves.png') #8
imagePathArray.append('asset/items/cd_Boots.png') #9
imagePathArray.append('asset/items/Mercurys_Treads.png') #10
imagePathArray.append('asset/items/Plated_Steelcaps.png') #11
imagePathArray.append('asset/items/Sorcerers_shoes.png') #12
imagePathArray.append('asset/items/Sapphire_Crystal.png') #13
imagePathArray.append('asset/items/Fiendish_Codex.png') #14
imagePathArray.append('asset/items/Kindlegem.png') #15
imagePathArray.append('asset/items/Serrated_Dirk.png') #16
imagePathArray.append('asset/items/Leeching_Leer.png') #17
imagePathArray.append('asset/items/Last_Whisper.png') #18
imagePathArray.append('asset/items/Zeal.png') #19
imagePathArray.append('asset/items/Recurve_Bow.png') #20
imagePathArray.append('asset/items/Chain_Vest.png') #21
imagePathArray.append('asset/items/Giants_Belt.png') #22
imagePathArray.append('asset/items/Negatron_Cloak.png') #23



itemPool = [None] * len(imagePathArray)

for i in range(0,len(imagePathArray)):
    itemPool[i] = pygame.image.load(imagePathArray[i])
    itemPool[i] = pygame.Surface.convert_alpha(itemPool[i]) 

imagePathArray = None

# Initial empty list of items in the item bar
item_bar_list = [0,1,2]

pygame.display.quit()
screen = None