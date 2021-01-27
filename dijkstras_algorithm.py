"""Dijkstra’s algorithm is an iterative algorithm that provides us with the shortest
path from one particular starting node to all other nodes in the graph"""

from priorityQueue import PriorityQueue
from AdjacencyListGraph import Graph, Vertex


def dijkstra(a_graph: "Graph", start: "Vertex"):
    """Iterates over each vertex in a graph in order of distance between vertices
    controlled by a priority queue. Provided a weighted graph, the distances from
    the starting vertex to any given vertex are set correctly, along with each
    vertex's predecessor link.
    """
    pq = PriorityQueue()
    # "start" will be first in the PriorityQueue due to distance 0.
    start.set_distance(0)
    # The PriorityQueue class stores tuples of key, value pairs
    pq.buildHeap([(v.get_distance(), v) for v in a_graph])
    while not pq.isEmpty():
        current_vert: Vertex = pq.delMin()
        next_vert: Vertex
        for next_vert in current_vert.get_connections():
            new_dist = current_vert.get_distance() \
                     + current_vert.get_weight(next_vert)
            if new_dist < next_vert.get_distance():
                # This new route is shorter.
                next_vert.set_distance(new_dist)
                next_vert.set_predecessor(current_vert)
                # descreaseKey is used when the distance to a vertex that is already
                # in the queue is reduced, moving that vertex nearer the front.
                pq.decreaseKey(next_vert, new_dist)
