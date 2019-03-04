from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertices_number = 0
        self.start = ''
        self.finish = ''
        self.nearby = {}
        self.error = ""

    def __iter__(self):
        return iter(self.vertices.values())

    def set_vertex(self, node):
        self.vertices_number = self.vertices_number + 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def set_edge(self, start, finish, cost = 0):
        if start not in self.vertices:
            self.add_vertex(start)
        if finish not in self.vertices:
            self.add_vertex(finish)

        self.vertices[start].set_adjacent(self.vertices[finish], cost)
        self.vertices[finish].set_adjacent(self.vertices[start], cost)

    def set_previous(self, curr):
        self.previous = curr

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()

    def get_previous(self):
        return self.previous

    def set_start(self, start):
        self.start = start

    def set_finish(self, finish):
        self.finish = finish

    def get_start(self):
        return self.start

    def get_finish(self):
        return self.finish

    def set_nearby(self, vertex, distance):
        self.nearby = { self.get_vertex(vertex): distance }

    def get_nearby(self):
        return self.nearby

    def set_error(self, error_message):
        self.error = error_message

    def get_error(self):
        return self.error
