import threading
from items import *
from item_synthesis_path import *
from Unique_items_specific import *

currentUpdateBlock = None
currentDrawBlock = None

subStateMachineArray = {}

objectPool = []
buttons = []
ssv = []
subState = []
animationPool = []
assetPool = []
buttons = []
imageThread = threading.Thread()
sceneTimer = 0
item = [gold, 
        your_choice, 
        shoes, 
        start_items, 
        epic_items, 
        legendary_items, 
        doran_series, 
        unique_shoes,
        unique_epic_items, 
        unique_legendary_items,
        supplies]
item_synthesis_path = [item_synthesis_path,
                       epic_item_synthesis_path,
                       epic_unique_item_synthesis_path,
                       legendary_items_synthesis_path,
                       legendary_unique_items_synthesis_path]
unique_item = [doran_ring(),
               doran_shield(),
               plated_shoe()]
res_w = 0 
res_h = 0 
BGMVolume = 0
SFXVolume = 0
score = 0
scoreboard = None

screen = None