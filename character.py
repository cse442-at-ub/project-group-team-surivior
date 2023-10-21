import pygame
from items import *
from item_synthesis import *
from Distance import *


character = {}

#Character Basic Attributes
character['yasuo'] = [
    #health 0
    650,
    #Growing Attack Health 1
    50,
    #mana 2
    400,
    #Growing Attack Mana 3
    30,
    #attack damage 4
    68,
    #Growing Attack Power 5
    5,
    #ability power 6
    0,
    #attack speed 7
    0.75, # Attacks per second
    #Growing Attack Speed 8
    0.08,
    #Movement 9
    325,
    #critical strike chance 10
    0.00,
    #armor 11
    30,
    #Growing Attack Armor 12
    3,
    #magic resistance 13
    25,
    #Growing Attack Magic Resistance 14
    2,
    #lethality 15
    0,
    #armor penetration 16
    0.00,
    #magic penetration 17
    0.00,
    #ability haste 18
    0,
    #lifesteal 19
    0.00,
    #omnivamp 20
    0.00,
    #health regen 21
    1.5,
    #Growing Attack Health Regen 22
    0.5,
    #mana regen 23
    0.8,
    #Growing Attack Mana Regen 24
    0.3,
    #Level 25
    1,
    #exp tp next level 26
    300,
    #normal attack with magic damage 27
    0
]

character_current_health = character['yasuo'][0]
character_Growing_Attack_Health = character['yasuo'][1]
character_current_mana = character['yasuo'][2]
character_Growing_Attack_Mana = character['yasuo'][3]
character_current_attack_damage = character['yasuo'][4]
character_Growing_Attack_Power = character['yasuo'][5]
character_current_ability_power = character['yasuo'][6]
character_current_attack_speed = character['yasuo'][7]
character_Growing_Attack_Speed = character['yasuo'][8]
character_current_Movement = character['yasuo'][9]
character_current_critical_strike_chance = character['yasuo'][10]
character_current_armor = character['yasuo'][11]
character_Growing_Attack_Armor = character['yasuo'][12]
character_current_magic_resistance = character['yasuo'][13]
character_Growing_Attack_Magic_Resistance = character['yasuo'][14]
character_current_lethality = character['yasuo'][15]
character_current_armor_penetration = character['yasuo'][16]
character_current_magic_penetration = character['yasuo'][17]
character_current_ability_haste = character['yasuo'][18]
character_current_lifesteal = character['yasuo'][19]
character_current_omnivamp = character['yasuo'][20]
character_current_health_regen = character['yasuo'][21]
character_Growing_Attack_Health_Regen = character['yasuo'][22]
character_current_mana_regen = character['yasuo'][23]
character_Growing_Attack_Mana_Regen = character['yasuo'][24]
character_current_level = character['yasuo'][25]
character_exp = character['yasuo'][26]
character_normal_attack_with_magic_damage = character['yasuo'][27]

character_current_exp = 0

# enemy basic attributes
enemy = {}

enemy['Baron'] = [
    #health 0
    300,
    #attack damage 1
    30,
    #armor
    20,
    #magic resistance
    15
]
enemy_health = enemy['Baron'][0]
enemy_attack_damage = enemy['Baron'][1]
enemy_armor = enemy['Baron'][2]
enemy_magic_resistance = enemy['Baron'][3]

kill_enemy_get_exp = 20
use_skill = False

def kill_enemy():
    while enemy_health > 0:
        if distance <= 15:
            enemy_health -= character_current_attack_damage
        return False
    return True

def cost_mana():
    if_cost_mana = False
    if kill_enemy() == True:
        if_cost_mana = True
        character_current_mana *= 0.8

    return if_cost_mana

def cost_health():
    if_cost_health = False
    if kill_enemy() == True:
        if_cost_health = True
        character_current_health -= enemy_attack_damage
    return if_cost_health

def upgrade():
    if kill_enemy() == True:
        character_current_exp += kill_enemy_get_exp
    if character_current_exp == character_exp:
        character_current_level += 1
        return True
    return False

def if_move():
    character_x, character_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    prev_character_x, prev_character_y = character_x, character_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_current_Movement
    if keys[pygame.K_RIGHT]:
        character_x += character_current_Movement
    if keys[pygame.K_UP]:
        character_y -= character_current_Movement
    if keys[pygame.K_DOWN]:
        character_y += character_current_Movement

    if (character_x, character_y) != (prev_character_x, prev_character_y):
        return True
    return False