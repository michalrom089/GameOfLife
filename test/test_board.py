import pytest
import numpy as np
from life.board import Board, PointState


def test_board_type():
    # Assign
    b = Board(10, 10)

    # Act

    # Assert
    assert (b.board == PointState.Dead).all()
    assert type(b.board[0, 0]) == type(PointState.Dead)


def test_populate():
    # Assign
    b = Board(10, 10)
    p = np.full((10, 10), PointState.Dead, dtype=object)
    alive_points = [(0, 0), (9, 0), (0, 9), (9, 9), (4, 4), (5, 4), (2, 3)]
    for y, x in alive_points:
        p[y, x] = PointState.Alive

    # Act
    b.populate(p)

    # Assert
    assert b.board.shape == p.shape
    assert all([b.board[y, x] == PointState.Alive for y, x in alive_points])


def test_get_state():
    # Assign
    b = Board(10, 10)
    p = np.full((10, 10), PointState.Dead, dtype=object)
    alive_points = [(0, 0), (9, 0), (0, 9), (9, 9), (4, 4), (5, 4), (2, 3)]
    for y, x in alive_points:
        p[y, x] = PointState.Alive

    # Act
    b.populate(p)

    # Assert
    assert all([b.is_alive(x, y) for y, x in alive_points])

    with pytest.raises(AssertionError):
        b.is_alive(-1, -1)
    with pytest.raises(AssertionError):
        b.is_alive(10, 10)


def test_set_state():
    # Assign
    b = Board(10, 10)
    p = np.full((10, 10), PointState.Dead, dtype=object)
    alive_points = [(0, 0), (9, 0), (0, 9), (9, 9), (4, 4), (5, 4), (2, 3)]

    # Act
    for y, x in alive_points:
        b.set_state(x, y, PointState.Alive)

    # Assert
    assert all([b.board[y, x] == PointState.Alive for y, x in alive_points])

    with pytest.raises(AssertionError):
        b.set_state(-1, -1, PointState.Dead)
    with pytest.raises(AssertionError):
        b.set_state(10, 10, PointState.Dead)


def test_get_neighbour_population():
    # Assign
    b = Board(10, 10)
    p = np.full((10, 10), PointState.Dead, dtype=object)
    alive_points = [(3, 2), (4, 2), (2, 3), (3, 3), (3, 4)]
    for x, y in alive_points:
        p[y, x] = PointState.Alive

    b.populate(p)

    # Assert
    assert b.get_neighbour_population(3, 3) == 4
    assert b.get_neighbour_population(2, 2) == 3
    assert b.get_neighbour_population(0, 0) == 0
