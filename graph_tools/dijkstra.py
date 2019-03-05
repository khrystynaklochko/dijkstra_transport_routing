import heapq

def shortest_path(v, path):
    # Building from previous
    if v.previous:
        path.append(v.previous.get_id())
        shortest_path(v.previous, path)
    return



def dijkstra(route, start_vertice, nearby):
    start_vertice.set_distance(0) # Start

    not_visited_vertices = [(v.get_distance(),v) for v in route] # Building visiting queue
    heapq.heapify(not_visited_vertices)

    while len(not_visited_vertices):
        # Taking smallest distance
        fresh_vertices = heapq.heappop(not_visited_vertices)
        current_vertice = fresh_vertices[1]
        current_vertice.set_visited()

        for next in current_vertice.adjacent:
            if next.visited:
                continue
            new_dist = current_vertice.get_distance() + current_vertice.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current_vertice)

        while len(not_visited_vertices):
            heapq.heappop(not_visited_vertices)
        not_visited_vertices = [(v.get_distance(),v) for v in route if not v.visited]
        heapq.heapify(not_visited_vertices) # Adding not visted to a queue

        # Taking all reachable nodes by time from queue
        for v in fresh_vertices:
            if 0 < fresh_vertices[0] <= int(nearby[start_vertice]):
               start_vertice.set_reachable_for_time(fresh_vertices[1].id, fresh_vertices[0])
