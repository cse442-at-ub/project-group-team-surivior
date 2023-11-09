import pygame, globalVar

class ScoreBoard():
    def __init__(self):
        self.score = globalVar.score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Helvetica', 48)
    
    def showScore(self):
        str_score = "Score: " + str(self.score) # change int to str
        self.score_image = self.font.render(str_score, False, self.text_color) # turn str to Surface object
        globalVar.screen.blit(self.score_image,(0,0))