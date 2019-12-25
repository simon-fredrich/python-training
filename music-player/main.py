import pygame
import os

pygame.mixer.init()

# setting up screen/window
(width, height) = (400, 700)
background_color = (50, 50, 50)
caption = "Music Player"

path = input("Bitte gib den Ordner an in dem sich deine Musik befindet: ")
music_list = os.listdir("/home/simon/Musik")

screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption(caption)

for item in music_list:
    pygame.mixer.music.load(path+"/" + item)

for item in music_list:

# "gameloop"
running = True
i = 20
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False



