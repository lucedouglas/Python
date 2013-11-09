import pygame,sys
from pygame.locals import *

pygame.init()

#Global Variables
screen_x = 800
screen_y = 480
screen =  pygame.display.set_mode((screen_x, screen_y))
x_coordinate = 0
y_coordinate = 0
moveX, moveY = 0, 0


#This function will take the screen coordinates and draw
#a tile to the entire screen. It will draw tiles no matter
#the screen size.

def keyMoveSprite():
    sprite = pygame.image.load("character.png").convert_alpha()
    global x_coordinate, y_coordinate, moveX, moveY
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveX = -.1
            elif event.key == K_RIGHT:
                moveX = +.1
            elif event.key == K_UP:
                moveY = -.1
            elif event.key == K_DOWN:
                moveY = +.1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveX = 0
            elif event.key == K_RIGHT:
                moveX = 0
            elif event.key == K_UP:
                moveY = 0
            elif event.key == K_DOWN:
                moveY = 0

    x_coordinate = x_coordinate + moveX
    y_coordinate = y_coordinate + moveY

    screen.blit(sprite,(x_coordinate, y_coordinate))
    pygame.display.update()
    print("Character drawn at:", x_coordinate, y_coordinate)


def mapDraw(screen_x, screen_y):

    

    floor = pygame.image.load("floor_tile.png")
    wall = pygame.image.load("wall_tile.png")
    treasure = pygame.image.load("treasure_chest.png")

# Intialize row for loop
    row = 0
    mapColumn = 0
    mapRow = 0

#Loop between the values 0 to the screen's y variable, in intervals of
#32, and store them in the variable row once per loop.

    mapArray = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
  

    for row in range(0, screen_y, 32):
        column = 0 # Set column to 0 per iteration, this allows reset of the x coordinate
        print("Map Row Value:", mapRow)
        mapColumn = 0 # Resets mapColumn variable to 0
        for column in range(0, screen_x, 32):

            if mapArray[mapRow][mapColumn] == 0:
                
                screen.blit(floor, (column, row)) 
                #print(column,row)
                pygame.display.update()
                #print("Map Column Value:",mapColumn)
                print("MapCol",mapColumn,"MapRow",mapRow)

            elif mapArray[mapRow][mapColumn] == 1:
                screen.blit(wall, (column, row))
                pygame.display.update()





            
                
            mapColumn = mapColumn + 1
                
        mapRow = mapRow + 1

                
def main():
    
    mapFloor = mapDraw(800,480)
    while True:

        keyMoveSprite()

main()
