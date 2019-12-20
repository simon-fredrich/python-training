import pygame
import math

gravity_angle = math.pi
gravity_speed = 0.3
drag = 0.999
elasticity = 0.75

def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)
    return (angle, length)


class Particle:
    def __init__(self, window, x, y, rad):
        self.window = window
        self.x = x
        self.y = y
        self.rad = rad
        self.color = (200, 0, 30)
        self.thickness = 2
        self.speed = 1.5
        self.angle = math.pi/4

    def display(self):
        pygame.draw.circle(self.window, self.color, (int(self.x),
        int(self.y)), self.rad, self.thickness)

    def move(self):
        self.speed *= drag
        (self.angle, self.speed) = addVectors(self.angle, self.speed,
        gravity_angle, gravity_speed)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        if self.x > self.window.get_width() - self.rad:
            self.x = 2 * (self.window.get_width() - self.rad) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.rad:
            self.x = 2 * self.rad - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > self.window.get_height() - self.rad:
            self.y = 2 * (self.window.get_height() - self.rad) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.rad:
            self.y = 2 * self.rad - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

