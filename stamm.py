import pygame
import person

SCREEN = (540, 960)

TRACK = (SCREEN[0]/3, SCREEN[1])
pygame.init()
logo = pygame.image.load('images.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption('run')

screen = pygame.display.set_mode((SCREEN))
pygame.display.flip()


me = person.Person(1, screen, SCREEN)
me.person_draw()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                me.move_person('left')
            if event.key == pygame.K_RIGHT:
                me.move_person('right')
