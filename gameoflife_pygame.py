from time import sleep
from random import randint
import pygame
from sys import *

pygame.init()

#Initialise the screen
xmax = 600 #Width of screen in pixels
ymax = 600 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen

def evolve_cell(alive, neighbours):
    '''
    Justify if a cell is alive or not

    Parameters
    --------
    alive
        Bool of one cell's initial living status, 1 for alive and 0 for dead 
    neighbours
        Int of number of one cell's neighbours

    Return
    -------
    final state of cell
        Bool of one cell's updated living status, 1 for alive and 0 for dead 
    '''
    return neighbours == 3 or (alive and neighbours == 2)


def count_neighbours(grid, position):
    '''
    Count the number of a cell's neighbours

    Parameters
    --------
    grid
        2-dimensions Array of the universe
    position
        Tuple (y,x) of selected cell

    Return
    -------
    count
        Int of the number of one cell's neighbours
    '''
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count


def make_empty_grid(x, y):
    '''
    Initialize an universe with dead cells

    Parameters
    --------
    x, y
        Int of the scale of initial universe 

    Return
    -------
    grid
        two-dimensional Array of initial universe
    '''
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid


def make_random_grid(x, y):
    '''
    Generate an universe with alive ceils which is randomly distributed

    Parameters
    --------
    x, y
        Int of the scale of universe with alived ceils but not envolved

    Return
    -------
    grid
        two-dimensional Array of universe with alived ceils but not envolved
    '''
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(randint(0,1))
        grid.append(row)
    return grid


def evolve(grid):
    '''
    Justify every ceil's current status and envolve the whole universe

    Parameters
    --------
    grid
        two-dimensional Array of current universe

    Return
    -------
    new_grid
        two-dimensional Array of envolved universe
    '''
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if evolve_cell(cell, neighbours) else 0
    return new_grid

BLACK = (0, 0, 0)

def draw_block(x, y, alive_color):
    '''
    Justify every ceil's current status and envolve the whole universe

    Parameters
    --------
    grid
        two-dimensional Array of current universe

    Return
    -------
    new_grid
        two-dimensional Array of envolved universe
    '''
    block_size = 9
    x *= block_size
    y *= block_size
    center_point = (int(x + (block_size / 2)), int(y + (block_size / 2)))
    pygame.draw.circle(screen, alive_color, center_point,
                       int(block_size / 2), 0)


def handleInputEvents(xlen, ylen):
    '''
    Generate a new world with alived ceils by detecting whether mouse is clicked  

    Parameters
    --------
    xlen, ylen
        Int of the scale of initial universe
    '''
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):  # left click
                global world
                world = make_random_grid(xlen, ylen)
        if(event.type == pygame.KEYDOWN):
            sys.exit(0)  # quit on any key
        if (event.type == pygame.QUIT):  # pygame issues a quit event, for e.g. by closing the window
            print("quitting")
            sys.exit(0)


def main():
    h = 0
    cell_number = 0
    alive_color = pygame.Color(0,0,0)
    alive_color.hsva = [h, 100, 100]
    xlen = xmax // 9
    ylen = ymax // 9
    global world
    world = make_random_grid(xlen, ylen)
    while True:
        # detect if generating a new world or not
        handleInputEvents(xlen, ylen)
        for x in range(xlen):
            for y in range(ylen):
                alive = world[x][y]
                cell_number += 1
                cell_color = alive_color if alive else BLACK
                draw_block(x, y, cell_color)
        pygame.display.flip()
        h = (h + 2) % 360
        alive_color.hsva = (h, 100, 100)
        world = evolve(world)
        cell_number = 0
        sleep(0.1)

if __name__ == '__main__':
    main()
