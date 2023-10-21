import pygame

def play_music(text):
    pygame.mixer.music.load(text)
    pygame.mixer.music.play()

def play_sound_effect(text):
    effect = pygame.mixer.Sound(text)
    effect.play