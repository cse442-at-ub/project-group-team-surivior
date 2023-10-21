#items
gold = {'value': 1}
# if you do not want any beginer item, you have another choice
your_choice = {}
your_choice['Boots'] = {'movement': 25, 'gold': 150}
your_choice['gold'] = {'gold': 450}

#shoes
shoes = {}
shoes["Berserker's Greaves"] = {'attack speed': 0.35, 'movement speed': 45}
shoes['Ionian Boots of Lucidity'] = {'ability haste': 20, 'movement': 45}
shoes["Sorcerer's Shoes"] = {'magic penetration': 18, 'movement': 45}
shoes['Plated Steelcaps'] = {'armor': 20,'movement': 45}

#start items
start_items = {}
start_items['Amplifying Tome'] = {'ability power': 20}
start_items['Agility Cloak'] = {'critical strike chance': 0.15}
start_items['Cloth Armor'] = {'armor': 15}
start_items['Magic Mantle'] = {'magic resistance': 25}
start_items['Dagger'] = {'attack speed': 0.12}
start_items['Long Sword'] = {'attack damage': 10}
start_items['Ruby Crystal'] = {'health': 150}
start_items['Sapphire Crystal'] = {'mana': 250}

#Epic items
epic_items = {}
epic_items['Serrated Dirk'] = {'attack damage': 30, 'lethality': 10}
epic_items['Kindlegem'] = {'ability haste': 10, 'health': 200}
epic_items['Vampiric Scepter'] = {'attack damage': 10, 'lifesteal': 0.07}

epic_items['Fiendish Codex'] = {'ability power': 35, 'aility haste': 10}
epic_items['Leeching Leer'] = {'ability power': 20, 'health': 250, 'omnivamp': 0.5}
epic_items['Needlessly Large Rod'] = {'ability power': 60}

epic_items['Last Whisper'] = {'attack damage': 20, 'armor penetration': 0.18}
epic_items['Zeal'] = {'attack speed': 0.15, 'critical strike chance': 0.15, 'movement': 0.05}
epic_items['B.F.Sword'] = {'attack damage': 40}

epic_items['Chain Vest'] = {'armor': 40}
epic_items["Giant's Belt"] = {'health': 350}
epic_items['Negatron Cloak'] = {'magic resistance': 50}


#Legendary items
legendary_items ={}
legendary_items['Cosmic Drive'] = {'ability power': 100, 'ability haste': 30, 'movement': 0.05}

############################################################################################################################################

#unique items

# beginner items, you can choose one of them before gmae's beginning, these will not be added in item bar.
doran_series = {}
doran_series["Doran's Blade"] = {'attack damage': 8, 'health': 80, 'omnivamp': 0.025}
doran_series["Doran's Shield"] = {'health': 80, 'health regen': 0.8} #UNIQUE
doran_series["Doran's Ring"] = {'ability power': 15, 'health': 80} #UNIQUE

# shoes with unique stuff
unique_shoes = {}
unique_shoes["Mercury's Treads"] = {'magic resistance': 25, 'movement': 45} #UNIQUE

# epic items with unique stuff
unique_epic_items = {}
unique_epic_items['Lost Chapter'] = {'ability power': 40, 'ability haste': 10,'mana': 300}
unique_epic_items['Phage'] = {'attack damage': 15, 'health': 200}
unique_epic_items['Hextexh Alternator'] = {'ability power': 25, 'health': 150}#UNIQUE
unique_epic_items['Hearthbound Axe'] = {'attack damage': 20, 'attack speed': 0.15}#UNIQUE
unique_epic_items['Kircheis Shard'] = {'attack damage': 15}#UNIQUE
unique_epic_items['Rageknife'] = {'attack speed': 0.25}#UNIQUE
unique_epic_items['Recurve Bow'] = {'attack speed': 0.15}#UNIQUE
unique_epic_items["Bami's Cinder"] = {'health': 300}#UNIQUE
unique_epic_items["Spectre's Cowl"] = {'health': 250, 'magic resistance': 25}#UNIQUE
unique_epic_items["Warden's Mail"] = {'armor': 40}#UNIQUE

# unqiue legendary items
unique_legendary_items = {}
unique_legendary_items['Demonic Embrace'] = {'ability power': 75, 'health': 350}#UNIQUE
unique_legendary_items['Horizon Focus'] = {'ability power': 100, 'ability haste': 15, 'health': 150}#UNIQUE
unique_legendary_items["Rabadon's Deathcap"] = {'ability power': 120}#UNIQUE
unique_legendary_items['Hextech Gunblade'] = {'ability power': 80, 'attack damage': 40, 'omnivamp': 0.2}#UNIQUE
unique_legendary_items["Liandry's Anguish"] = {'ability power': 100, 'ability haste': 20, 'mana': 600}#UNIQUE
unique_legendary_items['Bloodthirster'] = {'attack damage': 55, 'critical strike chance': 0.2, 'lifesteal': 0.18}#UNIQUE
unique_legendary_items["Lord Dominik's Regards"] = {'attack damage': 35, 'critical strike chance': 0.2, 'armor penetration': 0.3}#UNIQUE
unique_legendary_items["Nashor's Tooth"] = {'ability power': 100, 'ability haste': 15, 'attack speed': 0.5}#UNIQUE
unique_legendary_items["Runaan's Hurricane"] = {'attack speed': 0.4, 'critical strike chance': 0.2, 'movement': 0.07}#UNIQUE
unique_legendary_items['Statikk Shiv'] = {'attack damage': 50, 'critical strike chance': 0.2, 'attack speed': 0.3}#UNIQUE
unique_legendary_items["Wit's End"] = {'attack damage': 40, 'attack speed': 0.4, 'magic resistance': 40}#UNIQUE
unique_legendary_items['Abyssal Mask'] = {'ability haste': 10, 'health': 300, 'magic resistance': 60}#UNIQUE
unique_legendary_items['Force of Nature'] = {'magic rresistance': 60, 'health': 400, 'movement': 0.05}#UNIQUE
unique_legendary_items['Spirit Visage'] = {'ability haste': 10, 'health': 450, 'magic resistance': 60, 'health regen': 1}#UNIQUE / health regen: 100%
unique_legendary_items["Sterak's Gage"] = {'health': 450}#UNIQUE
unique_legendary_items["Warmog's Armor"] = {'ability haste': 10, 'health': 800, 'health regen': 2}#UNIQUE / health regen: 200%
unique_legendary_items["Jak'sSho, The Protean"] = {'ability haste': 20, 'health': 400, 'magic resistance': 30, 'armor': 30}#UNIQUE


# supplies after the player getting 3 legendary items
supplies = {}
supplies['health potion'] = {
    'gold': 50,
    'capability': 0, # Regenerates 4 health every 0.5 seconds over 15 seconds, restoring a total of 120 health.
    'limitation': 5
}
supplies['Elixir of Iron'] = {
    'gold': 50,
    'capability': 1, # Grants 300 bonus health, 25% Tenacity icon Tenacity, and 15% increased size for 180 seconds. While active, moving leaves behind a path briefly that grants 15% bonus movement speed to allied champions within. Can be used while dead.
    'limitation': 1
}
supplies['Elixir of Sorcery'] = {
    'gold': 50,
    'capability': 2, # Grants 50 ability power and 15 bonus mana regeneration for 180 seconds. While active, going in combat by affecting enemy champions or turrets deals 25 bonus true damage (5 second cooldown on each champion, no cooldown against turrets). Can be used while dead.
    'limitation': 1
}
supplies['Elixir of Wrath'] = {
    'gold': 50,
    'capability': 3, # Grants 30 bonus attack damage and Heal power icon heals for 12% of physical damage dealt to champions for 180 seconds. The heal is reduced to 33% effectiveness for area damage. Can be used while dead.
    'limitation': 1
}