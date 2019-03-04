import pygame
from utils import *
import game
import sys
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--X', type=int, default=4, help='the row of the board')
    parser.add_argument('--Y', type=int, default=4, help='the column of the board')
    parser.add_argument('--INIT-BLOCK', type=int, default=4, help='the number of blocks')

    args, remaining_argv = parser.parse_known_args()

    X = args.X
    Y = args.Y
    assert X == Y
    INIT_BLOCK = args.INIT_BLOCK

    mygame = game.Game(X, Y, INIT_BLOCK)
    # define a variable to control the main loop
    running = True
    status = True
    # main loop
    while running:
        # event handling, gets  all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                # change the value to False, to exit the main loop
                mygame.record()
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    status = mygame.base.move_blocks("up")

                elif event.key == pygame.K_DOWN:
                    status = mygame.base.move_blocks("down")

                elif event.key == pygame.K_RIGHT:
                    status = mygame.base.move_blocks("right")

                elif event.key == pygame.K_LEFT:
                    status = mygame.base.move_blocks("left")

        mygame.update(status)


if __name__ == "__main__":
    main()

