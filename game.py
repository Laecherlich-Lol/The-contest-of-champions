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
        self.tracks = Track.Track(self.screen)
        self.tracks.generate_track(self.SCREEN)
        pygame.display.flip()

        self.me = person.Person(1, self.screen, self.SCREEN)
        self.me.person_draw()

        self.track = Track.Obstacle(self.screen, self.SCREEN)

        self.run = Track.Running(self.tracks.generate_track(self.SCREEN), self.SCREEN, self.me)

    # def scenes_generator(self):
    #     self.track.rect_object()

    # def person_update(self):
    #     self.me.person_draw()
    #     return False

    def update(self):
        self.tracks.clear_track()
        self.run.begin()
        self.tracks.blit_track()
        self.me.person_draw()
        pygame.display.flip()

    def move(self, ins):
        if ins == pygame.K_LEFT:
            self.me.move_person('left')
        if ins == pygame.K_RIGHT:
            self.me.move_person('right')

    # def stop(self):
    #     return self.move.cancel()