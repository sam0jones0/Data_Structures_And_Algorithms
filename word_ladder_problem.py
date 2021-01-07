"""Solving the word ladder problem (change one word to another word of the same
length by changing one letter at a time. Each step must transform one word to
another word, you are not allowed to transform a word into a non-word) using an
Adjacency List Graph.
"""

from AdjacencyListGraph import Graph

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
            bucket = word[:i] + "_" + word[i+1:]
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


# TODO: Implement breadth first search.
