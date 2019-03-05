import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None
        self.reachable_for_time = {} # Dictionary to store all reachable vertices for a given time

    def set_distance(self, dist):
        self.distance = dist

    def set_adjacent(self, adj, weight=0):
        self.adjacent[adj] = int(weight)

    def set_reachable_for_time(self, rtm, weight=0):
        self.reachable_for_time[rtm] = int(weight)

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

    def get_reachable_for_time(self):
        return self.reachable_for_time
