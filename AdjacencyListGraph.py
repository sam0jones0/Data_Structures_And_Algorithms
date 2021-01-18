"""An Adjacency List Graph. A master list of all vertices is stored in the graph object
and each vertex object maintains a list of all other vertices it is connected to.
"""

import sys

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
        return list(self.vert_list.keys())

    def __iter__(self):
        return iter(self.vert_list.values())


class Vertex:
    """A Vertex (node) of an Adjacency List Graph."""
    def __init__(self, id):
        self.id = id
        self.connected_to = {}
        self.colour = 'white'
        self.dist = sys.maxsize
        self.predecessor = None
        self.disc = 0
        self.fin = 0

    def __str__(self):
        """Return string representation of this vertex, it's variables and
        connected vertices IDs.
        """
        return f"key:{str(self.id)} " + \
            f"colour:{self.colour} " + \
            f"disc:{str(self.disc)} " + \
            f"fin:{str(self.fin)} " + \
            f"dist:{str(self.dist)}\n" + \
            f"pred: [{str(self.predecessor)}]\n"

    def add_neighbour(self, nbr, weight=0):
        """Add a connection from this vertex to another."""
        self.connected_to[nbr] = weight

    def set_colour(self, colour):
        """Set vertex colour."""
        self.colour = colour

    def get_colour(self):
        """Return vertex colour."""
        return self.colour

    def set_distance(self, distance):
        """Set vertex distance."""
        self.dist = distance

    def get_distance(self):
        """Return vertex distance."""
        return self.dist

    def set_predecessor(self, pred):
        """Set vertex predecessor."""
        self.predecessor = pred

    def get_predecessor(self):
        """Return vertex predecessor."""
        return self.predecessor

    def set_discovery(self, dtime):
        """Set vertex discovery time."""
        self.disc = dtime

    def get_discovery(self):
        """Return vertex discovery time."""
        return self.disc

    def set_finish(self, ftime):
        """Set vertex finish time."""
        self.fin = ftime

    def get_finish(self):
        """Return vertex finish time."""
        return self.fin

    def get_connections(self):
        """Return dict keys of this vertex's connections."""
        return self.connected_to.keys()

    def get_id(self):
        """Return ID of this vertex."""
        return self.id

    def get_weight(self, nbr):
        """Return weight of edge between this vertices and a neighbour."""
        return self.connected_to[nbr]
