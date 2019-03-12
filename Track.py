import pygame


def generate_track(surface, screen):
    track1 = pygame.Surface((screen[0]/3, screen[1]))
    track2 = pygame.Surface((screen[0]/3, screen[1]))
    track3 = pygame.Surface((screen[0]/3, screen[1]))

    # track1.fill(0x028C6A).blit(surface, (0, 0))
    # track2.fill(0x0E03101).blit(surface, (screen[0]/3, 0))
    # track3.fill(0x1D6A96).blit(surface, (screen[0]/3*2, 0))
    return track1, track2, track3