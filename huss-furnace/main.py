import pygame
import math
import random
import os
from smoke_particle import SmokeParticle

pygame.init()

# declaring important variables and constants
(width, height) = (400, 400)
background_color = (255, 255, 255)
smoke_particles = []
particle_number = 10
ofen_img = pygame.image.load("./huss_ofen.jpg")
ofen_img = pygame.transform.scale(ofen_img, (90, 200))
pygame.mixer.music.load("./coin-drop.mp3")

# setting up the screen
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("Räucherofen")

# create the smoke particles
def createSmoke(part_num, surface):
    for particle in range(part_num):
        particle = SmokeParticle(surface, random.randint(270, 286), 200)
        smoke_particles.append(particle)

coin_count = 0;
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    createSmoke(particle_number, screen)
    # update the screen
    screen.fill(background_color)
    screen.blit(ofen_img, (200, 200))

    # for every particle decide if delete or move and display
    for particle in smoke_particles:
        if (particle.x < 0 or particle.x > width or particle.y < 0 or particle.y > height):
            # music play
            if (coin_count == 1000):
                #pygame.mixer.music.play()
                coin_count = 0
            else:
                coin_count+=1

            smoke_particles.remove(particle)
        else:
            if (particle.y < 50):
                particle.angle += math.pi/3
            particle.move()
            particle.display()

    pygame.display.flip()

