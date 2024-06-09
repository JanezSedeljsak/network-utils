import igraph as ig
import numpy as np

def erdos(n=300, p=0.2, directed=False):
    random_graph = ig.Graph.Erdos_Renyi(n=n, p=p, directed=directed)
    return random_graph

def watts_strogatz(n=300, k=4, p=0.1):
    ws_graph = ig.Graph.Watts_Strogatz(dim=1, size=n, nei=k, p=p)
    return ws_graph

def generate_configuration_model(degree_sequence=[2, 3, 1, 1, 1, 2, 1, 1, 1, 1]):
    return ig.Graph.Degree_Sequence(degree_sequence)

def stochastic_block_model(n=300, p_matrix=[[0.5, 0.1], [0.1, 0.5]]):
    blocks = [n // 2, n // 2]
    sbm_graph = ig.Graph.SBM(n=blocks, pref_matrix=p_matrix)
    return sbm_graph

def price(n=300, m=3):
    price_graph = ig.Graph.Barabasi(n=n, m=m)
    return price_graph

def generate_hierarchical_model(n=10, children=3):
    return ig.Graph.Tree(n=n, children=children)

def generate_stochastic_block_model(sizes=[10, 10, 10], probs=[[0.8, 0.1, 0.1], [0.1, 0.8, 0.1], [0.1, 0.1, 0.8]]):
    n = sum(sizes)
    labels = np.hstack([[i]*size for i, size in enumerate(sizes)])
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if np.random.rand() < probs[labels[i], labels[j]]:
                edges.append((i, j))
    return ig.Graph(n=n, edges=edges)