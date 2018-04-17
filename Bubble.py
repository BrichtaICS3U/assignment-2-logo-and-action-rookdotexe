import pygame, random
WHITE = (255,255,255)

class Bubble(pygame.sprite.Sprite):
    def __init__(self,color,radius,speed):
        super().__init__()
        self.image = pygame.Surface([radius,radius])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.color = color
        self.speed = speed
        self.radisu = radius

        pygame.draw.ellipse(self.image,self.color,[0,0,radius,radius], 3)
        self.rect = self.image.get_rect()

    def Float(self, speed):
        self.rect.y -= speed 
