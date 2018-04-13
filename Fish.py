import pygame, random
WHITE = (255,255,255)

class Fish(pygame.sprite.Sprite):

    def __init__(self,color,width,height,speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        #pygame.draw.rect(self.image,color, [0,0,width,height])
        fishes = ["fishy.png", "tigerfish.png", "glawb.png"]
        self.image = pygame.image.load(random.choice(fishes))
        self.rect = self.image.get_rect()

    def moveRight(self,speed):
        self.rect.x +=self.speed* speed / 20
