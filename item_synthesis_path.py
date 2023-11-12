class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

item_synthesis_path = LinkedList()
#shoes
Berserkers_Greaves = {'Berserkers_Greaves': ('Boots', 'Dagger')}
cd_Boots = {'cd_Boots': ('Boots', 600)}
Sorcerers_Shoes = {'Sorcerers_Shoes': ('Boots', 600)}
Plated_Steelcaps = {'Plated_Steelcaps': ('Boots', 'Cloth_Armor')}
Mercurys_Treads = {'Mercurys_Treads': ('Boots', 'Magic_Mantle')}
#epic items
Serrated_Dirk = {'Serrated_Dirk': ('Long_Sword', 'Long_Sword')}
Kindlegem = {'Kindlegem': ('Ruby_Crystal', 'Ruby_Crystal')}
Vampiric_Scepter = {'Vampiric_Scepter': ('Long_Sword', 'Long_Sword')}
Fiendish_Codex = {'Fiendish_Codex': ('Amplifying_Tome', 'Amplifying_Tome')}
Leeching_Leer = {'Leeching_Leer': ('Amplifying_Tome', 'Ruby_Crystal')}
Last_Whisper = {'Last_Whisper': ('Long_Sword', 'Agility_Cloak')}
Zeal = {'Zeal': ('Dagger', 'Agility_Cloak')}
Recurve_Bow = {'Recurve_Bow': ('Dagger', 'Dagger', 600)}
Chain_Vest = {'Chain_Vest': ('Cloth_Armor', 'Ruby_Crystal')}
Giants_Belt = {'Giants_Belt': ('Ruby_Crystal', 'Ruby_Crystal')}
Negatron_Cloak = {'Negatron_Cloak': ('Magic_Mantle', 'Magic_Mantle')}
#unique_epic_item
Lost_Chapter = {'Lost_Chapter': ('Amplifying_Tome', 'Sapphire_Crystal', 600)}
Phage = {'Phage': ('Long_Sword', 'Ruby_Crystal', 600)}
Hextexh_Alternator = {'Hextexh_Alternator': ('Amplifying_Tome', 'Ruby_Crystal', 600)}
Hearthbound_Axe = {'Hearthbound_Axe': ('Long_Sword', 'Dagger', 600)}
Kircheis_Shard = {'Kircheis_Shard': ('Long_Sword', 'Dagger', 600)}
Rageknife = {'Rageknife': ('Dagger', 'Amplifying_Tome', 600)}
Bamis_Cinder = {'Bamis_Cinder': ('Ruby_Crystal', 'Ruby_Crystal', 600)}
Spectres_Cowl = {'Spectres_Cowl': ('Magic_Mantle', 'health', 600)}
Wardens_Mail = {'Wardens_Mail': ('Cloth_Armor', 'Cloth_Armor', 600)}
#legendary items
Cosmic_Drive = {'Cosmic_Drive': ('Kindlegem', 'Fiendish_Codex')}
#unique legendary item
Demonic_Embrace = {'Demonic_Embrace': ('Fiendish_Codex', 'Giants_Belt', 600)}
Horizon_Focus = {'Horizon_Focus': ('Fiendish_Codex', 'Hextexh_Alternator', 600)}
Hextech_Gunblade = {'Hextech_Gunblade': ('Hextexh_Alternator', 'Vampiric_Scepter', 600)}
Liandrys_Anguish = {'Liandrys_Anguish': ('Lost_Chapter', 'Fiendish_Codex', 600)}
Bloodthirster = {'Bloodthirster': ('Vampiric_Scepter', 'B_F_Sword', 600)}
Lord_Dominiks_Regards = {'Lord_Dominiks_Regards': ('Last_Whisper', 'Recurve_Bow', 600)}
Nashors_Tooth = {'Nashors_Tooth': ('Recurve_Bow', 'Fiendish_Codex', 600)}
Runaans_Hurricane = {'Runaans_Hurricane': ('Recurve_Bow', 'Zeal', 600)}
Statikk_Shiv = {'Statikk_Shiv': ('Zeal', 'Kircheis_Shard', 600)}
Wits_End = {'Wits_End': ('Negatron_Cloak', 'Recurve_Bow', 600)}
Abyssal_Mask = {'Abyssal_Mask': ('Kindlegem', 'Negatron_Cloak', 600)}
Force_of_Nature = {'Force_of_Nature': ('Negatron_Cloak', 'Negatron_Cloak', 600)}
Spirit_Visage = {'Spirit_Visage': ('Kindlegem', 'Spectres_Cowl', 600)}
Steraks_Gage = {'Steraks_Gage': ('Giants_Belt', 'Giants_Belt', 600)}
Warmogs_Armor = {'Warmogs_Armor': ('Giants_Belt', 'Giants_Belt', 600)}

item_synthesis_path.append(Berserkers_Greaves)
item_synthesis_path.append(cd_Boots)
item_synthesis_path.append(Sorcerers_Shoes)
item_synthesis_path.append(Plated_Steelcaps)
item_synthesis_path.append(Mercurys_Treads)

item_synthesis_path.append(Serrated_Dirk)
item_synthesis_path.append(Kindlegem)
item_synthesis_path.append(Vampiric_Scepter)
item_synthesis_path.append(Fiendish_Codex)
item_synthesis_path.append(Leeching_Leer)
item_synthesis_path.append(Last_Whisper)
item_synthesis_path.append(Zeal)
item_synthesis_path.append(Recurve_Bow)
item_synthesis_path.append(Chain_Vest)
item_synthesis_path.append(Giants_Belt)
item_synthesis_path.append(Negatron_Cloak)

item_synthesis_path.append(Lost_Chapter)
item_synthesis_path.append(Phage)
item_synthesis_path.append(Hextexh_Alternator)
item_synthesis_path.append(Hearthbound_Axe)
item_synthesis_path.append(Kircheis_Shard)
item_synthesis_path.append(Rageknife)
item_synthesis_path.append(Bamis_Cinder)
item_synthesis_path.append(Spectres_Cowl)
item_synthesis_path.append(Wardens_Mail)
item_synthesis_path.append(Cosmic_Drive)
item_synthesis_path.append(Demonic_Embrace)
item_synthesis_path.append(Horizon_Focus)
item_synthesis_path.append(Hextech_Gunblade)
item_synthesis_path.append(Liandrys_Anguish)
item_synthesis_path.append(Bloodthirster)
item_synthesis_path.append(Lord_Dominiks_Regards)
item_synthesis_path.append(Nashors_Tooth)
item_synthesis_path.append(Runaans_Hurricane)
item_synthesis_path.append(Statikk_Shiv)
item_synthesis_path.append(Wits_End)
item_synthesis_path.append(Abyssal_Mask)
item_synthesis_path.append(Force_of_Nature)
item_synthesis_path.append(Spirit_Visage)
item_synthesis_path.append(Steraks_Gage)
item_synthesis_path.append(Warmogs_Armor)