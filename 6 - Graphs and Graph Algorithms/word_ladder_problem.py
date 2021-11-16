"""Solving the word ladder problem (change one word to another word of the same
length by changing one letter at a time. Each step must transform one word to
another word, you are not allowed to transform a word into a non-word) using an
Adjacency List Graph.
"""

from AdjacencyListGraph import Graph, Vertex
from Queue_my import Queue


def build_graph(word_file):
    """Place words with only one differing letter into buckets (dictionaries),
    create a vertex for each word and create edges between all vertices which
    share the same dictionary key.
    """
    d = {}
    g = Graph()
    word_file = open(word_file, "r")

    # Create buckets of words that differ only by one letter.
    for line in word_file:
        word = line[:-1]
        for i in range(len(word)):
            # Replace each char of word with wildcard "_".
            bucket = word[:i] + "_" + word[i + 1 :]
            if bucket in d:
                # Append word to existing bucket.
                d[bucket].append(word)
            else:
                # Create new bucket.
                d[bucket] = [word]

    # Add vertices and edges for words in the same bucket.
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g


def breadth_first_search(graph: "Graph", start: "Vertex"):
    """Breadth first search of 'Graph' starting at 'start' vertex."""
    start.set_distance(0)
    start.set_predecessor(None)
    vertex_q = Queue()  # Queue tracks exploration order.
    vertex_q.enqueue(start)
    while vertex_q.size() > 0:
        current_vertex: Vertex = vertex_q.dequeue()
        nbr: Vertex
        for nbr in current_vertex.get_connections():
            if nbr.get_colour() == "white":
                # Explore an unexplored vertex: "white" and set colour "grey" /
                # to note initial discovery and exploration in progress.
                nbr.set_colour("grey")
                nbr.set_distance(current_vertex.get_distance() + 1)
                nbr.set_predecessor(current_vertex)
                vertex_q.enqueue(nbr)  # Add to queue for further exploration.
        # Set vertex color: "black" to note it has been fully explored. /
        # i.e. It has no "white" (undiscovered) adjacent vertices.
        current_vertex.set_colour("black")
    traverse(current_vertex)


def traverse(y: "Vertex"):
    """Follow the predecessor variable from y back to the tree root,
    printing out the word ladder in the process.
    """
    x: "Vertex" = y
    while x.get_predecessor():
        print(x.get_id())
        x = x.get_predecessor()
    print(x.get_id())


g = build_graph("word_ladder_words_file.txt")
start_vertex_key = list(g.get_vertices())[0]
start_vertex = g.get_vertex(start_vertex_key)
breadth_first_search(g, start_vertex)
traverse(start_vertex)
