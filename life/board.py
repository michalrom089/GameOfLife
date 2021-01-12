import numpy as np
from enum import Enum


class PointState(Enum):
    Dead = 0
    Alive = 1


class Board:

    def __init__(self, height, width):
        # +2 for margins (to easily count get_neighbour_populationMatrix)
        self.height = height
        self.width = width
        self._board = np.full((height+2, width+2),
                              PointState.Dead, dtype=object)

    @property
    def board(self):
        return self._board[1:self.height+1, 1:self.width+1]

    def populate(self, population):
        assert type(population) == np.ndarray
        assert population.shape == (self.height, self.width)
        assert population.dtype == object

        # self.board = population
        self._board[1:self.height+1, 1:self.width+1] = population

    def is_alive(self, x, y):
        assert x >= 0 and x < self.width
        assert y >= 0 and y < self.height

        return self.board[y, x] == PointState.Alive

    def set_state(self, x, y, state):
        assert x >= 0 and x < self.width
        assert y >= 0 and y < self.height

        self._board[y+1, x+1] = state

    def get_neighbour_population(self, x, y):
        # accunt on margins
        x = x+1
        y = y+1

        assert x >= 1 and x <= self.width
        assert y >= 1 and y <= self.height

        neighbourhood_map = np.full((3, 3), PointState.Alive, dtype=object)
        neighbourhood_map[1, 1] = self._board[y, x]
        neighbourhood = self._board[y-1:y+2, x-1:x+2]

        return np.sum(neighbourhood_map == neighbourhood)-1

    def get_empty_population(self):
        return np.full((self.height, self.width), PointState.Dead, dtype=object)
