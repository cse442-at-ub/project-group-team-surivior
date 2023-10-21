from item_synthesis_path import *
from items import *

"""
Based on the original assumption of game, the game has three major levels, 
first two major levels has six smaller levels (for better distribution and synthesis of item logic written ), 
and the last major level has 10 smaller levels.

For item bar, there are 7 grids.

The beginer items (Doran series) do not occupy item grid.

For current gold, the player can get different amount of golds from killing different monster.
"""
item_bar = []
current_gold = 0
"""
In each major level, the first two small levels can choose two starter items, 
then choose an epic item based on the starter items the player choose at the third small level;
same as the following three small level. 
At the end of the first two major levels, the player can choose legendary items based on their epic items chocies.
      
For the last major levels, after the first 6 small levels, the player will have 3 legendary items and them can buy supplies based on their needs
"""

start_items_check_box = []
epic_items_check_box = []
legendary_items_check_box = []

if len(item_bar) != 0:
    for item in item_bar:
        if item in list(start_items.keys()):
            start_items_check_box.append(item)
        elif item in list(epic_items.keys()):
            epic_items_check_box.append(item)
        elif item in list(legendary_items.keys()):
            legendary_items_check_box.append(item)

# check if the player can get epic item or not
epic_item_available = []

if len(start_items_check_box) == 2:
    for synthesis in epic_item_synthesis_path:
        if set(synthesis.values()) == set(start_items_check_box):
            epic_item_available.append(list(synthesis.keys())[0])

epic_unique_item_available = []

if len(start_items_check_box) == 2 and current_gold == 600:
    items = list(start_items_check_box) + [600]  # Append 600 to the list
    for synthesis in epic_unique_item_synthesis_path:
        if set(synthesis.values()) == set(items):
            epic_unique_item_available.append(list(synthesis.keys())[0])

# Check if the player can get legendary item or not
legendary_items_available = []

if len(epic_items_check_box) == 2:
    for synthesis in legendary_items_synthesis_path:
        if set(synthesis.values()) == set(epic_items_check_box):
            legendary_items_available.append(list(synthesis.keys())[0])

legendary_unique_items_available = []

if len(epic_items_check_box) == 2 and current_gold == 600:
    items = list(start_items_check_box) + [600]
    for synthesis in legendary_unique_items_synthesis_path:
        if set(synthesis.values()) == set(items):
            legendary_unique_items_available.append(list(synthesis.keys())[0])