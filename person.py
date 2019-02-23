import pygame
import matplotlib


class Person:
    def person_draw(self, screen, screensize, size, color=(0, 0, 0)):
        if size == 'small':
            pygame.draw.rect(screen, color, pygame.Rect(screensize[0]/4, screensize[1]/4, 5, 5))
            pygame.display.flip()

    # def move_self_person(self, instruction):
    #     if instruction == 'forward':
    #         for
