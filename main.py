#multiplcation by k % 100
# 2 < k < 51
# 100 equally spaced dots on circle labeled 0-99
#for k in range (2, 52)
    #draw corcle
    #For i in range(0, 100)
        #draw line in corcle
#percentage around circle to coordinate
#100 -> radians


#PADDING, RADIUS
#Circle 1 coords = (padding + radius, padding + radius)
# circle 2 cords = (2 padding + 2 radius, padding + radius)
# circleX = k%5 + 1
# circleY = k//10 + 1
import math

PADDING = 10
RADIUS = 35
ROW_LENGTH = 10
SCREEN_RATIO = 2/1
SCREEN_X = PADDING * (ROW_LENGTH + 1) + (2 * RADIUS * ROW_LENGTH)
SCREEN_SIZE = (SCREEN_X, SCREEN_X / SCREEN_RATIO)

import pygame
pygame.init()
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode(SCREEN_SIZE)  # creates game screen
screen.fill((0, 0, 0))
clock = pygame.time.Clock()  # set up clock
gameover = False  # variable to run our game loop


while not gameover:  # GAME LOOP############################################################
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

    screen.fill((0,0,0))
    for k in range(2,52):
        circleNum = k-2
        xOffset = (circleNum%ROW_LENGTH) + 1
        yOffset = (circleNum//ROW_LENGTH) + 1
        x = (xOffset * PADDING) + ((xOffset - .5) * RADIUS * 2)
        y = (yOffset * PADDING) + ((yOffset - .5) * RADIUS * 2)
        oldTheta = 0
        pygame.draw.circle(screen,(255,255,255),(x, y), RADIUS, 1)
        for i in range(1,100):
            theta = (2 * math.pi) * (i / 100)
            thetaB = (2 * math.pi) * ((i * k % 100) / 100)
            startPos = (RADIUS * math.cos(theta) + x, RADIUS * math.sin(theta) + y)
            endPos = (RADIUS * math.cos(thetaB) + x, RADIUS * math.sin(thetaB) + y)
            pygame.draw.line(screen, (255,255,255), startPos, endPos, 1)
    pygame.display.flip()

    

# end game loop------------------------------------------------------------------------------
pygame.quit()