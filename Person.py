import pygame


class Person:
    def __init__(self, size=(100, 100), relative_pos=(0.5, 0.8), track_num=1, color=(0, 0, 0), status='run', height=0):
        '''

        :param size:
        :param relative_pos: tuple; first is x, second is y; normalized
        :param track_num:
        :param color:
        :param status:
        :param height:
        '''
        self.size = size
        self.relative_pos = relative_pos
        self.track_num = track_num
        self.color = color
        self.status = status
        self.height = height

    def change_track(self, direction, total=3):
        if direction == 'left':
            self.track_num -= 1 if self.track_num > 0 else 0
        elif direction == 'right':
            self.track_num += 1 if self.track_num < total-1 else 0

    def set_height(self, height):
        self.height = height

    def get_view_size(self, i=None):
        if i is None:
            return self.size[0]+self.height, self.size[1]+self.height
        else:
            return self.size[i]+self.height

    def set_status(self, status):
        self.status = status

    def get_re_pos(self):
        return self.relative_pos

    def get_track_num(self):
        return self.track_num