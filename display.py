import Object
import pygame


class ProjectionViewer:
    """ Displays 3D objects on a Pygame screen """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('object Display')
        self.background = (10, 10, 50)

        self.objects = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255, 255, 255)
        self.edgeColour = (200, 200, 200)
        self.nodeRadius = 4

    def addobject(self, name, object):
        """ Add a named object object. """

        self.objects[name] = object

    def run(self):
        """ Create a pygame screen until it is closed. """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display()
            pygame.display.flip()

    def display(self):
        """ Draw the objects on the screen. """

        self.screen.fill(self.background)


if __name__ == '__main__':
    pv = ProjectionViewer(400, 300)

    cube = Object.Object()
    cube.addNodes([(x, y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])
    cube.addEdges(
        [(n, n + 4) for n in range(0, 4)] + [(n, n + 1) for n in range(0, 8, 2)] + [(n, n + 2) for n in (0, 1, 4, 5)])

    pv.addobject('cube', cube)
pv.run()