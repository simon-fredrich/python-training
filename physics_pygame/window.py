import pygame
import math
from random import randint
from particle import Particle

(width, height) = (1000, 800)
background_color = (255, 0, 0)
particles = []
particle_number = 10


def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.rad:
            return p
    return None


screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("physics simulation")

for particle in range(particle_number):
    particle = Particle(screen, randint(0, screen.get_width()), randint(
        0, screen.get_height()), randint(50, 70))
    particles.append(particle)

selected_particle = None
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(particles, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1

    # experimental
    for i in particles:
        for j in particles:
            if (i != j):
                hyp = (i.x - j.x)**2+(i.y - j.y)**2
                if ((i.rad + j.rad)**2 >= hyp):
                    print("Hwllo")
                    j.angle = 0

    screen.fill(background_color)

    for particle in particles:
        particle.move()
        particle.bounce()
        particle.display()

    pygame.display.flip()
