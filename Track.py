import pygame


def draw_track(surface, screen):
    pygame.draw.rect(surface, 0x028C6A, pygame.Rect(0, 0, screen[0]/3, screen[1]))
    pygame.draw.rect(surface, 0x0E03101, pygame.Rect(screen[0]/3, 0, screen[0]/3, screen[1]))
    pygame.draw.rect(surface, 0x1D6A96, pygame.Rect(screen[0]/3*2, 0, screen[0]/3, screen[1]))
