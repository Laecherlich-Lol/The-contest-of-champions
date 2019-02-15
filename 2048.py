import pygame
from pygame import display
from utils import *
from Board import Block

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

    testblock = Block(4, 1, 1)
    # pygame.draw.rect(board, (125, 0, 0), (160, 0, 100, 100))

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
                print(event.key)
                if event.key == pygame.K_UP:
                    testblock.y = 0

                elif event.key == pygame.K_DOWN:
                    testblock.y = Y - 1

                elif event.key == pygame.K_RIGHT:
                    testblock.x = X - 1

                elif event.key == pygame.K_LEFT:
                    testblock.x = 0
            board.fill(BOARD_COLOR)
            testblock.draw(board, BOARD_SIZE[0] / X)
            screen.blit(board, BOARD_POS)
            pygame.display.flip()

                # if event.key in (275, 274):
                # print("arrow key", event.key)





if __name__ == "__main__":
    main()



# score, record, restart