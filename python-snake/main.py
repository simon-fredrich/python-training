import sys, pygame
pygame.init()

size = width, height = 1500, 800
speed = [1, 2]
speed2 = [0.5, 1.3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball2 = pygame.image.load("ball2.png")
ball3 = pygame.image.load("ball3.png")

ballrect2 = ball2.get_rect()
ballrect3 = ball3.get_rect()

counter = 0
schweif = 100
    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect2 = ballrect2.move(speed)
    ballrect3 = ballrect3.move(speed2)
    if ballrect2.left < 0 or ballrect2.right > width:
        speed[0] = -speed[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed[1] = -speed[1]
        
    if ballrect3.left < 0 or ballrect3.right > width:
        speed2[0] = -speed2[0]
    if ballrect3.top < 0 or ballrect3.bottom > height:
        speed2[1] = -speed2[1]

    if (counter < schweif):
        counter += 1
    if (counter == schweif):
        screen.fill(black)
        counter = 0

    screen.blit(ball2, ballrect2)
    screen.blit(ball3, ballrect3)
    pygame.display.flip()
