# ICS3U
# Assignment 2: Action
# <Ahmed>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Fish import Fish 
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0,0,255)
WATER = (138, 178, 242)
    

speed = 1
colorList = (RED, GREEN, BLUE)
background = pygame.image.load("background.png") #i made this
fishes = ["fishy.png", "tigerfish.png", "glawb.png"] #i made these as well
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 4096)
pygame.mixer.music.load("underwater.mp3") #https://www.youtube.com/watch?v=yW2rmkg8c70&t=4s
pygame.mixer.music.play(-1) 


# Set the screen size
SCREENWIDTH = 800
SCREENHEIGHT = 800

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fish Tank")
all_sprites_list = pygame.sprite.Group()
moveing_fish = pygame.sprite.Group()


#Defineing all my objects
fish1 = Fish(RED, 80,60, random.randint(50,100))
fish1.rect.x = 400
fish1.rect.y = 400

fish2 = Fish(GREEN, 80,60, random.randint(50,100))
fish1.rect.x = 300
fish1.rect.y = 200

fish3 = Fish(BLUE, 80,60, random.randint(50,100))
fish1.rect.x = 200
fish1.rect.y = 300

#putting the classes in lists to make it easier to move them
all_sprites_list.add(fish1)
all_sprites_list.add(fish2)
all_sprites_list.add(fish3)
moveing_fish.add(fish1)
moveing_fish.add(fish2)
moveing_fish.add(fish3)

#clock stuff
carryOn = True
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #big money
                carryOn = False


    # --- Main logic
    all_sprites_list.update()
    for Fish in moveing_fish:
        Fish.moveRight(speed)
        if Fish.rect.x > SCREENWIDTH: #flips the sprite when it reachs the end of the screen. 
            Fish.speed *= -1          #ran into a bug because I did the same flip on both sides.
            Fish.rect.y = random.randint(50,SCREENHEIGHT)
            Fish.image = pygame.transform.flip(Fish.image, True, False) 
            Fish.image = pygame.image.load(random.choice(fishes))
            Fish.image = pygame.transform.flip(Fish.image, True, False)
        elif Fish.rect.x < -80:
            Fish.speed *= -1
            Fish.rect.y = random.randint(50,SCREENHEIGHT)
            Fish.image = pygame.transform.flip(Fish.image, True, False)
            Fish.image = pygame.image.load(random.choice(fishes))

        if pygame.mouse.get_pressed()[0]: #can drag fish around. Added this for fun 
         mousex,mousey = event.pos
         if Fish.rect.collidepoint(mousex,mousey):
             Fish.rect.x=mousex-Fish.rect.width/2
             Fish.rect.y=mousey-Fish.rect.height/2
                
    # --- Draw code goes here
    screen.fill(WATER)
    screen.blit(background, (0,0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
 
    # --- Frame rate=
    clock.tick(60)
    
pygame.quit()
