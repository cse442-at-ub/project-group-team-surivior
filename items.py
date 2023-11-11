class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, data):
        new_node = Node(name, data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
###############################################################shoes###################################################################################################
ITEMS = LinkedList()
Boots = {'current_moving_speed': 25}
Berserkers_Greaves = {'current_attack_speed': 0.35, 'current_moving_speed': 45}
cd_Boots = {'current_ability_haste': 20, 'current_moving_speed': 45}
Sorcerers_Shoes = {'current_magic_penetration': 18, 'current_moving_speed': 45}
Plated_Steelcaps = {'current_armor': 20,'current_moving_speed': 45}
Mercurys_Treads = {'current_magic_resistance': 25, 'current_moving_speed': 45}

ITEMS.append('Boots', Boots)
ITEMS.append('Berserkers_Greaves', Berserkers_Greaves)
ITEMS.append('cd_Boots', cd_Boots)
ITEMS.append('Sorcerers_Shoes', Sorcerers_Shoes)
ITEMS.append('Plated_Steelcaps', Plated_Steelcaps)
ITEMS.append('Mercurys_Treads', Mercurys_Treads)
################################################################start items############################################################################################

Amplifying_Tome = {'current_ability_power': 20}
Cloth_Armor = {'current_armor': 15}
Magic_Mantle = {'current_magic_resistance': 25}
Dagger = {'current_attack_speed': 0.12}
Long_Sword = {'current_physical_damage_number': 10}
Ruby_Crystal = {'current_health': 150}
Sapphire_Crystal = {'current_mana': 250}

ITEMS.append('Amplifying_Tome', Amplifying_Tome)
ITEMS.append('Cloth_Armor', Cloth_Armor)
ITEMS.append('Magic_Mantle', Magic_Mantle)
ITEMS.append('Dagger', Dagger)
ITEMS.append('Long_Sword', Long_Sword)
ITEMS.append('Ruby_Crystal', Long_Sword)
ITEMS.append('Sapphire_Crystal', Sapphire_Crystal)
################################################################epic items#############################################################################################

Serrated_Dirk = {'current_physical_damage_number': 30, 'current_lethality': 10}
Kindlegem = {'current_ability_haste': 10, 'current_health': 200}
Vampiric_Scepter = {'current_physical_damage_number': 10, 'current_lifesteal': 0.07}
Fiendish_Codex = {'current_ability_power': 35, 'aility haste': 10}
Leeching_Leer = {'current_ability_power': 20, 'current_health': 250, 'current_omnivamp': 0.5}
Last_Whisper = {'current_physical_damage_number': 20, 'current_armor_penetration': 0.18}
Zeal = {'current_attack_speed': 0.15, 'current_moving_speed': 0.05}
Recurve_Bow = {'current_attack_speed': 0.15, 'current_magical_damage_number': 15}
Chain_Vest = {'current_armor': 40}
Giants_Belt = {'current_health': 350}
Negatron_Cloak = {'current_magic_resistance': 50}

ITEMS.append('Serrated_Dirk', Serrated_Dirk)
ITEMS.append('Kindlegem', Kindlegem)
ITEMS.append('Vampiric_Scepter', Vampiric_Scepter)
ITEMS.append('Fiendish_Codex', Fiendish_Codex)
ITEMS.append('Leeching_Leer', Leeching_Leer)
ITEMS.append('Last_Whisper', Last_Whisper)
ITEMS.append('Zeal', Zeal)
ITEMS.append('Recurve_Bow', Recurve_Bow)
ITEMS.append('Chain_Vest', Chain_Vest)
ITEMS.append('Giants_Belt', Giants_Belt)
ITEMS.append('Negatron_Cloak', Negatron_Cloak)
################################################################legendary items########################################################################################

#Legendary items

Cosmic_Drive= {'current_ability_power': 100, 'current_ability_haste': 30, 'current_moving_speed': 0.05}

ITEMS.append('Cosmic_Drive', Cosmic_Drive)
############################################################################################################################################

# beginner items, you can choose one of them before gmae's beginning, these will not be added in item bar.
doran_series = LinkedList()
Dorans_Blade = {'current_physical_damage_number': 8, 'current_health': 80, 'current_omnivamp': 0.025}
Dorans_Shield = {'current_health': 80, 'current_health_regen': 0.8} 
Dorans_Ring = {'current_ability_power': 15, 'current_health': 80} 
doran_series.append('Dorans_Blade', Dorans_Blade)
doran_series.append('Dorans_Shield', Dorans_Shield)
doran_series.append('Dorans_Ring', Dorans_Ring)


# epic items

Lost_Chapter = {'current_ability_power': 40, 'current_ability_haste': 10,'current_mana': 300}
Phage = {'current_physical_damage_number': 15, 'current_health': 200}
Hextexh_Alternator = {'current_ability_power': 25, 'current_health': 150}
Hearthbound_Axe = {'current_physical_damage_number': 20, 'current_attack_speed': 0.15}
Kircheis_Shard = {'current_physical_damage_number': 15}
Rageknife = {'current_attack_speed': 0.25}
Bamis_Cinder = {'current_health': 300}
Spectres_Cowl = {'current_health': 250, 'current_magic_resistance': 25}
Wardens_Mail = {'current_armor': 40}

ITEMS.append('Lost_Chapter', Lost_Chapter)
ITEMS.append('Phage', Phage)
ITEMS.append('Hextexh_Alternator', Hextexh_Alternator)
ITEMS.append('Hearthbound_Axe', Hearthbound_Axe)
ITEMS.append('Kircheis_Shard', Kircheis_Shard)
ITEMS.append('Rageknife', Rageknife)
ITEMS.append('Bamis_Cinder', Bamis_Cinder)
ITEMS.append('Spectres_Cowl', Spectres_Cowl)
ITEMS.append('Wardens_Mail', Wardens_Mail)

#legendary items
Demonic_Embrace = {'current_ability_power': 75, 'current_health': 350}
Horizon_Focus = {'current_ability_power': 100, 'current_ability_haste': 15, 'current_health': 150}
Rabadons_Deathcap = {'current_ability_power': 120}
Hextech_Gunblade = {'current_ability_power': 80, 'current_physical_damage_number': 40, 'current_omnivamp': 0.2}
Liandrys_Anguish = {'current_ability_power': 100, 'current_ability_haste': 20, 'current_mana': 600}
Bloodthirster = {'current_physical_damage_number': 55, 'current_lifesteal': 0.18}
Lord_Dominiks_Regards = {'current_physical_damage_number': 35, 'current_armor_penetration': 0.3}
Nashors_Tooth = {'current_ability_power': 100, 'current_ability_haste': 15, 'current_attack_speed': 0.5}
Runaans_Hurricane = {'current_attack_speed': 0.4, 'current_magical_damage_number': 20, 'current_moving_speed': 0.07}
Statikk_Shiv = {'current_physical_damage_number': 50,  'current_attack_speed': 0.3}
Wits_End = {'current_physical_damage_number': 40, 'current_attack_speed': 0.4, 'current_magic_resistance': 40}
Abyssal_Mask = {'current_ability_haste': 10, 'current_health': 300, 'current_magic_resistance': 60}
Force_of_Nature = {'magic rresistance': 60, 'current_health': 400, 'current_moving_speed': 0.05}
Spirit_Visage = {'current_ability_haste': 10, 'current_health': 450, 'current_magic_resistance': 60, 'current_health_regen': 1}
Steraks_Gage = {'current_health': 450}
Warmogs_Armor = {'current_ability_haste': 10, 'current_health': 800, 'current_health_regen': 2} 

ITEMS.append('Demonic_Embrace', Demonic_Embrace)
ITEMS.append('Horizon_Focus', Horizon_Focus)
ITEMS.append('Rabadons_Deathcap', Rabadons_Deathcap)
ITEMS.append('Hextech_Gunblade', Hextech_Gunblade)
ITEMS.append('Liandrys_Anguish', Liandrys_Anguish)
ITEMS.append('Bloodthirster', Bloodthirster)
ITEMS.append('Lord_Dominiks_Regards', Lord_Dominiks_Regards)
ITEMS.append('Nashors_Tooth', Nashors_Tooth)
ITEMS.append('Runaans_Hurricane', Runaans_Hurricane)
ITEMS.append('Statikk_Shiv', Statikk_Shiv)
ITEMS.append('Wits_End', Wits_End)
ITEMS.append('Abyssal_Mask', Abyssal_Mask)
ITEMS.append('Force_of_Nature', Force_of_Nature)
ITEMS.append('Spirit_Visage', Spirit_Visage)
ITEMS.append('Steraks_Gage', Steraks_Gage)
ITEMS.append('Warmogs_Armor', Warmogs_Armor)