# Public Transport Routing

Routing solution for Berlin’s public transport system that lets people search for the quickest route between two given stations. In addition there is a possibility to find stations nearby a given station that can be reached within a given time.

This is CLI tool which reads network map from a txt file and provides an output for shortest path and nearby stations to an output file.

This CLI tool based on Dijkstra algorithm which is an algorithm for finding the shortest paths between nodes in a graph in a weighted graph.

For more info see Wikipedia.

## Development setup

OS X & Linux:

```python
pip install -r requirements.txt
```

CLI help:
```python
python cli.py --help
```

You should always specify ```--input_file``` and ``` --output_file``` files as they are required.

## Usage example

CLI is shipped with sample a test_route.txt file:

```python
python cli.py --input_file test_route.txt --output_file output.txt
```

```
Build route graph from file: test_route.txt
Find shortest path from: A to: B
The shortest path :
A -> C -> B: 130
The reachable destinations :
C: 70, B: 130, D: 120
```

And in output file you will see:

```
A -> C -> B: 130
C: 70, B: 130, D: 120
```

## Project structure
Project tree:
```python
  graph:
    - graph_tools:
      - models
        graph
        vertex
      build_graph
      dijkstra
      graph_tools_runner
    - test:
      cli_test
      test_dijkstra
  cli
  requirements
```
- graph_tools folder has models and utils to create Graph and find shortest path.
- test folder contains sytem and integration tests.
- cli.py is a main CLI file with commands to run.

## Testing

Install pytest:

```python
pip install pytest
```

Run test:

```python
python -m pytest ./test/
```
## Future improvements

- Add more flags for cli.
- Add more test cases.
- Improve Dijkstra with modifications for float and extremely big graphs.
