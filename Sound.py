import pygame

volm = 0.7
vole = 1


def play_music(text):
    pygame.mixer.music.load(text)
    pygame.mixer.music.set_volume(volm)
    pygame.mixer.music.play(-1)

def play_sound_effect(text):
    effect = pygame.mixer.Sound(text)
    effect.set_volume(vole)
    effect.play