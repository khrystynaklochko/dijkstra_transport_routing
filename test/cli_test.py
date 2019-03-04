import click
import os
import heapq
from click.testing import CliRunner
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
    g = build_graph(input_file)
    if g.get_error() == "": # If text file is valid and Graph can be readable
       start = g.get_start()
       finish = g.get_finish()
       dijkstra(g, g.get_vertex(start), g.get_nearby())

       target = g.get_vertex(finish) # Destination point
       path = [target.get_id()]
       shortest_path(target, path) # Find a shortest path to finish
       path_output = ' -> '.join(path[::-1]) + ': ' + str(target.get_distance())
       click.echo(path_output)
       output_file.write(str(path_output) + '\n')

       # Build reachable destiations string from Dictionary
       reachable_destinations = ', '.join("%s: %r" % (key,val) for (key,val) in g.get_vertex(start).get_reachable_for_time().iteritems())
       click.echo(reachable_destinations)
       output_file.write(str(reachable_destinations))
    else:
       click.echo(g.get_error())
       output_file.write(g.get_error())

def shared_examples(input, output):
    runner = CliRunner()
    output_file = os.path.join(os.path.dirname(__file__), output)
    result = runner.invoke(main, ['--input_file',
                                  os.path.join(os.path.dirname(__file__), input),
                                  '--output_file',
                                  output_file])
    file = open(output_file)
    route_output = file.readline()
    nearby_vertexes = file.readline()
    file.close()
    assert result.exit_code == 0
    assert route_output in result.output
    assert nearby_vertexes in result.output

def test_init_graph():
    shared_examples('init_graph.txt', 'init_output.txt') # Test case from a task

def test_small_graph():
    shared_examples('small_graph.txt', 'small_output.txt') # Modified test case from a task

def test_errored_graph(): # Test errored Graph structure
    runner = CliRunner()
    output_file = os.path.join(os.path.dirname(__file__), 'errored_output.txt')
    result = runner.invoke(main, ['--input_file',
                                  os.path.join(os.path.dirname(__file__), 'errored_graph.txt'),
                                  '--output_file',
                                  output_file])
    file = open(output_file)
    route_output = file.readline()
    nearby_vertexes = file.readline()
    file.close()
    assert result.exit_code == 0
    assert route_output in result.output
