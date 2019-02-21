import pygame
import utils

NUM_COLOR = {2: (0, 0, 255),
             4: (0, 0, 128),
             8: (0, 0, 64),
             16: (0, 0, 0)}
BLOCK_FONT_SIZE = 30
BLOCK_FONT_COLOR = (255, 255, 255)


class Block:
    def __init__(self, value, row, col):
        self.value = value
        self.x = row
        self.y = col

    def draw(self, surface, unit):
        pygame.draw.rect(surface,
                         NUM_COLOR[self.value], (self.y*unit, self.x * unit, unit, unit))
        font = pygame.font.SysFont("monospace", BLOCK_FONT_SIZE)
        render = font.render(str(self.value), 1, BLOCK_FONT_COLOR )

        surface.blit(render, (self.y*unit+unit/3, self.x*unit+unit/3))


class Board:
    def __init__(self, surface, nrow, ncol):
        self.surface = surface
        self.unit = surface.get_rect()[2]/nrow  #TODO: extend to rectangle
        self.X = nrow
        self.Y = ncol
        self.blocks = []

    def add_blocks(self, blocks):
        for block in blocks:
            self.blocks.append(block)

    def move_blocks(self, direction):

            for i in range(self.Y):  #TODO: extend to rectangle
                group = []

                group_attr = 'y' if direction == 'up' or direction == 'down' else 'x'
                sort_attr = 'x' if direction == 'up' or direction == 'down' else 'y'

                for block in self.blocks:    # group a row or col
                    if getattr(block, group_attr) == i:
                        group.append(block)

                tf = direction == 'down' or direction == 'right'
                sorted_blocks = utils.sort_by(group, sort_attr, tf)
                for index, block in enumerate(sorted_blocks):
                    if direction == 'up' or direction == 'left':
                        setattr(block, sort_attr, index)
                    else:
                        setattr(block, sort_attr, self.X - index - 1) #TODO: extend to rectangle

    def draw_blocks(self):
        for block in self.blocks:
            block.draw(self.surface, self.unit)

    # def merge_blocks(self):
    #     new_blocks = []
    #     for i in range(self.Y):
    #         if


