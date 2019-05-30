import pygame


class Person:
    def __init__(self, size=(40, 40), relative_pos=(0.5, 0.3), track_num=1, color=(0, 0, 0), status='run', height=0):
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
        # elif instruction == 'up':
        #     self.delta = default
        #     self.dev = 40 - self.delta

    def set_height(self, height):
        self.height = height

    def get_view_size(self, i=None):
        return self.size[0]+self.height, self.size[1]+self.height if i is None else self.size[i]+self.height

    def set_status(self, status):
        self.status = status

    def get_re_pos(self):
        return self.relative_pos

    def get_track_num(self):
        return self.track_num