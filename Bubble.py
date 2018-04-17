import pygame, random
WHITE = (255,255,255)

class Bubble(pygame.sprite.Sprite):
    def __init__(self,color,radius,speed):
        super().__init__()
        self.image = pygame.Surface([radius,radius])
        self.image.fill(WHITE)

        self.color = color
        self.speed = speed
        self.radisu = radius

        pygame.draw.rect(self.image,self.color,[0,0,radius,radius])
        self.rect = self.image.get_rect()

    def Float(self, speed):
        self.rect.y -= speed 
