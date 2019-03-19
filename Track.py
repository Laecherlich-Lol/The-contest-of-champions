import pygame


def generate_track(surface, screen):
    track1 = pygame.Surface((screen[0]/3, screen[1]))
    track2 = pygame.Surface((screen[0]/3, screen[1]))
    track3 = pygame.Surface((screen[0]/3, screen[1]))

    track1.fill(0x028C6A)
    track2.fill(0x0E03101)
    track3.fill(0x1D6A96)
    surface.blit(track1, (0, 0))
    surface.blit(track2, (screen[0]/3, 0))
    surface.blit(track3, (screen[0]/3*2, 0))
    return track1, track2, track3

class Obstacle:
    def __init__(self, surface, screen):
        self.col = surface
        self.rect_object = {'small': (screen[0]/3-10, 120),
                            'medium': (screen[0]/3-10, 200),
                            'big': (screen[0]/3-10, 280),
                            'normal': (screen[0]/3-20, 20)}
        self.position = 0

    def rect_obstacle(self, size, color, position=0):
        self.position += position
        return pygame.draw.rect(self.col, color,
                                pygame.Rect((5, -self.rect_object[size][1]-1+self.position), self.rect_object[size]))

    def normal_obstacle(self, position=0):
        self.position += position
        return pygame.draw.rect(self.col, (255, 255, 255),
                                pygame.Rect((10, -self.rect_object['normal'][1]-1+self.position),
                                            self.rect_object['normal']))

# class Running:
#     def __init__(self):
