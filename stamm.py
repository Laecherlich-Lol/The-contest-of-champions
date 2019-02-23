import pygame
import person

SCREEN = (1080, 720)

GROUND_COLOR = (155, 155, 155)
GROUND_SIZE = (1080, 240)
GROUND_POS = (0, SCREEN[1]-GROUND_SIZE[1])

BACKGROUND_COLOR = (125, 0, 255)
BACKGROUND_SIZE = (1080, SCREEN[1]-GROUND_SIZE[1])
BACKGROUND_POS = (0, 0)

pygame.init()
logo = pygame.image.load('246x0w.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption('FIGHT')

screen = pygame.display.set_mode((SCREEN))
pygame.draw.rect(screen, (GROUND_COLOR), pygame.Rect((GROUND_POS), (GROUND_SIZE)))
pygame.draw.rect(screen, (BACKGROUND_COLOR), pygame.Rect((BACKGROUND_POS), (BACKGROUND_SIZE)))
pygame.display.flip()


me = person.Person()
me.person_draw(screen, SCREEN, 'small')

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
