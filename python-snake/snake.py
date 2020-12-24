import pygame
import sys
pygame.init()

pygame.key.set_repeat(1, 50)

groeße = width, height = 800, 800
geschwindigkeit = [1,1]
# Minze
hintergrund = 102, 255, 204
# weiße Schokoloade
schlangenfarbe = 255, 255, 255
# Größe
schlangengroeße = 0, 0, 50, 50

fenster = pygame.display.set_mode(groeße)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("links")
                lst = list(schlangengroeße)
                lst[0] -= 10
                schlangengroeße = tuple(lst)
            if event.key == pygame.K_RIGHT:
                print("rechts")
                lst = list(schlangengroeße)
                lst[0] += 10
                schlangengroeße = tuple(lst)
            if event.key == pygame.K_UP:
                print("oben")
                lst = list(schlangengroeße)
                lst[1] -= 10
                schlangengroeße = tuple(lst)
            if event.key == pygame.K_DOWN:
                print("unten")
                lst = list(schlangengroeße)
                lst[1] += 10
                schlangengroeße = tuple(lst)

    fenster.fill(hintergrund)
    pygame.draw.rect(fenster, schlangenfarbe, schlangengroeße)
    pygame.display.flip()

