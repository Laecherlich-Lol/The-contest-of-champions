import pygame


class Obstacle:
    def __init__(self, size, type, color, use_times=0):
        self.size = size
        self.type = type
        self.color = color
        self.use_times = use_times
        self.position = 0
        self.types = {'red': 'dead',
                      'green': 'safe',
                      'white': 'dangerous'}

    def get_type(self):
        return self.types[self.type]

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_use_times(self):
        return self.use_times

    def set_type(self, type):
        self.type = type

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def clear_position(self):
        self.position = 0

    def used(self):
        self.use_times += 1

    def move(self):
        self.position += 1
