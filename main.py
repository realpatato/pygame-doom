''' MAIN - HANDLES THE GAME '''
''' IMPORTS '''
import pygame
import map

''' PYGAME SETUP '''
#initiates the pygame module
pygame.init()

#defines a width and height for the screen
screen_width = 500
screen_height = 500
#creates the screen
screen = pygame.display.set_mode((screen_width, screen_height))
#changes the caption of the screen
pygame.display.set_caption("DOOM")

''' GAME LOOP SETUP '''
#clock for controlling frame rate
clock = pygame.time.Clock()
#variable for controlling game loop
keep_playing = True

level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_map = map.Map(level, screen)

''' GAME LOOP '''
while keep_playing:
    #iterates over each possible pygame event
    for event in pygame.event.get():
        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    screen.fill((0, 0, 0))

    screen.blit(level_map._map_display, (0, 0))

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()