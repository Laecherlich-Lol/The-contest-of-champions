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

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for dings in self.objects.values():
                            # dings.move('up', 20, dings)
                            dings.rotate('x')
                    if event.key == pygame.K_DOWN:
                        for dings in self.objects.values():
                            # dings.move('up', 20, dings)
                            dings.rotate('y')
                    if event.key == pygame.K_LEFT:
                        for dings in self.objects.values():
                            # dings.move('up', 20, dings)
                            dings.rotate('z')
            self.display()
            pygame.display.flip()

    def display(self):
        """ Draw the objects on the screen. """

        self.screen.fill(self.background)
        for dings in self.objects.values():
            for node in dings.nodes:
                pygame.draw.circle(self.screen, self.nodeColour, (
                    round(node.x), round(node.y)), self.nodeRadius)
            for edge in dings.edges:
                pygame.draw.line(self.screen, self.edgeColour,
                                 (round(edge.start.x), round(edge.start.y)), (edge.stop.x, edge.stop.y))

if __name__ == '__main__':
    pv = ProjectionViewer(1000, 1000)

    cube = Object.Object()
    cube.addNodes([(x, y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])
    cube.addEdges(
        [(n, n + 4) for n in range(0, 4)] + [(n, n + 1) for n in range(0, 8, 2)] + [(n, n + 2) for n in (0, 1, 4, 5)])

    pv.addobject('cube', cube)
    pv.addobject('cube2', cube)
    pv.objects['cube'].scale(1)
    pv.objects['cube'].move('down', 20, pv.objects['cube'])
    pv.run()