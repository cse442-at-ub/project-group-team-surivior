import pygame
from items import *
from character import *
from Distance import *

def doran_shield():
    if distance <= 15:
        character_current_health_regen += 3

def doran_ring():
    if distance <= 15:
        enemy_health -= character_current_attack_damage + 15

def plated_shoe():
    if distance <= 15:
        character_current_health -= enemy_attack_damage*0.85

