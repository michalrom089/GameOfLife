from view import View
import numpy as np
import math
from life.board import Board, PointState

BOARD_WIDTH = 101
BOARD_HEIGHT = 101
BOARD_CENTER_X = math.floor(BOARD_WIDTH / 2)
BOARD_CENTER_Y = math.floor(BOARD_HEIGHT / 2)

BOARD_CELL_SIZE = 15
DEBUG = True

board = Board(BOARD_HEIGHT, BOARD_WIDTH)
population = board.get_empty_population()

shape = [(0, 0), (-1, 0), (0, 1), (0, -1), (1, -1)]
for x, y in shape:
    population[BOARD_CENTER_X+x, BOARD_CENTER_Y+y] = PointState.Alive
board.populate(population)

v = View(board, BOARD_CELL_SIZE, debug=DEBUG)
v.run()
