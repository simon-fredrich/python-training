import pygame
import clock
import math
from time import localtime, strftime


(width, height) = (400, 400)
background_color = (150, 150, 150)
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
pygame.display.set_caption("python-clock")

# initializing clock Class
clock_one = clock.Clock(200, 200, 150, screen)

sec360min = []
hour2degree = []
for item in range(-90, 270, 6):
    sec360min.append(item)

for item in range(-90, 270, 30):
    hour2degree.append(item)


print(hour2degree)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    second = sec360min[int(strftime("%S", localtime()))]
    minute = sec360min[int(strftime("%M", localtime()))]
    hour = int(strftime("%H", localtime()))
    if (int(strftime("%H", localtime())) > 12):
        hour -= 12
        hour = hour2degree[hour]

    screen.fill(background_color)
    clock_one.display(second, minute, hour)

    pygame.display.flip()
