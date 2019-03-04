import click
import heapq
from build_graph import build_graph

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
    start = g.get_start()
    finish = g.get_finish()

    click.echo('Find shortest path from: '+ start +' to: ' + finish)

if __name__ == '__main__':
    main()
