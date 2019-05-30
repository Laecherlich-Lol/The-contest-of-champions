import pygame


class Track:
    '''
    A rectangle instance of pygame surface to ......
    '''
    def __init__(self, pos, size, color=(255, 255, 255)):
        '''
        Initialization
        :param pos: tuple of two ints; position of the left up corner of the track
        :param size: tuple of two ints; x and y of track
        :param color: tuple of three ints; rgb format.
        '''
        self.pos = pos
        self.size = size
        self.color = color
        self.track = pygame.Surface(self.size)
        self.track.fill(self.color)

    def update_track(self):
        '''

        :return:
        '''
        self.track = pygame.Surface(self.size)
        self.track.fill(self.color)

    def get_track(self):
        return self.track

    def get_pos(self):
        return self.pos

    def get_size(self):
        return self.size

    def set_color(self, color):
        self.color = color

    def set_pos(self, pos):
        self.pos = pos

    def set_size(self, size):
        self.size = size