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
    print(f"{'Gamma:'.ljust(25)} {calc_gamma(graph.degree())}")
    print(f"{'Number of Components:'.ljust(25)} {len(graph.decompose(mode='strong'))}")
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