import pygame

def sort_by(seq, attr_name, reverse=False):
    '''
    Sort a list/dictionary of objects via one of its attribute name
    :param seq: a list of objects
    :param attr_name:
    :param reverse: increasing if false, decreasing if true
    :return: a sorted sequence
    '''
    return sorted(seq, key=lambda element: getattr(element, attr_name), reverse=reverse)


def draw_info(surface, text, number, position, color=(255, 255, 255)):
    '''
    Draw a block with a text title and a number
    :param surface: surface to draw on, pygame.Surface
    :param text: a string
    :param number: a number
    :param position: a four number tuple
    :param color: a three elements tuple (R, G, B)
    :return: None
    '''

    # surface -> pygame.Surface
    pygame.draw.rect(surface, color, position)
    font = pygame.font.SysFont("monospace", 20)
    text_render = font.render(text, 1, (255-color[0], 255-color[1], 255-color[2]))
    num_render = font.render(str(number), 1, (255-color[0], 255-color[1], 255-color[2]))
    surface.blit(text_render, position)
    num_position = (position[0], position[1]+position[3]/2)
    surface.blit(num_render, num_position)
