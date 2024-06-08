import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def info(graph, approx_len=False):
    print(f"{'Is Directed:'.ljust(25)} {graph.is_directed()}")
    print(f"{'Average Degree:'.ljust(25)} {sum(graph.degree()) / len(graph.degree())}")
    print(f"{'Max Degree:'.ljust(25)} {max(graph.degree())}")
    print(f"{'Clustering Coefficient:'.ljust(25)} {graph.transitivity_avglocal_undirected(mode='zero')}")
    print(f"{'Number of Vertices:'.ljust(25)} {graph.vcount()}")
    print(f"{'Number of Edges:'.ljust(25)} {graph.ecount()}")
    if approx_len:
        print(f"{'Approx. Avg. Path Length:'.ljust(25)} {approximate_avg_path_length(graph)}")
    else:
        print(f"{'Avg. Path Length:'.ljust(25)} {graph.average_path_length()}")

def components(graph):
    return graph.decompose(mode='strong')

def plot_degree_distribution(graph):
    degrees = graph.degree()
    values, counts = np.unique(degrees, return_counts=True)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.bar(values, counts, width=0.80, color='b')
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.subplot(1, 2, 2)
    plt.loglog(values, counts, 'b-', marker='o')
    plt.title('Log-Log Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()


def read_pajek(path):
    nx_graph = nx.read_pajek(path)
    mapping = {node: i for i, node in enumerate(nx_graph.nodes())}
    g_ig = ig.Graph()
    g_ig.add_vertices(len(mapping))
    g_ig.add_edges((mapping[u], mapping[v]) for u, v in nx_graph.edges())
    # g_ig.vs['label'] = list(mapping.keys())
    g_ig.vs['name'] = list(mapping.keys())
    return g_ig


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

def read_ajd(file_path):
    with open(file_path, 'r') as file:
        for _ in range(4):
            next(file) # skip line
            
        edges = [tuple(map(int, line.split())) for line in file]
    return ig.Graph.TupleList(edges, directed=True)

def erdos(n=300, p=0.2, directed=False):
    random_graph = ig.Graph.Erdos_Renyi(n=n, p=p, directed=directed)
    return random_graph

def barabasi(n=300, m=2):
    g = ig.Graph.Barabasi(n=n, m=m)
    return g