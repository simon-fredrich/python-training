import pygame

class Grid:
    def __init__(self, x_num, y_num, surface, color):
        self.x_num = x_num
        self.y_num = y_num
        self.square_arr = []
        self.surface = surface
        self.color = color

    def create(self):
        for i in range(0, self.x_num+1, int(self.x_num/10)):
            for j in range(0, self.y_num+1, int(self.y_num/10)):
                pygame.draw.rect(self.surface, self.color, (i, j, int(self.x_num/10), int(self.y_num/10)), border_radius=5)