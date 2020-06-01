import pygame
import color_constants


# Initiate pygame, as important as import
pygame.init()

# Make variables for game screen size
display_width = 800
display_height = 600

# Color definitions
black = color_constants.colors['black']
white = color_constants.colors['white']
red = color_constants.colors['red1']




# Set the Display Window size, 
# It takes a Tuple as an argument, which is why it's in double parantheses
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set the Window Caption
pygame.display.set_caption('Passing the Board')

# Initiate the clock
# TODO look into how this works
clock = pygame.time.Clock()

# Set the parameter to end the game
gameEnded = False

# Start the game loop - Important for window display
while not gameEnded:

    for event in pygame.event.get():
        # If the 'X' in the top is clicked, end the game
        if event.type == pygame.QUIT:
            gameEnded = True
        
        #print(event)
    # Update the display 
    # Can also use .flip() 
    # TODO Look into flip vs update
    pygame.display.update()

    # Define the FPS of the clock
    # To be fast but smooth, increase the FPS
    clock.tick(60)

# We have to un-initiate pygame
pygame.quit()
# We have to quite python?
#quit()


