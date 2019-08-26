import pygame


class Obstacle:
    def __init__(self, size, type, color):
        self.size = size
        self.type = type
        self.color = color
        self.position = 0
        self.types = {'red': 'dead',
                      'white': 'dangerous'}

    def get_type(self):
        return self.types[self.type]

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def set_type(self, type):
        self.type = type

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def clear_position(self):
        self.position = 0

    def move(self, steps=1):
        self.position += steps

