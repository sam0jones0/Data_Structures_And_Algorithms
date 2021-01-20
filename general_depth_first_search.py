"""General depth first search graph with methods to search the nodes in a graph as
deeply as possible while connecting as many vertices in the graph as possible and
branching where necessary.

This extends the AdjacencyListGraph class with a new variable "time", to track the
discovery and finish time of each vertex's exploration.
"""

from AdjacencyListGraph import Graph, Vertex


class DFSGraph(Graph):
    """Builds a depth first search graph.
    TODO
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def depth_first_search(self):
        """Iterate over all the unexplored vertices in a graph by calling dfs_visit
         on each vertex.
         """
        for vertex in self:  # Here, self represents all vertices in the graph.
            vertex.set_colour("white")
            vertex.set_predecessor(-1)
        for vertex in self:
            if vertex.get_colour() == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex: "Vertex"):
        """Starting with start_vertex, recursively explore all the neighbouring
         unexplored vertices as deeply as possible.
         """
        start_vertex.set_colour("grey")
        self.time += 1
        start_vertex.set_discovery(self.time)
        next_vertex: Vertex
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_colour() == "white":
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.set_colour("black")
        self.time += 1
        start_vertex.set_finish(self.time)
