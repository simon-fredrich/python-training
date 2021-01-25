import sys, pygame
from Grid import Grid
pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
color = (100, 100, 100)

grid = Grid(size[0], size[1], screen, color)
grid.create()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

    pygame.display.flip()