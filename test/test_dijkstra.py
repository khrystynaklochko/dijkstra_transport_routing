import pytest
import re
import heapq
from graph_tools.models.graph import Graph
from graph_tools.build_graph import build_graph
from graph_tools.dijkstra import dijkstra
from graph_tools.dijkstra import shortest_path


def test_dijkstra_easy():
    g = Graph()
    g.set_vertex('A')
    g.set_vertex('B')
    g.set_vertex('C')
    g.set_vertex('D')
    g.set_vertex('E')

    # A -> B -> C with cost 3
    g.set_edge('A', 'B', 1)
    g.set_edge('B', 'C', 1)
    g.set_edge('C', 'D', 1)

    # A -> E with cost 2
    g.set_edge('A', 'E', 1)
    g.set_edge('E', 'D', 1)

    g.set_nearby('E', 1)

    dijkstra(g, g.get_vertex('E'), g.get_nearby())
    target = g.get_vertex('D') # Destination point
    path = [target.get_id()]
    shortest_path(target, path)
    path_output = ' -> '.join(path[::-1]) + ': ' + str(target.get_distance())
    reachable_destinations = ', '.join("%s: %r" % (key,val) for (key,val) in g.get_vertex('E').get_reachable_for_time().iteritems())

    assert 'E -> D: 1' == path_output
    assert ['D', 'E'] == path
    assert 'A: 1, D: 1' == reachable_destinations

def test_dijkstra_dead_ends():
    g = Graph()
    g.set_vertex('A')
    g.set_vertex('B')
    g.set_vertex('C')
    g.set_vertex('D')
    g.set_vertex('E')
    g.set_vertex('G')
    g.set_vertex('H')

    # A -> B -> C -> D  with cost 3
    g.set_edge('A', 'B', 1)
    g.set_edge('B', 'C', 1)
    g.set_edge('C', 'D', 1)

    # A -> E -> D  with cost 2
    g.set_edge('A', 'E', 1)
    g.set_edge('E', 'D', 1)

    # Dead-ends
    g.set_edge('D', 'G', 1)
    g.set_edge('D', 'C', 1)
    g.set_edge('A', 'H', 0)

    g.set_nearby('A', 2)

    dijkstra(g, g.get_vertex('A'), g.get_nearby())
    target = g.get_vertex('D') # Destination point
    path = [target.get_id()]
    shortest_path(target, path)
    path_output = ' -> '.join(path[::-1]) + ': ' + str(target.get_distance())
    reachable_destinations = ', '.join("%s: %r" % (key,val) for (key,val) in g.get_vertex('A').get_reachable_for_time().iteritems())

    assert 'A -> E -> D: 2' == path_output
    assert ['D', 'E', 'A'] == path
    assert 'C: 2, B: 1, E: 1, D: 2' == reachable_destinations
