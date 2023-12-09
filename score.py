import pygame, globalVar

class ScoreBoard():
    def __init__(self):
        self.score = globalVar.score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Helvetica', 36)
    
    def showScore(self,x,y):
        str_score = "Score: " + str(self.score) # change int to str
        self.score_image = self.font.render(str_score, False, self.text_color) # turn str to Surface object
        self.score_rect = self.score_image.get_rect(center=(x, y)) # 获取分数图形的坐标位置
        x = self.score_rect.x
        y = self.score_rect.y
        x_win, y_win = globalVar.screen.get_size()
        x_img, y_img = self.score_image.get_size()
        image = pygame.transform.scale(self.score_image, (x_img*x_win/1600,y_img*y_win/900))
        globalVar.screen.blit(image, (x*x_win/1600, y*y_win/900))