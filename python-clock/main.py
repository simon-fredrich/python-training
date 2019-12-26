import pygame
import clock
import math
from time import localtime, strftime

pygame.init()
(width, height) = (800, 800)
background_color = (150, 150, 150)
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("python-clock")
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("The Python Clock", True, (0, 128, 0))


# creating objects
clock_arr = []
i = 0
j = 0
for row in range(0, 4):
    clock_arr.append(clock.Clock(int(width/8)+i, int(width/8), int(width/8), screen))
    for col in range(0, 4):
        clock_arr.append(clock.Clock(int(width/8)+i, int(height/8)+j, int(width/8), screen))
        j += int(width/4)
    i += int(width/4)
    j = 0

print(len(clock_arr))

sec360min = []
hour2degree = []
for item in range(-90, 270, 6):
    sec360min.append(item)

for item in range(-60, 300, 30):
    hour2degree.append(item)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    second = sec360min[int(strftime("%S", localtime()))]
    minute = sec360min[int(strftime("%M", localtime()))]
    hour = int(strftime("%H", localtime()))
    if hour > 12:
        hour -= 12
        hour = hour2degree[hour]
    else:
        hour = hour2degree[hour-1]
    screen.fill(background_color)
    for clock in clock_arr:
        clock.display(second, minute, hour)

    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
