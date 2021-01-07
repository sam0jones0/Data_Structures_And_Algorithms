"""An Adjacency List Graph. A master list of all vertices is stored in the graph object
 and each vertex object maintains a list of all other vertices it is connected to.
"""


class Graph:
    """An Adjacency List Graph."""
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Add vertex to the graph with the provided key."""
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, key):
        """Return vertex associated with key."""
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, key):
        """Return True if vertex in graph, False otherwise."""
        return key in self.vert_list

    def add_edge(self, from_, to, weight=0):
        """Add edge between from_ and to vertices, with optional weight."""
        if from_ not in self.vert_list:
            new_vertex = self.add_vertex(from_)
        if to not in self.vert_list:
            new_vertex = self.add_vertex(to)
        self.vert_list[from_].add_neighbour(self.vert_list[to], weight)

    def get_vertices(self):
        """Return dict list of vertices' keys."""
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


class Vertex:
    """A Vertex (node) of an Adjacency List Graph."""
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def __str__(self):
        """Return string representation of this vertex and connected vertices IDs."""
        return str(self.id) + " connected_to " + str([nbr.id for nbr in self.connected_to])

    def add_neighbour(self, nbr, weight=0):
        """Add a connection from this vertex to another."""
        self.connected_to[nbr] = weight

    def get_connections(self):
        """Return dict keys of this vertex's connections."""
        return self.connected_to.keys()

    def get_id(self):
        """Return ID of this vertex."""
        return self.id

    def get_weight(self, nbr):
        """Return weight of edge between this vertices and a neighbour."""
        return self.connected_to[nbr]
