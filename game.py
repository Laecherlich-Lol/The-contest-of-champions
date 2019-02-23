import pygame
from pygame import display
from utils import *
from Board import Board

# x, y axis block number


# screen
SCREEN_SIZE = (680, 680)
BACKGROUND_COLOR = (255,255,255)

# board
BOARD_COLOR = (125, 125, 125)
# BOARD_POS = (100, 200, 400, 400)
BOARD_SIZE = (400, 400)
BOARD_POS = (100, 200)

# info
SCORE_POS = (20, 20, 100, 100)
RECORD_POS = (160, 20, 100, 100)


class Game:
    def __init__(self, n_row, n_col, n_block, logo_name="pig.png", caption="piggy2048"):
        # initialization
        pygame.init()

        # load and set the logo
        self.logo = pygame.image.load(logo_name)
        self.logo.set_colorkey((255, 255, 255))  # make logo proper
        display.set_icon(self.logo)
        display.set_caption(caption)

        # create a surface on screen that has the size of 240 x 180
        self.screen = display.set_mode(SCREEN_SIZE)
        self.screen.fill(BACKGROUND_COLOR)

        draw_info(self.screen, "Record", 2048, RECORD_POS)
        # pygame.draw.rect(screen, BOARD_COLOR, BOARD_POS)
        self.board = pygame.Surface(BOARD_SIZE, pygame.SRCALPHA, 32)
        self.board.fill(BOARD_COLOR)

        self.base = Board(self.board, n_row, n_col)
        # blocks = [Block(random.choice([2, 4, 8]), rint(0, X-1), rint(0, Y-1)) for i in range(5)]
        for i in range(n_block):
            self.base.duang()
        # base.add_blocks(blocks)
        pygame.display.flip()

    def update(self):
        self.board.fill(BOARD_COLOR)
        self.base.draw_blocks()
        draw_info(self.screen, "Score", self.base.get_score(), SCORE_POS)

        self.screen.blit(self.board, BOARD_POS)
        pygame.display.flip()





