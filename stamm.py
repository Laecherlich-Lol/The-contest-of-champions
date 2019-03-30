import pygame
import game

thisgame = game.Game()
running = True

last = 0
while running:
    start = pygame.time.get_ticks()
    # print(start, last)
    if (start-last)/25 >= 1:
        thisgame.update()
        last = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                thisgame.me.move_person('left')
            if event.key == pygame.K_RIGHT:
                thisgame.me.move_person('right')
        thisgame.person_update()
        # print('here')



