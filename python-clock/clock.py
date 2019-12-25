import pygame
import math

class Clock:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen

    def draw(self, degree, zeiger):
        degree = math.radians(degree)
        if degree > 180:
            y_pos = self.y + math.sin(degree) * self.radius * zeiger
        else:
            y_pos = self.y + math.sin(degree) * self.radius * zeiger


        if (degree < 90 or degree > 270):
            x_pos = self.x + math.cos(degree) * self.radius * zeiger
        else:
            x_pos = self.x + math.cos(degree) * self.radius * zeiger 
        
        return ((x_pos, y_pos))

    def drawClock(self):
        pygame.draw.circle(self.screen, (0, 255, 0), (self.x, self.y), self.radius, 1)
        
    def drawSec(self, degree, zeiger):
        pygame.draw.line(self.screen, (255, 255, 0), (self.x, self.y), self.draw(degree, zeiger))

    def drawMin(self, degree, zeiger):
        pygame.draw.line(self.screen, (255, 255, 0), (self.x, self.y), self.draw(degree, zeiger))

    def drawHour(self, degree, zeiger):
        pygame.draw.line(self.screen, (255, 255, 0), (self.x, self.y), self.draw(degree, zeiger))

    def display(self, sd, md, hd):
        self.drawClock()
        self.drawSec(sd, 1)
        self.drawMin(md, 0.75)
        self.drawHour(hd, 0.5)

