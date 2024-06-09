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

def test_get_edges():
    graph = ig.Graph.Erdos_Renyi(n=10, m=20)
    edges = get_edges(graph)
    assert len(edges) == 20, f"Expected 20 edges, got {len(edges)}"

def test_get_node_names():
    graph = ig.Graph(n=3)
    graph.vs["name"] = ["A", "B", "C"]
    names = get_node_names(graph)
    assert names == ["A", "B", "C"], f"Expected ['A', 'B', 'C'], got {names}"

def test_get_node_indices():
    graph = ig.Graph(n=3)
    indices = get_node_indices(graph)
    assert indices == [0, 1, 2], f"Expected [0, 1, 2], got {indices}"

def test_node_degree():
    graph = ig.Graph(n=3)
    graph.add_edge(0, 1)
    degree = node_degree(graph, 0)
    assert degree == 1, f"Expected degree 1, got {degree}"

def test_get_degrees():
    graph = ig.Graph(n=3)
    graph.add_edge(0, 1)
    degrees = get_degrees(graph)
    assert degrees == [1, 1, 0], f"Expected degrees [1, 1, 0], got {degrees}"

def test_degree_distrib():
    graph = ig.Graph(n=3)
    graph.add_edge(0, 1)
    distrib = degree_distrib(graph)
    assert distrib == {1: 2, 0: 1}, f"Expected distribution {1: 2, 0: 1}, got {distrib}"

def test_nodes_are_connected():
    graph = ig.Graph(n=3)
    graph.add_edge(0, 1)
    assert nodes_are_connected(graph, 0, 1), "Nodes 0 and 1 should be connected"

def test_add_node():
    graph = ig.Graph(n=3)
    graph.vs['name'] = [str(i) for i in graph.vs.indices]
    add_node(graph, "D")
    assert "D" in get_node_names(graph), "Node 'D' should be in the graph"

def test_remove_node():
    # important when we delete a node all the vertexes get new indices
    graph = ig.Graph(n=3)
    remove_node(graph, 1)
    assert len(get_node_indices(graph)) == 2, "The graph should have 2 nodes"

def test_connect_nodes():
    graph = ig.Graph(n=3)
    connect_nodes(graph, 0, 2)
    assert nodes_are_connected(graph, 0, 2), "Nodes 0 and 2 should be connected"

def test_disconnect_nodes():
    graph = ig.Graph(n=3)
    graph.add_edge(0, 1)
    disconnect_nodes(graph, 0, 1)
    assert not nodes_are_connected(graph, 0, 1), "Nodes 0 and 1 should not be connected"

if __name__ == '__main__':
    test_motifs()
    test_graphlet()
    test_get_edges()
    test_get_node_names()
    test_get_node_indices()
    test_node_degree()
    test_get_degrees()
    test_degree_distrib()
    test_nodes_are_connected()
    test_add_node()
    test_remove_node()
    test_connect_nodes()
    test_disconnect_nodes()