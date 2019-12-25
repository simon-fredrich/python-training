import pygame
import clock

pygame.init()

(width, height) = (800, 800)
background_color = (150, 150, 150)

screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("python-clock")
clock_one = clock.Clock(200, 200, 100, 300, screen)

degree_list = []
for degree in range(0, 360, 6):
    degree_list.append(degree)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock_one.draw()


    pygame.display.flip()
