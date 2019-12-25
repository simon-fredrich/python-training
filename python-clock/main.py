import pygame

pygame.init()

(width, height) = (400, 400)
background_color = (150, 150, 150)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("python-clock")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
