from items import ITEMS
class Role:
    def __init__(self,
                 name,
                 current_gold,
                 max_health, current_health, current_health_regen,
                 max_mana, current_mana, current_mana_regen,
                 current_physical_damage_number, current_magical_damage_number,
                 current_armor, current_lethality, current_armor_penetration,
                 current_magic_resistance, current_ability_power, current_magic_penetration,
                 current_true_damage,
                 current_attack_speed, current_moving_speed,
                 current_ability_haste,
                 current_lifesteal, current_omnivamp,
                 current_level,
                 rune_keystone):
        self.name = name
        self.current_gold = current_gold
        self.current_ability_power = current_ability_power
        self.current_health = current_health
        self.max_health = max_health
        self.current_health_regen = current_health_regen
        self.current_mana = current_mana
        self.max_mana = max_mana
        self.current_mana_regen = current_mana_regen
        self.current_physical_damage_number = current_physical_damage_number
        self.current_magical_damage_number = current_magical_damage_number
        self.current_true_damage = current_true_damage
        self.current_attack_speed = current_attack_speed
        self.current_moving_speed = current_moving_speed
        self.current_armor = current_armor
        self.current_lethality = current_lethality
        self.current_armor_penetration = current_armor_penetration
        self.current_magic_resistance = current_magic_resistance
        self.current_magic_penetration = current_magic_penetration
        self.current_ability_haste = current_ability_haste
        self.current_lifesteal = current_lifesteal
        self.current_omnivamp = current_omnivamp
        self.current_level = current_level
        self.rune_keystone = rune_keystone

    exp_to_upgrade = 600
    current_exp = 0
    exp = 20

    def apply_item_to_role(role, item_names):
        current = ITEMS.head
        while current:
            if current.name in item_names:
                for attribute, value in current.data.items():
                    if hasattr(role, attribute):
                        setattr(role, attribute, getattr(role, attribute) + value)
            current = current.next
        return role
        """
        the above function returns an object, if you want to check if the item's attributes applys to characetr,
        using the following line of code, change the role.attribute based on your need. (go to check.py)
        print(f"Updated Health: {yasuo.current_health}")
        """
    
    # upgrade just valid for character instead of enemy
    def upgrade(self):
        if self.current_exp >= self.exp_to_upgrade and self.current_level < 18:
            self.current_level += 1
            self.current_exp -= self.exp_to_upgrade
            self.exp_to_upgrade += 200  # Increase the exp required for the next level
            upgrades = {
                'max_health': 20,
                'current_health': 20,
                'current_health_regen': 0.1,
                'max_mana': 10,
                'current_mana': 10,
                'current_mana_regen': 0.08,
                'current_physical_damage_number': 5,
                'current_magical_damage_number': 0,
                'current_armor': 5,
                'current_lethality': 0,
                'current_armor_penetration': 0.0,
                'current_magic_resistance': 3,
                'current_ability_power': 0,
                'current_magic_penetration': 0.0,
                'current_true_damage': 0,
                'current_attack_speed': 0.08,
                'current_moving_speed': 0,
                'current_ability_haste': 0,
                'current_lifesteal': 0,
                'current_omnivamp': 0,
                'current_level': 1,
                'rune_keystone': 0
            }

            for attribute, value in upgrades.items():
                setattr(self, attribute, getattr(self, attribute) + value)

    # only for characetr
    def gain_exp(self):
        if self.take_damage:
            self.current_exp += 20
            self.upgrade()
    
    # only for characetr
    def gian_gold(self):
        current_health = self.current_health.take_damage(self.current_magical_damage_number, self.current_physical_damage_number)
        if current_health == 0:
            self.current_gold += 50
    
    # For both
    def take_damage(self, current_magical_damage_number, current_physical_damage_number):
        physical_damage = current_physical_damage_number * (10 // self.current_armor)
        magical_damage = current_magical_damage_number * (10 // self.current_magic_resistance)

        if self.current_health > 0:
            self.current_health -= physical_damage + magical_damage + self.current_true_damage
        if self.current_health == 0:
            return True
    
    # For both
    def attack(self, target):
        target.take_damage(self.current_magical_damage_number, self.current_physical_damage_number)