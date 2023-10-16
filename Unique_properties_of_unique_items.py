from items import *
from item_synthesis import *

# this file is used to write all unique items' unique properties
for item in item_bar:
    if item in list(unique_epic_items.keys()) or list(unique_legendary_items.keys()):
        if item == 'Lost Chapter':
            # Returns a certain percentage of mana when the character is upgraded.
            # It has no cooldown
            continue
        if item == 'Phage':
            # Restores a certain percentage of health when the character is attacked.
            # It has no cooldown
            continue
        if item == 'Tiamat':
            # When you attack an enemy, you deal physical damage to enemies within a certain range.
            # It has no cooldown.
            continue
        if item == 'Sheen':
            """
            When you use a skill once, the next normal attack for a certain amount of time deals 
            an additional double the damage of your current attack power.
            """
            # It has a cooldown
            continue
        if item == 'Hextexh Alternator':
            # When you use a skill to attack an enemy, your skill deals additional magic damage.
            # It has a cooldown
            continue
        if item == 'Catalyst of Aeons':
            """
            When you deplete mana, it returns a percentage of your health; when you are attacked, 
            it returns a percentage of your mana.
            """
            # It has no cooldown
            continue
        if item == 'Hearthbound Axe':
            # When a character attacks an enemy, they gain a speed bonus for 2 seconds.
            # It has no cooldown
            continue
        if item == 'Kircheis Shard':
            """
            Characters gain points by moving, and when they reach 100, 
            their next normal attack deals 20 points of magic damage to the enemy 
            and gains an ever-decreasing bonus to movement speed over 2 seconds.
            """
            # It has no cooldown
            continue
        if item == 'Noonquiver':
            # The character's normal attack deals an additional 15 points of physical damage to the enemy.
            # It has no cooldown
            continue
        if item == 'Rageknife':
            """
            When you equip this equipment, you will not be able to deal bludgeoning damage to enemies, 
            and you will no longer be able to select any equipment with the bludgeoning attribute. 
            The bludgeoning you already have will be converted into a percentage of magic damage.
            """
            # It has no cooldown
            continue
        if item == 'Recurve Bow':
            # Your normal attack will deal 15 points of magic damage to the enemy.
            # It has no cooldown
            continue
        if item == "Bami's Cinder":
            # You deal 15 points of magic damage per second to enemies that would be within a certain range (increases with life).
            # It has no cooldown
            continue
        if item == 'Bramble Vest':
            # When you are attacked, 15 points of magic damage are returned to the enemy attacking you.
            # It has no cooldown
            continue
        if item == "Spectre's Cowl":
            # The character's life regen and shield value will increase by 150%.
            # It has no cooldown
            continue
        if item == "Warden's Mail":
            # Damage taken by the character from enemy normal attacks is reduced by 15%.
            # It has no cooldown
            continue
        if item == 'Winged Moonplate':
            # Character's movement speed is increased by 15%.
            # It has no cooldown
            continue
        if item == 'Hexdrinker':
            # When below 30% life, it gains a magic shield of 200 life points and 15% life steal for 5 seconds
            # It has a cooldown
            continue
        if item == 'Maw of Malmortius':
            # When life is below 30%, the character gains a magic shield of 500 life points and gains 20% life steal for 5 seconds.
            # It has no cooldown
            continue
        if item == 'Titanic Hydra':
            """
            When you attack an enemy (Normal Attacks, Skill Attacks, and Equipment Active Effect Attacks, etc.), 
            you deal Physical Damage as a percentage of your own Maximum Life to the attacked target, 
            and deal Ranged Physical Damage in a cone of range behind the attacked target (again, proportional to a percentage of your Maximum Life).
            """
            # It has no cooldown
            continue
        if item == 'Ravenous Hydra':
            """
            When you attack an enemy (Normal Attacks, Skill Attacks, 
            and Equipped Active Effect Attacks, etc.), physical damage is dealt to enemies within a certain range, 
            and the character can gain Attack Power, up to 40 points, by killing enemies.
            """
            # It has no cooldown
            continue
        if item == "Death's Dance":
            """
            When you are attacked, it reduces physical damage by 20% and magic Shanghai by 15%. 
            The mitigated damage will be deducted from your character's life value in the form of real damage for the next 10 seconds.
            """
            # It has no cooldown
            continue
        if item == 'Spear of Shojin':
            """
            Non-ultimate skills as well as ultimate skills gain skill cooldowns (proportional to attack power). 
            Using non-Ultimate skills reduces the cooldown reduction of other non-Ultimate skills.
            """
            # It has no cooldown
            continue
        if item == 'Divine Sunderer':
            """
            When you use a skill once, your next normal attack deals a percentage of its maximum lifesteal to the enemy, 
            while returning 55% of the damage dealt to the enemy's lifesteal.
            """
            # It has cooldown
            continue
        if item == 'Demonic Embrace':
            """
            Gain a percentage of ability power based on your maximum life, 
            as well as searing enemies and dealing 8% of their maximum life value in magic damage for 8 seconds when dealing skill damage to them.
            """
            # It has no cooldown
            continue
        if item == 'Horizon Focus':
            """
            Increases magic damage proportional to your own ability power when dealing damage to an enemy 600 yards away.
            """
            # It has no cooldown
            continue
        if item == 'Lich Bane':
            """
            When you use a skill once, your next normal attack deals 400 + (10% * ability power) magic damage to the enemy.
            """
            # It has cooldown
            continue
        if item == "Rabadon's Deathcap":
            # Increases the character's ability power by 120% on top of what they already have.
            # It has no cooldown
            continue
        if item == "Rylai's Crystal Scepter":
            # When you use a skill on an enemy, slow the enemy by 20% for 4 seconds.
            # It has no cooldown
            continue
        if item == 'Rod of Ages':
            # Responds to a percentage of life when depleting blue, and a percentage of blue when receiving an attack.
            # It has no cooldown
            continue
        if item == 'Hextech Gunblade':
            # Item Active Effect: Inflicts (abiity power*20% + Attack Power*15%) magic damage on designated enemies.
            # It has cooldown
            continue
        if item == "Luden's Tempest":
            # When you attack an enemy with a skill, it deals splash damage to its four nearest enemies.
            # It has cooldown
            continue
        if item == "Liandry's Anguish":
            # When you hit an enemy with a skill, cauterize the enemy, dealing 20% of their maximum life value in magic damage for 5 seconds.
            # It has no cooldown
            continue
        if item == 'Bloodthirster':
            # Characters gain an additional 40 attack power when their life is above 70%.
            # It has no cooldown
            continue
        if item == 'kraken Slayer':
            # After every two normal attacks, the third normal attack deals 50 points of true damage to the enemy.
            # It has no cooldown
            continue
        if item == "Lord Dominik's Regards":
            # Normal attacks deal an additional 35% damage to enemies with a max life greater than your own.
            # It has no cooldown
            continue
        if item == "Nashor's Tooth":
            # Normal Attack deals 50 points (50 + mana * 1%) of magic damage to the enemy.
            # It has no cooldown
            continue
        if item == "Rapid Firecannon":
            """
            Accumulate points as the character moves, and when points reach 00, 
            the attack distance of the next normal attack is increased by 100 yards.
            """
            # It has no cooldown
            continue
        if item == "Runaan's Hurricane":
            """
            When the character is making a normal attack, 
            the item will actively split two arrows, dealing 30 points of magic damage to the enemy.
            """
            # It has no cooldown
            continue
        if item == 'Statikk Shiv':
            """
            Accumulates points as the character moves, and when it reaches 100 points, 
            deals an additional 100 points of magic damage to one enemy and sends out 
            a bolt of lightning that deals 50 points of magic damage to the 4 nearest enemies.
            """
            # It has no cooldown
            continue
        if item == "Wit's End":
            # Normal attacks deal 50 points of magic damage to enemies and gain 20 points of movement speed that decays to 0 over 2 seconds.
            # It has no cooldown
            continue
        if item == 'Navori Quickblades':
            # Reduces the cooldown reduction of non-ultimate skills when performing normal attacks on enemies.
            # It has no cooldown
            continue
        if item == "Guinsoo's Rageblade":
            """
            Normal attacks deal (20 + Strike Chance * 20%) magic damage to the enemy and stack 5% Attack Speed with each normal attack, 
            up to a maximum of 5.
            """
            # It has no cooldown
            continue
        if item == 'Abyssal Mask':
            # Reduces the magic resistance of neighboring enemies and gains additional magic resistance.
            # It has no cooldown
            continue
        if item == "Dead Man's Plate":
            """
            Accumulates points as the character moves, up to 100, and gains 50 additional movement speed; 
            as points increase, the next normal attack deals an equal amount of magic damage to the enemy, 
            and the accumulated points reset.
            """
            # It has no cooldown
            continue
        if item == 'Force of Nature':
            """
            When a character takes magical damage, they gain a tier of points, 
            and when the tier reaches 6, they reduce the magical damage taken by 20%.
            """
            # It has no cooldown
            continue
        if item == "Randuin's Omen":
            # Reduces 20% of physical damage taken as well as 35% of bludgeoning damage.
            # It has no cooldown
            continue
        if item == 'Spirit Visage':
            # Shield value and life recovery increased by 150%.
            # It has no cooldown
            continue
        if item == "Sterak's Gage":
            # Gain attack power proportional to current max life and 600 points of shield when life is below 40%.
            # It has a cooldown
            continue
        if item == 'Thornmail':
            # When a character is attacked by an enemy, return 20% of the damage taken in magic damage to the enemy attacking the character.
            # It has no cooldown
            continue
        if item == "Warmog's Armor":
            # Boosts max life by 50% and gains 200% additional life regen.
            # It has no cooldown
            continue
        if item == 'Frostfire Gauntlet':
            """
            When you use a skill once, after making your next normal attack, 
            it creates a circular area of slowdown and cauterizes enemies in that circular area, 
            dealing 50 points of magic damage to them.
            """
            # It has cooldown
            continue
        if item == "Jak'sSho, The Protean":
            """
            When a character takes damage, they gain points, 
            and when the number of points increases to 8, they draw blood from nearby enemies for lifesteal restoration.
            """
            # It has no cooldown
            continue
        if item == 'Heartsteel':
            # Gain a certain number of points of maximum life for each enemy killed.
            # It has no cooldown
            continue
