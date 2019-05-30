import pygame
import game
import math

thisgame = game.Game()
running = True
base_time = None
last = 0
while running:
    start = pygame.time.get_ticks()
    # print(start, last)
    if (start-last)/25 >= 1:
        thisgame.update()
        last = pygame.time.get_ticks()
    running = thisgame.check_ob(thisgame.me.pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            thisgame.move(event.key)
            if event.key == pygame.K_UP and thisgame.me.status is not 'fly':
                base_time = pygame.time.get_ticks()
                print('get base time')
                thisgame.me.status = 'fly'
    if thisgame.me.status is 'fly':
        # print('b')
        if pygame.time.get_ticks() - base_time > 100 and thisgame.default == 0:
            print('v')
            thisgame.me.status = 'run'
        else:
            # print(int(((pygame.time.get_ticks() - base_time) - math.sqrt(1))**2 + 1),
            #       pygame.time.get_ticks() - base_time,
            #       thisgame.me.dev)
            # thisgame.default = int(-3.0*((pygame.time.get_ticks() - base_time)/120.0 - math.sqrt(20))**2 + 20)
            dt = (pygame.time.get_ticks() - base_time)/1000.0
            thisgame.default = int(-80*dt**2 + 80 * dt)
            print(pygame.time.get_ticks(), base_time, thisgame.default)
            thisgame.me.move_person('up',
                                    default=thisgame.default)



