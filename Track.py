import pygame


class Track:
    def __init__(self, surface):
        self.surface = surface

    def generate_track(self, screen):
        self.screen = screen
        self.track1 = pygame.Surface((screen[0]/3, screen[1]))
        self.track2 = pygame.Surface((screen[0]/3, screen[1]))
        self.track3 = pygame.Surface((screen[0]/3, screen[1]))

        self.track1.fill(0x028C6A)
        self.track2.fill(0x0E03101)
        self.track3.fill(0x1D6A96)
        return self.track1, self.track2, self.track3

    def blit_track(self):
        self.surface.blit(self.track1, (0, 0))
        self.surface.blit(self.track2, (self.screen[0] / 3, 0))
        self.surface.blit(self.track3, (self.screen[0] / 3 * 2, 0))

    def clear_track(self):
        self.track1.fill(0x028C6A)
        self.track2.fill(0x0E03101)
        self.track3.fill(0x1D6A96)


class Obstacle:
    def __init__(self, surface, screen):
        self.col = surface
        self.size = screen
        self.rect_object = {'small': (screen[0]/3-10, 120),
                            'medium': (screen[0]/3-10, 200),
                            'big': (screen[0]/3-10, 280),
                            'normal': (screen[0]/3-20, 20)}
        self.position = {}

    def rect_obstacle(self, size, color, num, top=True, position=0):
        print(self.position, num)
        self.position[num] += position
        return pygame.draw.rect(self.col, color,
                                pygame.Rect((5, -self.rect_object[size][1]-1+self.position[num]),
                                            self.rect_object[size])) if top \
            else pygame.draw.rect(self.col, color,
                                  pygame.Rect((5, self.size[1]-self.rect_object[size][1]+self.position[num]),
                                              self.rect_object[size]))

    def normal_obstacle(self, num, position=0):
        self.position[num] += position
        return pygame.draw.rect(self.col, (255, 255, 255),
                                pygame.Rect((10, -self.rect_object['normal'][1]-1+self.position[num]),
                                            self.rect_object['normal']))

class Running:
    def __init__(self, surface, screen):
        self.surface = surface
        self.obstacles_begin = []
        self.obstacles_rect = []
        self.obstacles_normal = []
        self.obstacle_st = Obstacle(self.surface[0], screen)
        self.obstacle_ed = Obstacle(self.surface[1], screen)
        self.obstacle_rd = Obstacle(self.surface[2], screen)

    def begin(self):
        self.obstacles_begin.append(self.obstacle_st)
        self.obstacle_st.position[0] = 0
        self.obstacles_begin.append(self.obstacle_rd)
        self.obstacle_rd.position[0] = 0
        self.obstacles_rect.append(self.obstacle_ed)
        self.obstacle_ed.position[0] = 0
        print(self.obstacles_rect[0].position)
        if self.obstacles_rect[0].position[0] >= 200:
            # print()
            self.obstacles_rect.append(self.obstacle_st)
            self.obstacle_st.position[1] = 0
            self.obstacles_rect.append(self.obstacle_rd)
            self.obstacle_rd.position[1] = 0
        for idx, ob in enumerate(self.obstacles_begin):
            print(idx)
            ob.rect_obstacle('big', (255, 0, 0), 0, top=False, position=0.1)
        for idx, ob in enumerate(self.obstacles_rect):
            ob.rect_obstacle('big', (255, 0, 0), idx, position=0.1)

        return self.obstacles_rect