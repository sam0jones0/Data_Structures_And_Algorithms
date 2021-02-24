"""Algorithm to construct a minimum weight spanning tree. This is an acyclic subset
of a graph's edges that connects all the vertices. The sum of the weights of the
edges is minimised."""

from priorityQueue import PriorityQueue
from AdjacencyListGraph import Graph, Vertex


def prim_spanning_tree(a_graph: "Graph", start: "Vertex"):
    """Construct a minimum weight spanning tree, connecting all vertices acyclicly
    from "start" while minimising the weight of all the edges in the tree.
    Graph is modified in place; the distance attr from start to each other vertex
    is set to the minimum possible value.
    """
    pq = PriorityQueue()
    vertex: Vertex
    for vertex in a_graph:
        # Ensure dist and pred are set to default values.
        vertex.set_distance_max()
        vertex.set_predecessor(None)
    # "start" will be first in the PriorityQueue due to distance 0.
    start.set_distance(0)
    # The PriorityQueue class stores tuples of key, value pairs
    pq.buildHeap([(v.get_distance(), v) for v in a_graph])
    while not pq.isEmpty():
        # Add the vertex at the front of the priority queue to the tree.
        current_vertex: Vertex = pq.delMin()
        next_vertex: Vertex
        for next_vertex in current_vertex.get_connections():
            new_cost = current_vertex.get_weight(next_vertex)
            if next_vertex in pq and new_cost < next_vertex.get_distance():
                # Only consider vertices that are not already in the tree.
                next_vertex.set_distance(new_cost)
                next_vertex.set_predecessor(current_vertex)
                # descreaseKey is used when the distance to a vertex that is already
                # in the queue is reduced, moving that vertex nearer the front.
                pq.decreaseKey(next_vertex, new_cost)
