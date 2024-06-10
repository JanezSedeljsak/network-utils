import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def info_as_dict(graph, approx_len=False):
    info_dict = {
        'Is Directed': graph.is_directed(),
        'Average Degree': sum(graph.degree()) / len(graph.degree()),
        'Max Degree': max(graph.degree()),
        'Clustering Coefficient': graph.transitivity_avglocal_undirected(mode='zero'),
        'Number of Vertices': graph.vcount(),
        'Number of Edges': graph.ecount(),
        'Gamma': calc_gamma(graph.degree()),
        'Number of Components': len(graph.decompose(mode='strong')),
        'LCC': max(c.vcount() for c in graph.decompose(mode='strong')) / graph.vcount(),
        'Number of Pendant Nodes': graph.degree().count(1),
        'Number of Isolated Nodes': graph.degree().count(0),
    }
    if approx_len:
        info_dict['Approx. Avg. Path Length'] = approximate_avg_path_length(graph)
    else:
        info_dict['Avg. Path Length'] = graph.average_path_length()
    
    return info_dict

def info(graph, approx_len=False):
    print(f"{'Is Directed:'.ljust(25)} {graph.is_directed()}")
    print(f"{'Average Degree:'.ljust(25)} {sum(graph.degree()) / len(graph.degree())}")
    print(f"{'Max Degree:'.ljust(25)} {max(graph.degree())}")
    print(f"{'Clustering Coefficient:'.ljust(25)} {graph.transitivity_avglocal_undirected(mode='zero')}")
    print(f"{'Number of Vertices:'.ljust(25)} {graph.vcount()}")
    print(f"{'Number of Edges:'.ljust(25)} {graph.ecount()}")
    print(f"{'Gamma:'.ljust(25)} {calc_gamma(graph.degree())}")
    print(f"{'Number of Components:'.ljust(25)} {len(graph.decompose(mode='strong'))}")
    print(f"{'Number of Pendant Nodes'.ljust(25)} {graph.degree().count(1)}")
    print(f"{'Number of Isolated Nodes'.ljust(25)} {graph.degree().count(0)}")
    lcc = (max(c.vcount() for c in graph.decompose(mode='strong')) / graph.vcount())
    print(f"{'LCC:'.ljust(25)} {lcc}")
    if approx_len:
        print(f"{'Approx. Avg. Path Length:'.ljust(25)} {approximate_avg_path_length(graph)}")
    else:
        print(f"{'Avg. Path Length:'.ljust(25)} {graph.average_path_length()}")

def components(graph):
    return graph.decompose(mode="strong")

def plot_deg(g):
    deg_dist = np.array(list(g.degree_distribution().bins()))
    deg_dist = deg_dist[(deg_dist[:, 2] > 0)]
    g_px, g_py = get_pcurve(g.degree())

    g_pk = deg_dist[:, 2] / g.vcount()
    g_k = deg_dist[:, 0]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.bar(g_k, g_pk, width=0.80, color='b')
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.subplot(1, 2, 2)
    plt.loglog(g_px, g_py, 'b--')
    plt.loglog(g_k, g_pk, 'bo')
    plt.title('Log-Log Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()


def approximate_avg_path_length(graph):
    total_path_length = 0
    num_pairs = 0

    # run avg distance 300 times to get O(300N) ~ O(N)
    for _ in range(300):
        source = random.choice(graph.vs)
        target = random.choice(graph.vs)
        
        if source != target:
            shortest_path_length = graph.distances(source, target)[0][0]
            if shortest_path_length != float('inf'):
                total_path_length += shortest_path_length
                num_pairs += 1
    
    if num_pairs > 0:
        approximate_avg_path_length = total_path_length / num_pairs
        return approximate_avg_path_length
    
    return -1

def standard_link_prediction(graph, num_samples):
    # randomly sample a set of unlinked node pairs
    unlinked_node_pairs = [(node1, node2) for node1 in graph.vs for node2 in graph.vs if node1.index != node2.index and not graph.are_connected(node1, node2)]
    sampled_node_pairs = random.sample(unlinked_node_pairs, min(num_samples, len(unlinked_node_pairs)))

    # remove a random set of node links
    edges = [edge for edge in graph.es]
    removed_edges = random.sample(edges, min(num_samples, len(edges)))
    graph.delete_edges(removed_edges)

    similarity_scores = []
    for node1, node2 in sampled_node_pairs:
        for edge in removed_edges:
            scores = graph.similarity_jaccard(pairs=[(node1.index, edge.source), (node1.index, edge.target), (node2.index, edge.source), (node2.index, edge.target)])
            similarity_scores.append(sum(scores) / len(scores))

    return np.mean(similarity_scores)


def calc_gamma(degs, k_min=5):
    degs = np.array(degs)
    Ks = degs[degs >= k_min]
    n, itt_divisor = Ks.shape[0], k_min - .5
    vec_sum = np.sum(np.log(Ks / itt_divisor))
    return 1 + n * (vec_sum ** -1)

def get_pcurve(degs):
    gamma = calc_gamma(degs)
    min_, max_ = min(degs), max(degs)
    pcurve_x = np.arange(min_, max_ + 1)
    pcurve_y = np.power(pcurve_x, -1 * gamma)
    return pcurve_x, pcurve_y


def modularity(g: ig.Graph):
    # uses louvian
    community = g.community_multilevel()
    modularity = g.modularity(community)
    return modularity

def calc_core_periphery_coefficient(g):
    A = np.array(g.get_adjacency().data)
    D = np.diag(A.sum(axis=1))
    L = D - A
    eigvals, eigvecs = np.linalg.eig(L)
    index = np.argsort(eigvals)[1]
    coreness = eigvecs[:, index]
    coreness = (coreness - np.min(coreness)) / (np.max(coreness) - np.min(coreness))
    core_periphery_coefficient = np.mean(coreness)
    return core_periphery_coefficient

def get_edges(graph):
    return graph.es

def get_node_names(graph):
    return graph.vs['name']

def get_node_indices(graph):
    return graph.vs.indices

def node_degree(graph, node_index):
    return graph.degree(node_index)

def get_degrees(graph):
    return graph.degree()

def degree_distrib(graph):
    degrees = graph.degree()
    return {i: degrees.count(i) for i in set(degrees)}

def nodes_are_connected(graph, node_index1, node_index2):
    return graph.are_adjacent(node_index1, node_index2)

def add_node(graph, name=None):
    graph.add_vertex(name=name)

def remove_node(graph, node_index):
    graph.delete_vertices(node_index)

def connect_nodes(graph, node_index1, node_index2):
    graph.add_edge(node_index1, node_index2)

def neighbors(graph, node_index):
    return graph.neighbors(node_index)

def disconnect_nodes(graph, node_index1, node_index2):
    edge_id = graph.get_eid(node_index1, node_index2, error=False)
    if edge_id != -1:
        graph.delete_edges(edge_id)

def to_networkx(graph: ig.Graph):
    networkx_graph = nx.DiGraph() if graph.is_directed() else nx.Graph()
    networkx_graph.add_edges_from(graph.get_edgelist())
    return networkx_graph