"""Solving the knight's tour problem (find a sequence of moves on a chess board
to allow a single knight piece to visit every square on the board exactly once)
using an Adjacency List Graph and drawing a PDF representation.
"""

import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

from AdjacencyListGraph import Graph, Vertex

# Board size variable can be any positive int.
board_size = 8


def build_knight_graph(board_size) -> Graph:
    """Builds graph with nodes for each board position and adds edges from each
    to nodes reachable by a legal knight's move.
    """
    knight_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            new_positions = gen_legal_moves(row, col, board_size)
            for each in new_positions:
                next_node_id = pos_to_node_id(each[0], each[1], board_size)
                knight_graph.add_edge(node_id, next_node_id)

    return knight_graph


def pos_to_node_id(row, col, board_size):
    """Converts a board co-ordinate to a linear vertex number/key and returns it."""
    return (row * board_size) + col


def gen_legal_moves(row, col, board_size):
    """Generates a list of legal knight move co-ordinates from the provided
    row/col co-ordinate.
    """
    new_moves = []
    move_offsets = [
        (-1, -2),
        (-1, 2),
        (-2, -1),
        (-2, 1),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    for move in move_offsets:
        if is_legal_coord(row + move[0], col + move[1], board_size):
            new_moves.append((row + move[0], col + move[1]))

    return new_moves


def is_legal_coord(row, col, board_size):
    """Return True if provided co-ordinate fits on a board of board_size, otherwise False"""
    if 0 <= row < board_size and 0 <= col < board_size:
        return True
    else:
        return False


def draw_graph_pdf(graph, board_size):
    """Create the data necessary for matplotlib and networkx, and have them draw a
    PDF representation of the graph.
    """
    matplotlib.use("Agg")

    # Parse graph data and create grid co-ordinates.
    graph_data = parse_graph_for_nx(graph, board_size)
    nx_graph = nx.Graph(graph_data)
    pos = get_graph_pos(board_size)
    nx.draw_networkx(
        nx_graph,
        pos=pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="k",
        font_size=8,
    )

    # Draw the graph and save as PDF.
    plt.axis("off")
    plt.draw()
    plt.savefig("knight_moves_graph.pdf")


def parse_graph_for_nx(graph, board_size):
    """Parse our adjacency list graph data structure into networkx readable format."""
    graph_adjacency_list = {}
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            current_node: Vertex = graph.get_vertex(node_id)
            cur_node_connections = current_node.get_connections()
            connection_keys = [v.get_id() for v in cur_node_connections]
            # Weight is set to 1 for all nodes.
            graph_adjacency_list[node_id] = {e: 1 for e in connection_keys}

    return graph_adjacency_list


def get_graph_pos(board_size):
    """Create a list of vertex co-ordinates in grid formation."""
    pos = {}
    nx_grid = nx.grid_2d_graph(board_size, board_size)
    grid_coords = iter([node for node in nx_grid.nodes()])
    for i in range(board_size ** 2):
        pos[i] = next(grid_coords)

    return pos


# knight_graph = build_knight_graph(board_size)
# draw_graph_pdf(knight_graph, board_size)
