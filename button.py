import pygame

class Button:
    def __init__(self, txt, pos, screen):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (180, 30))
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, 'light gray', self.button, 0, 2)

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False