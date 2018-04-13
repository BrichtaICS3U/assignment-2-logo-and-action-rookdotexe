# ICS3U
# Assignment 2: Logo
# <Ahmed Abdulwahab>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
import math  
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GWEEN = (129, 210, 169)
RED = (255, 0, 0)
BROWN = (106, 69, 60)
PALE = (235, 225, 220)
BLUE = (71, 155, 251)
DARK = (61, 58, 53) 
MIDBLACK = (52, 52, 52) 
YELLOW = (255, 207, 58) 
WED = (253, 59, 96)
GRAY = (182, 172, 170)

# Set the screen size (please don't change this)
SCREENWIDTH = 399 #i am rebel man
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Old IG logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here
    
    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    pygame.draw.rect(screen, PALE, [10, 80, 380, 300], 0) #this is the lower bit of the camera
    pygame.draw.rect(screen, BROWN, [10, 10, 380, 100], 0) #this is the top brown bit of the camera

    #right camera curve
    pygame.draw.rect(screen, WHITE, [365, 10, 50, 50], 0)
    pygame.draw.ellipse(screen, BROWN, [340,10,50,50],0)
    pygame.draw.rect(screen, BROWN, [340,39,50,50],0)
    
    #left camera curve 
    pygame.draw.rect(screen, WHITE, [10, 10, 50, 50], 0)
    pygame.draw.ellipse(screen, BROWN, [10,10,50,50],0)
    pygame.draw.rect(screen, BROWN, [10,39,50,50],0)
    pygame.draw.rect(screen, BROWN, [30,10,50,10],0)
    
    pygame.draw.rect(screen, BLACK, [325, 45, 55,55],0) #this is the bit where the flash would come out of
    pygame.draw.rect(screen, BLUE, [100, 20, 20, 90], 0) #blue stripe
    pygame.draw.rect(screen, GWEEN, [80, 20, 20, 90], 0) #green stripe
    pygame.draw.rect(screen, YELLOW, [60, 20, 20, 90],0) #yellow stripe
    pygame.draw.rect(screen, WED, [40, 20,20,90], 0) #red stripe
    pygame.draw.rect(screen, MIDBLACK, [40, 100, 80, 30] , 0) #all the stripes touch this bit
    pygame.draw.ellipse(screen, MIDBLACK, [130, 150, 150, 150],0) #apature
    pygame.draw.ellipse(screen, BLACK,[125, 145, 160,160], 20) #outter bit of the aperture. I really don't know camera part names...
    pygame.draw.ellipse(screen, GRAY,[115, 135, 180,180], 15)
    
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
