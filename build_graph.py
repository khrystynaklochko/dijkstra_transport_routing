from graph import Graph
import re

# Utility to read Graph data from file and construct Graph and Vertex objects
def build_graph(file_path):
    vertices_number = int(file_path.readline()) # Reading first line with a number of weights
    vertices = []
    g = Graph()
    while vertices_number > 0:
          line = file_path.readline()
          distance = re.split('->|, |:|',line.strip('\n').replace(" ", ""))
          # Adding vertices
          if distance[0] not in vertices:
            vertices.append(distance[0])
            g.set_vertex(distance[0])
          if distance[1] not in vertices:
            vertices.append(distance[1])
            g.set_vertex(distance[1])

          g.set_edge(distance[0] ,distance[1], distance[2])
          vertices_number -=1
    # Reading start and destination point
    line = file_path.readline()
    route = re.split('->',line.strip('\n').replace('route', ' ').replace(" ", ""))

    if route[0] and route[1] in vertices:
       g.set_start(route[0])
       g.set_finish(route[1])
       line = file_path.readline()
       nearby = re.split(',',line.strip('\n').replace('nearby', ' ').replace(" ", "")) # Reading time to reach closest destiation points for start vertex
       g.set_nearby(nearby[0], nearby[1])
    else:
       g.set_error("Not possible to find a route")

    return g
