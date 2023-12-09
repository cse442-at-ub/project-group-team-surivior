from character import Role
from rune_keystone import Conqueror

character1 = Role('yasuo',
                  750,
                  75,
                  30, 27,
                  Conqueror)

Enemy = Role('nasher',
             200,
             35,
             10, 7,
             None)

item_list = ['Plated_Steelcaps','Mercurys_Treads','B_F_Sword',
            'Hearthbound_Axe','Aegis_of_the_Legion',
            'Randuin_Omen','Abyssal_Mask',
            'Winter_Approach','Force_of_Nature','Warmog_Armor']

character1.apply_item_to_role(character1, item_list)

character1.apply_rune_keystone_to_role(character1, 'Conqueror')