from dijkstra import dijkstra
from dijkstra import shortest_path

def graph_tools_runner(g, input_file):
    start = g.get_start()
    finish = g.get_finish()
    target = g.get_vertex(finish) # Destination point
    path = [target.get_id()]

    dijkstra(g, g.get_vertex(start), g.get_nearby())

    shortest_path(target, path) # Find a shortest path to finish
    path_output = ' -> '.join(path[::-1]) + ': ' + str(target.get_distance())
    # Build reachable destiations string from Dictionary
    reachable_destinations = ', '.join("%s: %r" % (key,val) for (key,val) in g.get_vertex(start).get_reachable_for_time().iteritems())
    return path_output, reachable_destinations
