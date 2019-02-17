import pygame
from pygame import display
from utils import *
from Board import Block
from Board import Board
from random import randint as rint
import random
# x, y axis block number
X = 4
Y = 4

# screen
SCREEN_SIZE = (680, 680)
BACKGROUND_COLOR = (255,255,255)

# board
BOARD_COLOR = (125, 125, 0)
# BOARD_POS = (100, 200, 400, 400)
BOARD_SIZE = (400, 400)
BOARD_POS = (100, 200)

# info
SCORE_POS = (20, 20, 100, 100)
RECORD_POS = (160, 20, 100, 100)


def main():
    # initialization
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("pig.png")
    logo.set_colorkey((255,255,255)) # make logo proper
    display.set_icon(logo)
    display.set_caption("piggy2048")

    # create a surface on screen that has the size of 240 x 180
    screen = display.set_mode(SCREEN_SIZE)
    screen.fill(BACKGROUND_COLOR)

    draw_info(screen, "Score", 20, SCORE_POS)
    draw_info(screen, "Record", 2048, RECORD_POS)
    # pygame.draw.rect(screen, BOARD_COLOR, BOARD_POS)
    board = pygame.Surface(BOARD_SIZE, pygame.SRCALPHA, 32)
    board.fill(BOARD_COLOR)

    blocks = [Block(random.choice([2, 4, 8]), rint(0, X-1), rint(0, Y-1)) for i in range(5)]
    base = Board(board, 4, 4)
    base.add_blocks(blocks)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets  all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                # change the value to False, to exit the main loop
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    base.move_blocks("up")

                elif event.key == pygame.K_DOWN:
                    base.move_blocks("down")

                elif event.key == pygame.K_RIGHT:
                    base.move_blocks("right")

                elif event.key == pygame.K_LEFT:
                    base.move_blocks("left")

        board.fill(BOARD_COLOR)
        base.draw_blocks()

        screen.blit(board, BOARD_POS)
        pygame.display.flip()

if __name__ == "__main__":
    main()

