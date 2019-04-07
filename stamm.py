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
            thisgame.move(event.key)
        # thisgame.person_update()
        # print('here')



