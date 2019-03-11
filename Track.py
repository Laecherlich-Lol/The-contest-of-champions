import pygame


def generate_track(surface, screen):
    pygame.Surface((0, screen[1]), surface)
    pygame.Surface((screen[0]/3, screen[1]), surface)
    pygame.Surface((screen[0]/3*2, screen[1]), surface)

# 0x028C6A 0x0E03101 0x1D6A96