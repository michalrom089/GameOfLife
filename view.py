import pygame
import numpy as np
import time
from life.life import Life
from life.board import Board, PointState


class View:
    BACKGROUND_COLOR = (220, 220, 220)
    ALIVE_COLOR = (0, 0, 0)
    DEAD_COLOR = (255, 255, 255)

    def __init__(self, board, board_cell_size, debug=False):
        pygame.init()
        self.screen_width = board.width * board_cell_size
        self.screen_height = board.height * board_cell_size
        self.board_cell_size = board_cell_size

        # setup game
        self.life = Life(board, debug=debug)

        # setup display
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.BACKGROUND_COLOR)

        self.clock = pygame.time.Clock()
        self.running = False
        self.emulation_started = False
        self.emulation_step = False

        self.print_game()
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            # Look at every event in the queue
            for event in pygame.event.get():

                # Did the user hit a key?
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("emulation step")
                        self.emulation_step = True
                    elif event.key == pygame.K_r:
                        print("emulation run")
                        self.emulation_started = True
                        time.sleep(2)
                    elif event.key == pygame.K_s:
                        print("emulation stopped")
                        self.emulation_started = False
                    elif event.key == pygame.K_ESCAPE:
                        print("escape pressed")
                        self.running = False

                elif event.type == pygame.QUIT:
                    self.running = False

            if self.emulation_started or self.emulation_step:
                self.emulation_step = False

                self.life.tick()
                self.print_game()

            pygame.display.flip()

            self.clock.tick(60)

    def print_game(self):
        for idx, val in np.ndenumerate(self.life.get_state()):
            color = self.ALIVE_COLOR if val == PointState.Alive else self.DEAD_COLOR
            self.draw_rect(idx[0], idx[1], color)

    def draw_rect(self, x, y, color):
        rect_x = (x*self.board_cell_size)+1
        rect_y = (y*self.board_cell_size)+1
        rect_size = self.board_cell_size - 2
        pygame.draw.rect(self.screen, color,
                         (rect_x, rect_y, rect_size, rect_size))

