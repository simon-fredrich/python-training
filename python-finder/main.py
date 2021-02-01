import sys, pygame
from Grid import Grid
from Tile import *
import random
pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
color = (100, 100, 100)

# grid = Grid(size[0], size[1], screen, color)
# grid.create()

tiles = []
tile_width = 30
tile_height = 30
x_quant = int(width/tile_width)
y_quant = int(height/tile_height)

find_object = random.randint(0, 500)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    x_tile = 0
    y_tile = 0

    for i in range(x_quant):
        for j in range(y_quant):
            tile = Tile(screen, color, x_tile, y_tile, tile_width, tile_height)
            tile.draw()
            tiles.append(tile)
            y_tile = y_tile + 30

        x_tile = x_tile + 30
        y_tile = 0
        
    tiles[find_object].color = [200, 0, 0]
    tiles[find_object].draw()

    for tile in tiles:
        if tile.color == [200, 0, 0]:
            tile.color = [0, 0, 200]
            tile.draw()
            break
        else: 
            tile.color = [0, 200, 0]
            tile.draw()

    

    pygame.display.flip()