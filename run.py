from view import View
import numpy as np
import math
from life.board import Board, PointState

BOARD_WIDTH = 101
BOARD_HEIGHT = 101
BOARD_CENTER_X = math.floor(BOARD_WIDTH / 2)
BOARD_CENTER_Y = math.floor(BOARD_HEIGHT / 2)

BOARD_CELL_SIZE = 10
DEBUG = False

board = Board(BOARD_HEIGHT, BOARD_WIDTH)
population = board.get_empty_population()


# oscillator 1
# shape = [(-1,0),(0,0),(1,0)]

# glider 1
# shape = [(0,-1),(1,0),(-1,1),(0,1),(1,1)]

# die hard
shape = [(-3,0),(-3,-1),(-4,-1),(1,0),(2,0),(3,0),(2,-2)]

# spaceship
# shape = [(0,0),(1,0),(2,0),(3,0),(0,-1),(0,-2),(1,-3),(4,-3),(4,-1)]

# r-pentomino
# shape = [(0, 0), (-1, 0), (0, 1), (0, -1), (1, -1)]

for x, y in shape:
    population[BOARD_CENTER_X+x, BOARD_CENTER_Y+y] = PointState.Alive
board.populate(population)

v = View(board, BOARD_CELL_SIZE, debug=DEBUG)
v.run()
