import pygame

class Button:
    def __init__(self, txt, pos, screen):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))
        self.screen = screen

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        pygame.draw.rect(self.screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(self.screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        self.screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False