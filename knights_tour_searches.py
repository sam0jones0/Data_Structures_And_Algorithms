"""Various graph search algorithms solving the knights tour problem using an
 adjacency list graph which represents the legal moves of a knight chess piece
 as generated by knights_tour_graph.py"""

from AdjacencyListGraph import Graph, Vertex
from knights_tour_graph import build_knight_graph


def knights_tour_dfs(current_depth, path, vertex, limit):
    """Recursive depth first search to return a valid path for the knights tour problem.
    current_depth: Current depth in the search tree (start at 0)
    path: A list of vertices visited up to the current point in time.
    vertex: The current vertex we wish to explore (initially used as search start point.
    limit: The total number of nodes in the path, used as the base case.
    This algorithm is exponential and very slow: O(k**N)."""
    vertex.set_colour('gray')  # Denotes visited.
    path.append(vertex)
    if current_depth < limit:
        # There are still unvisited vertices.
        neighbour_list = list(vertex.get_connections())
        i = 0
        done = False
        while i < len(neighbour_list) and not done:
            # There are still unexplored neighbours.
            if neighbour_list[i].get_colour() == 'white':
                # This node is unvisited.
                done = knights_tour_dfs(current_depth + 1, path, neighbour_list[i], limit)
            i += 1
        if not done:  # No unvisited neighbours/dead end. Prepare to backtrack.
            path.pop()
            vertex.set_colour('white')
    else:
        done = True
        print([v.id for v in path])

    return done


# # Example run for knights_tour_dfs
# board_size = 8
# knight_graph = build_knight_graph(board_size)
# start_vertex = knight_graph.vert_list[0]
#
# knights_tour_dfs(0, [], start_vertex, 63)


# TODO: Other search algorithms.
