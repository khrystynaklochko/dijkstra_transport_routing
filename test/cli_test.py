import click
import os
import heapq
from click.testing import CliRunner
from graph_tools.build_graph import build_graph
from graph_tools.graph_tools_runner import graph_tools_runner

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

       path_output, reachable_destinations = graph_tools_runner(g, input_file)

       click.echo(path_output)
       output_file.write(str(path_output) + '\n')

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
    shared_examples('files/init_graph.txt', 'files/init_output.txt') # Test case from a task

def test_small_graph():
    shared_examples('files/small_graph.txt', 'files/small_output.txt') # Modified test case from a task

def test_errored_graph(): # Test errored Graph structure
    runner = CliRunner()
    output_file = os.path.join(os.path.dirname(__file__), 'files/errored_output.txt')
    result = runner.invoke(main, ['--input_file',
                                  os.path.join(os.path.dirname(__file__), 'files/errored_graph.txt'),
                                  '--output_file',
                                  output_file])
    file = open(output_file)
    route_output = file.readline()
    nearby_vertexes = file.readline()
    file.close()
    assert result.exit_code == 0
    assert route_output in result.output
