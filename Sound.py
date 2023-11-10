import pygame
import globalVar

volm = globalVar.BGMVolume
vole = globalVar.SFXVolume

def sound_sys_init():
    globalVar.BGMVolume = 0.7
    globalVar.SFXVolume = 1

def sound_sys_init():
    globalVar.BGMVolume = 0.7
    globalVar.SFXVolume = 1

def play_music(text):
    pygame.mixer.music.load(text)
    pygame.mixer.music.set_volume(volm)
    pygame.mixer.music.play(-1)

def play_sound_effect(text):
    effect = pygame.mixer.Sound(text)
    effect.set_volume(vole)
    effect.play

def change_music(text):
    pygame.mixer.music.stop
    play_music(text)

def increase_vol(kind):
    if(kind < 1 ):
        kind += 0.1
    
def decrease_vol(kind):
    if(kind > 0):
        kind -= 0.1 