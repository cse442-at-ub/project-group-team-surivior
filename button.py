import pygame, globalVar

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

def mainMenu():
    b_Document = Button("Document",(69,795),globalVar.screen)
    b_NewGame = Button("NewGame",(396,795),globalVar.screen)
    b_Continue = Button("Continue",(716,795),globalVar.screen)
    b_Config = Button("Config",(1052,795),globalVar.screen)
    b_Config.button = pygame.rect.Rect((b_Config.pos[0], b_Config.pos[1]), (130, 30))
    b_Exit = Button("Exit",(1348,795),globalVar.screen)
    
    return b_Document, b_NewGame, b_Continue, b_Config, b_Exit