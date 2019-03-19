import pygame
import person
import Track


class Game:
    def __init__(self, screen=(540, 960)):
        self.SCREEN = screen
        pygame.init()
        self.logo = pygame.image.load('images.jpg')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('run')

        self.screen = pygame.display.set_mode(self.SCREEN)
        Track.generate_track(self.screen, self.SCREEN)
        pygame.display.flip()

        self.me = person.Person(1, self.screen, self.SCREEN)
        self.me.person_draw()

        self.track = Track.Obstacle(self.screen, self.SCREEN)

    # def scenes_generator(self):
    #     self.track.rect_object()

    def update(self):
        Track.generate_track(self.screen, self.SCREEN)
        self.me.person_draw()
        self.track.normal_obstacle()
        pygame.display.flip()

