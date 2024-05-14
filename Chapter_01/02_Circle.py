from time import sleep
from random import seed
from random import randint
from datetime import datetime
import pygame

pygame.init()
window = pygame.display.set_mode((500, 400))

while(True):
    # This time successive non filled circles with random colors with line width of 5 will be created from centre of window
    # Each increasing in size of 2 times the value of i for 100 times
    for i in range (100):
        seed(datetime.now().timestamp()) # Create more randomness by seeding with current timestamp
        pygame.draw.circle(window, (randint(0, 255), randint(0, 255), randint(0, 255)), (250, 200), i*2, 10)
        pygame.display.update()
        sleep(0.03)
        # clear the screen by drawing a black rectangle equal to display size
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 500, 400)) 
        pygame.display.update()
        sleep(0.03)
