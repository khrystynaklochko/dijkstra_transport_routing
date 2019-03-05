import click
import heapq

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
    click.echo('Build route graph from file: ' + input_file.name)
    g = build_graph(input_file)
    if g.get_error() == "": # If text file is valid and Graph can be readable
       path_output, reachable_destinations = graph_tools_runner(g, input_file)
       click.echo('The shortest path:')
       click.echo(path_output)
       output_file.write(path_output + '\n')

       click.echo('The reachable destinations:')
       click.echo(reachable_destinations)
       output_file.write(reachable_destinations)
    else:
       click.echo(g.get_error())
       output_file.write(g.get_error())

if __name__ == '__main__':
    main()
