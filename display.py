import Object
import pygame
import math

key2function = {pygame.K_UP: lambda x:x.move('up', 1), pygame.K_DOWN:lambda x:x.move('down', -1),
                pygame.K_LEFT: lambda x:x.move('left', 1), pygame.K_RIGHT: lambda x:x.move('right', -1),
                pygame.K_w: lambda x:x.rotate('x'), pygame.K_s: lambda x:x.rotate('x', angle=-1),
                pygame.K_a: lambda x:x.rotate('y'), pygame.K_d: lambda x:x.rotate('y', angle=-1),
                pygame.K_q: lambda x:x.rotate('z'), pygame.K_e: lambda x:x.rotate('z', angle=-1),
                pygame.K_g: lambda x:x.scale(1.1), pygame.K_k: lambda x:x.scale(1/1.1)}

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
        self.perspective = True
        self.nodeColour = (255, 255, 255)
        self.edgeColour = (200, 200, 200)
        self.nodeRadius = 4
        self.fov = math.sqrt(2)
        self.d = (self.width/2) / math.tan(self.fov/2)

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
                    for dings in self.objects.values():
                        key2function[event.key](dings)
            self.display()
            pygame.display.flip()

    def display(self):
        """ Draw the objects on the screen. """

        self.screen.fill(self.background)
        for dings in self.objects.values():
            for node in dings.nodes:
                pygame.draw.circle(self.screen, self.nodeColour, (
                    round(node.x * self.d/node.z), round(node.y * self.d/node.z)), self.nodeRadius)
            for edge in dings.edges:
                pygame.draw.line(self.screen, self.edgeColour,
                                 (round(edge.start.x * self.d/edge.start.z), round(edge.start.y * self.d/edge.start.z)),
                                 (edge.stop.x * self.d/edge.stop.z, edge.stop.y * self.d/edge.stop.z))

if __name__ == '__main__':
    pv = ProjectionViewer(2000, 2000)

    cube = Object.Object()
    cube.addNodes([(x, y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])
    cube.addEdges(
        [(n, n + 4) for n in range(0, 4)] + [(n, n + 1) for n in range(0, 8, 2)] + [(n, n + 2) for n in (0, 1, 4, 5)])

    pv.addobject('cube', cube)
    pv.addobject('cube2', cube)
    pv.objects['cube'].scale(1)
    pv.objects['cube'].move('down', 20)
    pv.run()