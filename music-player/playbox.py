import pygame

class Playbox:
    def __init__(self, y):
        self.y = y
        self.height = 20
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (20, y, 40, self.height))


    def detectMouse(self):
        (mouseX, mouseY ) = pygame.mouse.get_pos()
