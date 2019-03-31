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
    def __init__(self, surface, screen, size='big', top=True, using=True):
        self.col = surface
        self.screensize = screen
        self.rect_object = {'small': (screen[0]/3-10, 120),
                            'big': (screen[0]/3-10, 280),
                            'normal': (screen[0]/3-20, 20)}
        self.position = 0
        self.size = size
        self.top = top
        self.u = using

    def rect_obstacle(self, color, position=0):
        self.position += position
        # print(self.position, position)
        return pygame.draw.rect(self.col, color,
                                pygame.Rect((5, -self.rect_object[self.size][1]-1+self.position),
                                            self.rect_object[self.size])) if self.top \
            else pygame.draw.rect(self.col, color,
                                  pygame.Rect((5, self.screensize[1]-self.rect_object[self.size][1]+self.position),
                                              self.rect_object[self.size]))

    def normal_obstacle(self, position=0):
        self.position += position
        return pygame.draw.rect(self.col, (255, 255, 255),
                                pygame.Rect((10, -self.rect_object['normal'][1]-1+self.position),
                                            self.rect_object['normal']))


class Running:
    def __init__(self, surface, screen, person):
        self.surface = surface
        self.screensize = screen
        self.person = person
        self.begin_obstacles = [Obstacle(self.surface[i], self.screensize, top=False) for i in range(0, 3, 2)]
        self.col1 = [Obstacle(self.surface[0], self.screensize) for i in range(3)]
        self.col2 = [Obstacle(self.surface[1], self.screensize) for i in range(3)]
        self.col3 = [Obstacle(self.surface[2], self.screensize) for i in range(3)]


    def begin(self):
        for ob in self.begin_obstacles:
            if ob.u:
                ob.rect_obstacle((255, 0, 0), position=2)
            if ob.position > 280:
                ob.u = False
        # return self.begin_obstacles