import pygame

def play_music(text):
    pygame.mixer.music.load(text)
    pygame.mixer.music.play()