import pygame
import utils
import random
import numpy as np
import game

# NUM_COLOR = {2: (0, 0, 255),
#              4: (0, 0, 128),
#              8: (0, 0, 64),
#              16: (0, 0, 0)}
NUM_COLOR = {}
for i in range(20):
    NUM_COLOR[2**(i+1)] = (0, 0, 255 - 255/(20) * (i+1))


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

        self.coord_pool = []
        for i in range(self.X):
            for j in range(self.Y):
                self.coord_pool.append((i, j))

    def add_blocks(self, blocks):
        for block in blocks:
            self.blocks.append(block)

    def move_blocks(self, direction):
        self.direction = direction
        for i in range(self.Y):  #TODO: extend to rectangle
            group = []

            group_attr = 'y' if direction == 'up' or direction == 'down' else 'x'
            sort_attr = 'x' if direction == 'up' or direction == 'down' else 'y'

            for block in self.blocks:    # group a row or col
                if getattr(block, group_attr) == i:
                    group.append(block)

            tf = direction == 'down' or direction == 'right'
            sorted_blocks = utils.sort_by(group, sort_attr, tf)

            for i in range(len(sorted_blocks) - 1):
                if i + 1 >= len(sorted_blocks):
                    break

                if sorted_blocks[i].value == sorted_blocks[i+1].value:
                    sorted_blocks[i].value += sorted_blocks[i+1].value
                    self.blocks.remove(sorted_blocks[i+1])
                    del sorted_blocks[i+1]

            for index, block in enumerate(sorted_blocks):
                if direction == 'up' or direction == 'left':
                    setattr(block, sort_attr, index)
                else:
                    setattr(block, sort_attr, self.X - index - 1) #TODO: extend to rectangle

        return self.duang()

    def draw_blocks(self):
        for block in self.blocks:
            block.draw(self.surface, self.unit)

    def duang(self):
        print('duang')
        # use number to represant location (X: the digit at 10^1, Y: at 10^0)
        temp_list = self.coord_pool.copy()
        # print("Duang")
        for block in self.blocks:
            temp = (block.x, block.y)
            # print(temp)

            temp_list.remove(temp)
            # print(self.coord_pool)
        try:
            the_chosen_one = random.choice(temp_list)
            self.add_blocks([Block(random.choice([4096]), the_chosen_one[0], the_chosen_one[1])])
            if len(self.blocks) == self.X * self.Y:
                if self.check_stuck():
                    print('a')
                    # self.lost(self.surface)
                    return False
            print(len(self.blocks))
        except IndexError:
            # pass
            if self.check_stuck():
                print('a')
                # self.lost(self.surface)
                return False
            else: return True
        return True

    def get_score(self):
        max = np.max([block.value for block in self.blocks])
        # if max >= 128:
        #     print("! You win")
        return max

    def check_stuck(self):
        group_attr = 'x' if self.direction == 'up' or self.direction == 'down' else 'y'
        sort_attr = 'y' if self.direction == 'up' or self.direction == 'down' else 'x'

        for i in range(self.X):
            group = []

            for block in self.blocks:    # group a row or col
                if getattr(block, group_attr) == i:
                    group.append(block)
            sorted_blocks = utils.sort_by(group, sort_attr)

            for i in range(len(sorted_blocks) - 1):
                if sorted_blocks[i].value == sorted_blocks[i + 1].value:
                    print("Here")
                    return False
        return True

    def lost(self, surface):
        print("in lost")
        pygame.display.flip()


