import pygame
import math
import random


class SmokeParticle:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = 0.8
        self.angle = 0/math.pi#random.uniform(-math.pi/3, math.pi/3)

    def display(self):
        pygame.draw.circle(self.screen, (150, 150, 150), (int(self.x), int(self.y)), 1, 0)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

