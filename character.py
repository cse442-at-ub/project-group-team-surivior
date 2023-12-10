from rune_keystone import rune_keystones
from items import ITEMS

class Role:
    def __init__(self,
                 name,
                 max_health, 
                 current_damage_number,
                 current_armor, current_magic_resistance,
                 rune_keystone):
        self.name = name
        self.max_health = max_health
        self.current_damage_number = current_damage_number
        self.current_armor = current_armor
        self.current_magic_resistance = current_magic_resistance
        self.rune_keystone = rune_keystone

    # works
    def apply_item_to_role(self, role, item_names):
        current = ITEMS.head
        while current:
            for item in item_names:
                if current.name == item:
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

    def apply_rune_keystone_to_role(self, role, Rune_Keystone):
        current = rune_keystones.head
        while current:
            if current.name == Rune_Keystone:
                for attribute, value in current.data.items():
                    if hasattr(role, attribute):
                        setattr(role, attribute, getattr(role, attribute) + value)                
            current = current.next
        return role


