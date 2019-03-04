import pygame
import matplotlib


class Person:
    def __init__(self, track_num, screen, screensize):
        self.screen = screen
        self.screensize = screensize
        self.track_num = track_num

    def person_draw(self, color=(169, 36, 100)):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.screensize[0]/3*self.track_num+30, 720, 120, 120))
        pygame.display.flip()

    def move_person(self, instruction):
        if instruction == 'left':
            if self.track_num > 0:
                self.track_num -= 1
                self.person_draw()
                pygame.display.flip()
                print(self.track_num)
            else:
                pass
        elif instruction == 'right':
            if self.track_num < 2:
                self.track_num += 1
                self.person_draw()
                pygame.display.flip()
            else:
                pass
