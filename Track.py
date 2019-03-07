import pygame


def draw_track(surface, screen):
    pygame.draw.rect(surface, (0, 55, 255), pygame.Rect(0, 0, screen[0]/3, screen[1]))
    pygame.draw.rect(surface, (255, 0, 55), pygame.Rect(screen[0]/3, 0, screen[0]/3, screen[1]))
    pygame.draw.rect(surface, (55, 255, 0), pygame.Rect(screen[0]/3*2, 0, screen[0]/3, screen[1]))
