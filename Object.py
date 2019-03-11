import numpy as np
import math

class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]


class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


class Object:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))

    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))

    def outputNodes(self):
        print("\n --- Nodes --- ")
        for i, node in enumerate(self.nodes):
            print(" %d: (%.2f, %.2f, %.2f)" % (i, node.x, node.y, node.z))

    def outputEdges(self):
        print("\n --- Edges --- ")
        for i, edge in enumerate(self.edges):
            print(" %d: (%.2f, %.2f, %.2f) -> (%.2f, %.2f, %.2f)" % (i, edge.start.x, edge.start.y, edge.start.z, edge.stop.x, edge.stop.y, edge.stop.z))

    def scale(self, n, ref=(0, 0)):
        for node in self.nodes:
            node.x = (node.x-1)*n+ref[0]
            node.y = (node.y-1)*n+ref[1]
            node.z *= n

    def move(self, direction, distance, object):
        if direction == 'left':
            for node in object.nodes:
                node.x -= distance
            for edge in object.edges:
                edge.start.x -= distance
                edge.stop.x -= distance
        elif direction == 'right':
            for node in object.nodes:
                node.x += distance
            for edge in object.edges:
                edge.start.x += distance
                edge.stop.x += distance
        elif direction == 'up':
            for node in object.nodes:
                node.y -= distance
            for edge in object.edges:
                edge.start.y -= distance
                edge.stop.y -= distance
        elif direction == 'down':
            for node in object.nodes:
                node.y += distance
            for edge in object.edges:
                edge.start.y += distance
                edge.stop.y += distance

    def rotation(self, rec_coords, angle, orig_coords):
        a, b = rec_coords
        c0, c1 = orig_coords
        rho = math.hypot(a-c0, b-c1)
        phi = math.atan2(b-c1, a-c0) + angle
        a = rho * math.cos(phi) + c0
        b = rho * math.sin(phi) + c1
        return a, b

    def get_center(self):
        return sum(node.x for node in self.nodes)/len(self.nodes), \
               sum(node.y for node in self.nodes)/len(self.nodes), \
               sum(node.z for node in self.nodes)/len(self.nodes)

    def rotate(self, axis, angle=1):
        center = Node(self.get_center())

        all = ['x', 'y', 'z']
        all.remove(axis)
        ele1, ele2 = tuple(all)
        print(ele1, ele2)

        for node in self.nodes:
            a, b = self.rotation((getattr(node, ele1), getattr(node, ele2)), angle,
                                (getattr(center, ele1), getattr(center, ele2)))
            setattr(node, ele1, a)
            setattr(node, ele2, b)


if __name__ == "__main__":
    cube_nodes = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    cube = Object()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n, n + 4) for n in range(0, 4)])
    cube.addEdges([(n, n + 1) for n in range(0, 8, 2)])
    cube.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])
    cube.outputNodes()
    cube.outputEdges()
    cube.rotate_z()
    cube.outputNodes()
    cube.outputEdges()