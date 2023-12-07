from items import ITEMS
from rune_keystone import Conqueror, Guardian, Grasp_of_the_Undying
class Role:
    def __init__(self,
                 name,
                 max_health, 
                 current_damage_number,
                 current_armor, current_magic_resistance,
                 current_moving_speed,
                 rune_keystone):
        self.name = name
        self.max_health = max_health
        self.current_damage_number = current_damage_number
        self.current_moving_speed = current_moving_speed
        self.current_armor = current_armor
        self.current_magic_resistance = current_magic_resistance
        self.rune_keystone = rune_keystone


    # works
    def apply_item_to_role(self, role, item_names):
        current = ITEMS.head
        while current:
            if current.name in item_names:
                for attribute, value in current.data.items():
                    if hasattr(role, attribute):
                        setattr(role, attribute, getattr(role, attribute) + value)
            current = current.next
        return role
    #print(f"Updated Health: {yasuo.current_health}")
        """
        the above function returns an object, if you want to check if the item's attributes applys to characetr,
        using the following line of code, change the role.attribute based on your need. (go to check.py)
        print(f"Updated Health: {yasuo.current_health}")
        """
    def apply_rune_keystone_effects(self):
        if isinstance(self.rune_keystone, Conqueror):
            self.current_damage_number += 30
        elif isinstance(self.rune_keystone, Guardian):
            self.current_armor += 15
            self.current_magic_resistance += 10 
        elif isinstance(self.rune_keystone, Grasp_of_the_Undying):
            self.max_health += 100

    #works

    def attack(self, physical_damage, enemy_health):
        enemy_health -= physical_damage
        return enemy_health


