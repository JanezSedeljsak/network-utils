from utils import *
import igraph as ig
import random

random.seed(12) # deterministic execution
graph = ig.Graph.Erdos_Renyi(n=10, m=20)

def test_motifs():
    global graph
    motif1 = ig.Graph.TupleList([(0,1), (1,2), (2,0)]) # triangle
    motif2 = ig.Graph.TupleList([(0,1), (1,2)]) # line
    motif3 = ig.Graph.TupleList([(0,1), (1,2), (2,3), (3,0)]) # square

    count1 = count_motif(graph, motif1)
    count2 = count_motif(graph, motif2)
    count3 = count_motif(graph, motif3)
    assert count1 == 48, f"Triangle count should be 48, got {count1}"
    assert count2 == 132, f"Line count should be 132, got {count2}"
    assert count3 == 152, f"Square count should be 152, got {count3}"


def test_graphlet():
    global graph
    node_indices = [0, 1, 2]
    graphlet = get_graphlet(graph, node_indices)
    assert graphlet.vcount() == len(node_indices), f"Graphlet should have {len(node_indices)} nodes, got {graphlet.vcount()}"
    for node_index in node_indices:
        assert node_index in get_node_indices(graphlet), f"Node {node_index} should be in the graphlet"

    for node1 in node_indices:
        for node2 in node_indices:
            if node1 != node2 and graph.are_adjacent(node1, node2):
                assert graphlet.are_adjacent(node1, node2), f"Edge ({node1}, {node2}) should be in the graphlet"

    graphlet_count = count_graphlet(graph, graphlet)
    assert graphlet_count == 42, f"Graphlet count should be 42, got {graphlet_count}"

if __name__ == '__main__':
    test_motifs()
    test_graphlet()