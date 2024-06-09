import igraph as ig
import itertools as itt

def get_graphlet(graph: ig.Graph, node_indices: list[int]):
    subgraph = graph.subgraph(node_indices)
    return subgraph


def count_motif(graph: ig.Graph, motif: ig.Graph):
    count = graph.count_subisomorphisms_vf2(motif)
    return count

def count_graphlet(graph, graphlet):
    count = 0
    for nodes in itt.combinations(graph.vs, graphlet.vcount()):
        subgraph = graph.subgraph([v.index for v in nodes])
        if subgraph.isomorphic(graphlet):
            count += 1
    return count