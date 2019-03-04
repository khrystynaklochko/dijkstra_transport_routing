import click
import heapq
from build_graph import build_graph
from dijkstra import dijkstra
from dijkstra import shortest_path

@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    required=True,
)
@click.option(
    '--output_file',
    type=click.File('w'),
    required=True,
)


def main(input_file, output_file):
    click.echo('Build route graph from file: ' + input_file.name)
    g = build_graph(input_file)
    if g.get_error() == "":
       start = g.get_start()
       finish = g.get_finish()
       click.echo('Find shortest path from: '+ start +' to: ' + finish)
       dijkstra(g, g.get_vertex(start), g.get_nearby())

       click.echo('The shortest path :')
       target = g.get_vertex(finish)
       path = [target.get_id()]
       shortest_path(target, path)
       path_output = ' -> '.join(path[::-1]) + ': ' + str(target.get_distance())
       click.echo(path_output)
       output_file.write(path_output + '\n')

       click.echo('The reachable destinations :')
       reachable_destinations = ', '.join("%s: %r" % (key,val) for (key,val) in g.get_vertex(start).get_reachable_for_time().iteritems())
       click.echo(reachable_destinations)
       output_file.write(reachable_destinations)
    else:
       output_file.write(g.get_error())

if __name__ == '__main__':
    main()
