import pygame
import time

class Clock:
    def __init__(self, x, y, radius, minute, hour, end_pos, surface):
        self.x = x
        self.y = y
        self.minute = minute
        self.hour = hour
        self.radius = radius
        self.end_pos = end_pos

    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0, 70), (400, 400), 150)
        pygame.draw.line(screen, (0, 255, 0), (400, 400), end_pos)

    def update(self):

