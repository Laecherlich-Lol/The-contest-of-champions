import pygame
import Person
import Track


class Game:
    def __init__(self, screen=(540, 840)):
        self.SCREEN = screen
        pygame.init()
        self.logo = pygame.image.load('images.jpg')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('run')

        self.screen = pygame.display.set_mode(self.SCREEN)
        self.tracks = Track.Track(self.screen)
        self.tracks.generate_track(self.SCREEN)
        pygame.display.flip()

        self.me = Person.Person(1, self.screen, self.SCREEN)
        self.me.person_draw()

        self.track = Track.Obstacle(self.screen, self.SCREEN)

        self.run = Track.Running(self.tracks.generate_track(self.SCREEN), self.SCREEN, self.me)

        self.default = 0

    def update(self):
        self.tracks.clear_track()
        self.run.begin()
        self.tracks.blit_track()
        self.me.person_draw()
        pygame.display.flip()

    def move(self, ins):
        if ins == pygame.K_LEFT:
            # if self.me.track_num == 1:
            #     for i in self.run.col0:
            #         if self.me.person_pos+i.position > i.position > self.me.person_pos:
            #             return
            # elif self.me.track_num == 2:
            #     for i in self.run.col1:
            #         if self.me.person_pos+i.position > i.position > self.me.person_pos:
            #             return
            self.me.move_person('left')
        if ins == pygame.K_RIGHT:
            if self.me.track_num == 0:
                for i in self.run.col1:
                    if self.me.person_pos + i.position > i.position > self.me.person_pos:
                        return
            # elif self.me.track_num == 1:
            #     for i in self.run.col2:
            #         if self.me.person_pos + i.position > i.position > self.me.person_pos:
            #             return
            self.me.move_person('right')
            print('a')
        if ins == pygame.K_UP:
            self.me.move_person('up', default=self.default)

    def check_ob(self, num):
        col = 'col' + str(num)
        for i in getattr(self.run, col):
            if i.u:
                if i.position == 640:
                    if i.color == 'white':
                        return True if self.me.status == 'fly' else False
                    elif i.color == 'red':
                        for j in getattr(self.run, col):
                            if j.u:
                                if j.rect_object['big'][1]+self.me.person_pos+20 > j.position > self.me.person_pos \
                                        and j.size == 'big':
                                    return True
                        return False
        # if self.me.track_num == 0:
        #     for i in self.run.col0:
        #         if i.u:
        #             if i.position == 640:
        #                 print(self.me.status)
        #                 if i.color == (255, 255, 255):
        #                     return True if self.me.status == 'fly' else False
        #
        #                 elif i.color == (255, 0, 0):
        #                     for j in self.run.col0:
        #                         if j.u:
        #                             if j.rect_object['big'][1]+self.me.person_pos+20 > j.position > self.me.person_pos \
        #                                     and j.size == 'big':
        #                                     return True
        #                     return False
        # elif self.me.track_num == 1:
        #     for i in self.run.col1:
        #         if i.u:
        #             if i.position == 640:
        #                 if i.color == (255, 255, 255) and self.me.status == 'fly':
        #                     continue
        #                 elif i.color == (255, 0, 0):
        #                     for j in self.run.col1:
        #                         if j.u:
        #                             if j.rect_object['big'][1]+self.me.person_pos+20 > j.position > self.me.person_pos \
        #                                     and j.size == 'big':
        #                                 return True
        #                     return False
        # elif self.me.track_num == 2:
        #     # print('a')
        #     for i in self.run.col2:
        #         if i.u:
        #             if i.position == 640:
        #                 if i.color == (255, 255, 255) and self.me.status == 'fly':
        #                     continue
        #                 elif i.color == (255, 0, 0):
        #                     for j in self.run.col2:
        #                         if j.u:
        #                             if j.rect_object['big'][1]+self.me.person_pos+20 > j.position > self.me.person_pos \
        #                                     and j.size == 'big':
        #                                 return True
        #                     return False
        return True
