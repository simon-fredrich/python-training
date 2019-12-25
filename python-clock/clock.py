import pygame
import time
import math

class Clock:
    def __init__(self, x, y, radius, degree, screen):
        self.x = x
        self.y = y
        self.degree = degree
        self.radius = radius
        self.screen = screen

    def draw(self):
        if (self.degree > 180):
            y_pos = self.y + math.tan(self.degree) * self.radius
        elif self.degree == 180:
            y_pos = self.y
        else:
            y_pos = self.y - math.tan(self.degree) * self.radius


        if (self.degree < 90 or self.degree > 270):
            x_pos = self.x + math.cos(self.degree) * self.radius
        elif self.degree == 90 or self.degree == 270:
            x_pos = self.x
        else:
            x_pos = self.x + math.cos(self.degree) * self.radius

        pygame.draw.circle(self.screen, (0, 255, 0), (self.x, self.y), self.radius)
        pygame.draw.line(self.screen, (255, 255, 0), (self.x, self.y), (x_pos, y_pos))

