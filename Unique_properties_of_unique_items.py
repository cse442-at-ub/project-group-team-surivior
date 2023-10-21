from items import *
from item_synthesis import *
from Unique_items_specific import *

# this file is used to write all unique items' unique properties
doran_series_list = list(doran_series.keys())
for item in item_bar:
    if item == doran_series_list[1]:
        # Doran's Shield
        doran_shield()
        continue
    elif item == doran_series_list[2]:
        # Doran's Ring
        doran_ring()
        continue
