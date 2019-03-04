import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None

    def set_distance(self, dist):
        self.distance = dist

    def set_adjacent(self, adj, weight=0):
        self.adjacent[adj] = weight

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def get_id(self):
        return self.id

    def get_distance(self):
        return self.distance

    def get_weight(self, adj):
        return self.adjacent[adj]

    def get_connections(self):
        return self.adjacent.keys()
