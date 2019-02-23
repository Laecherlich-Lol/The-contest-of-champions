import pygame
from utils import *
import game

X = 4
Y = 4
INIT_BLOCK = 5


def main():


    mygame = game.Game(X, Y, INIT_BLOCK)
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
                    mygame.base.move_blocks("up")

                elif event.key == pygame.K_DOWN:
                    mygame.base.move_blocks("down")

                elif event.key == pygame.K_RIGHT:
                    mygame.base.move_blocks("right")

                elif event.key == pygame.K_LEFT:
                    mygame.base.move_blocks("left")

        mygame.update()


if __name__ == "__main__":
    main()

