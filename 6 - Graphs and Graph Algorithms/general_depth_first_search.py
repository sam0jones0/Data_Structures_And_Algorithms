"""General depth first search graph with methods to search the nodes in a graph as
deeply as possible while connecting as many vertices in the graph as possible and
branching where necessary.

There are also methods for identifying Strongly Connected Components (scc) within
a graph.
"""

import copy

from AdjacencyListGraph import Graph, Vertex


class DFSGraph(Graph):
    """Builds a depth first search graph, an extension of the AdjacencyListGraph
    class with a new variable "time", to track the discovery and finish time of
    each vertex's exploration.
    """

    def __init__(self):
        super().__init__()
        self.time = 0

    def copy(self):
        """Makes a deepcopy of self and returns it."""
        return copy.deepcopy(self)

    def depth_first_search(self, compute_scc=False):
        """Iterate over all the unexplored vertices in a graph by calling dfs_visit
        on each vertex.
        If compute_scc=True then strongly connected components will be grouped
        together into sublists.
        """
        if compute_scc:
            # Only used when computing SCC to group connected vertices.
            subtree_idx = -1
            subtree_list = []

        for vertex in self:  # Here, self represents all vertices in the graph.
            vertex.set_colour("white")

        for vertex in self:
            if vertex.get_colour() == "white":
                if compute_scc:
                    # Set the index of and append to the subtree_list this scc group.
                    subtree_idx += 1
                    subtree_list.append([vertex.id])
                    self.dfs_visit(
                        vertex, subtree_idx=subtree_idx, subtree_list=subtree_list
                    )
                else:
                    self.dfs_visit(vertex)

        if compute_scc:
            return subtree_list

    def dfs_visit(self, start_vertex: "Vertex", subtree_idx=0, subtree_list=None):
        """Starting with start_vertex, recursively explore all the neighbouring
        unexplored vertices as deeply as possible.
        If a subtree_list is provided, add scc vertices to their corresponding scc
        subtree list.
        """
        start_vertex.set_colour("grey")
        self.time += 1
        start_vertex.set_discovery(self.time)
        next_vertex: Vertex
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_colour() == "white":
                if subtree_list:
                    # Add members of this scc group to their corresponding subtree_list.
                    next_vertex.set_predecessor(start_vertex)
                    subtree_list[subtree_idx] += [next_vertex.id]
                    self.dfs_visit(next_vertex, subtree_idx, subtree_list)
                else:
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

    def transpose(self):
        """All the edges in the graph are reversed. That is, if there is a directed edge
        from node A to node B in the original graph then the new graph will contain an
        edge from node B to node A.

        Returns a new modified graph, leaving the original unchanged.
        """
        new_graph = self.copy()
        # Clear new_graph connections/edges.
        for new_vertex in new_graph:
            new_vertex.connected_to = {}
        # Reverse connections and add edges to new_graph.
        for vertex in self:
            for connection in vertex.get_connections():
                new_graph.add_edge(connection.id, vertex.id)

        return new_graph

    def compute_strongly_connected_components(self):
        """A strongly connected component, C, of a graph G, is the largest subset
        of vertices C⊂V such that for every pair of vertices v,w∈C we have a path
        from v to w and a path from w to v.
        Returns nested lists of strongly connected components.
        """
        self.depth_first_search()
        transposed_graph = self.transpose()
        # Sort vertex list by decreasing order of finish time.
        verts_desc_by_fin = sorted(
            transposed_graph.vert_list.items(), key=lambda x: x[1].fin, reverse=True
        )
        # Sorted list is converted back to a dictionary.
        verts_desc_by_fin = {v[0]: v[1] for v in verts_desc_by_fin}
        transposed_graph.vert_list = verts_desc_by_fin
        # DFS on the transposed/sorted graph reveals strongly connected components.
        transposed_graph.clear_vertices_attrs()
        scc_trees = transposed_graph.depth_first_search(compute_scc=True)

        return scc_trees

    def clear_vertices_attrs(self):
        """Clear attributes that must be empty for DFS to be re-run. Primarily used
        before searching a transposed graph."""
        self.time = 0
        for vertex in self:
            vertex.colour = "white"
            vertex.predecessor = None
            vertex.disc = 0
            vertex.fin = 0


# # Creating a graph with 3 Strongly Connected Components.
# g = DFSGraph()
# g.add_edge("A", "B")
# g.add_edge("B", "E")
# g.add_edge("E", "D")
# g.add_edge("E", "A")
# g.add_edge("D", "B")
# g.add_edge("D", "G")
# g.add_edge("G", "E")
# g.add_edge("B", "C")
# g.add_edge("C", "C")
# g.add_edge("C", "F")
# g.add_edge("F", "H")
# g.add_edge("H", "I")
# g.add_edge("I", "F")
#
# strongly_connected_components = g.compute_strongly_connected_components()
# print(strongly_connected_components)  # Prints: [['A', 'E', 'B', 'D', 'G'], ['C'], ['F', 'I', 'H']]

#######################

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
