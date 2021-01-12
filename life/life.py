from life.board import Board, PointState
from copy import deepcopy


class Life:
    def __init__(self, board, debug=False):
        """ interval_in_ms - interval between iterations
        """
        assert type(board) == Board

        self.board = board

        self.debug = debug
        self.debug_tick = debug
        self.debug_tick = debug

    def decide(self, x, y):
        population = self.board.get_neighbour_population(x, y)
        is_alive = self.board.is_alive(x, y)

        shouldLive = not is_alive and population == 3 \
                        or (is_alive and (population == 2 or population == 3))                

        future_state = PointState.Alive if shouldLive else PointState.Dead

        # if emulate and is_alive != shouldLive:
        if self.debug and is_alive != shouldLive:
            current_state = PointState.Alive if is_alive else PointState.Dead

            print(f"X:{x},Y:{y} | {current_state.name} -> {future_state.name} | population:{population}")

        return future_state

    def tick(self):
        new_board = self.board.get_empty_population()

        for x in range(self.board.width):
            for y in range(self.board.height):
                new_board[y, x] = self.decide(x, y)

        print(new_board)
        self.board.populate(new_board)
        
        if(self.debug and not self.debug_tick):
            self.debug_tick = True
        else:
            self.debug_tick = False

    def get_state(self):
        return self.board.board