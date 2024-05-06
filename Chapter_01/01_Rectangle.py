from time import sleep
import pygame

# Initialize the pygame library
pygame.init() 

# Create a 500 x 400 px window 
window = pygame.display.set_mode((500, 400)) 

# In this part, I added a twist
# Instead of just displaying a rectangle
# I made it blink every 200 ms
while(True):
    # Draw a green rectangle (R = 0, G = 255, B = 0) of dimensions 50 x 30 px
    # at the center of the display by subtracting half of the width (=25) and length (=15) from centre (250, 200) of window
    pygame.draw.rect(window, (0, 255, 0), (250-25, 200-15, 50, 30))

    # To put the drawn shape on the screen
    pygame.display.update() 

    # Sleep for 200 ms
    sleep(0.2)

    # Just draw a black rectangle at the same place, so that the previous one becomes invisible
    pygame.draw.rect(window, (0, 0, 0), (250-25, 200-15, 50, 30))
    pygame.display.update()

    # Sleep again for 200 ms
    sleep(0.2)