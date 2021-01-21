"""General depth first search graph with methods to search the nodes in a graph as
deeply as possible while connecting as many vertices in the graph as possible and
branching where necessary.
"""

from AdjacencyListGraph import Graph, Vertex


class DFSGraph(Graph):
    """Builds a depth first search graph, an extension of the AdjacencyListGraph
    class with a new variable "time", to track the discovery and finish time of
    each vertex's exploration.
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

    def topological_sort(self):
        """Produces a linear ordering of all vertices such that if the Graph G
        contains an edge (v, w) then the vertex v comes before the vertex w in
        the ordering. Returns a list of the ordered vertices.
        """
        vert_list = list(self.vert_list.values())
        vert_list.sort(key=lambda x: x.fin, reverse=True)
        return vert_list


# # Example of graph representing steps required to make pancakes. DFS and a topological
# # search produces a list of vertices sorted by order of completion in the full process.
# g = DFSGraph()
# g.add_edge("3/4 cup milk", "1 cup mix")
# g.add_edge("1 egg", "1 cup mix")
# g.add_edge("1 tbsp oil", "1 cup mix")
# g.add_edge("1 cup mix", "heat syrup")
# g.add_edge("1 cup mix", "pour 1/4 cup")
# g.add_edge("heat griddle", "pour 1/4 cup")
# g.add_edge("pour 1/4 cup", "turn when bubbly")
# g.add_edge("heat syrup", "eat")
# g.add_edge("turn when bubbly", "eat")
#
# g.depth_first_search()
# top_sorted = g.topological_sort()
# print([v.id for v in top_sorted])
