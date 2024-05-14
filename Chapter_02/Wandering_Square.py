# This code is my attempt at combining (almost) all concepts introduced in chapter 2

import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from datetime import datetime
from time import sleep

pygame.init()
clock = pygame.time.Clock() # used for controlling frame rate

fps = 20
width = 640
length = 480
squareLength = 20
squareWidth = 20
# Align the square to the centre of the display
posX = (width / 2) - squareWidth / 2
posY = (length / 2) - squareLength / 2
# Velocities
vX = 10.0
vY = 10.0

surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Wandering Square') # To set the title of the window

while (True):

    # clear the display to draw new frame
    surface.fill((0, 0, 0))

    # Change the color of the square randomly
    random.seed(datetime.now().timestamp())
    randR = random.randint(0, 255)
    randG = random.randint(0, 255)
    randB = random.randint(0, 255)

    # Draw the square on surface
    pygame.draw.rect(surface, (randR, randG, randB), (posX, posY, squareWidth, squareWidth))

    # Update the position randomly for next frame and keep within bounds of screen with random floating point numbers 
    vX = random.uniform(-squareWidth, squareWidth)
    vY = random.uniform(-squareLength, squareLength)
    posX += vX
    posY += vY
    if posX > width or posX < 0:
        posX = random.randint(0, width)
    if posY > length or posY < 0:
        posY = random.randint(0, length)

    # Check if user presses exit button and exit accordingly
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    # Render the drawn square on display
    pygame.display.update()
    clock.tick(fps) # control frames per second to value set in fps variable
