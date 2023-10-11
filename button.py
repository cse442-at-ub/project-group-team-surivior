import pygame
import globalVar

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 24)
        pygame.draw.rect(globalVar.screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(globalVar.screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        globalVar.screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

# button = Button("Quit",(0,0))
#         button.draw()
#         if button.check_clicked():
#             pygame.quit()