import pygame,sys
from pygame.locals import *

def mapDraw(screen_x, screen_y):

    screen =  pygame.display.set_mode((screen_x, screen_y))
    tile = pygame.image.load("floor_tile.png")


    row = 0
    for row in range(0, screen_y, 32):
        column = 0
        for column in range(0, screen_x, 32):
            screen.blit(tile, (column, row)) 
            print(column,row)
            pygame.display.update()


def main():

    mapFloor = mapDraw(1020,760)
main()
