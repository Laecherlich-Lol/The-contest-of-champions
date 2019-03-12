import pygame
import game

thisgame = game.Game()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                thisgame.me.move_person('left')
            if event.key == pygame.K_RIGHT:
                thisgame.me.move_person('right')
        thisgame.update()

