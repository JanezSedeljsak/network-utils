import igraph as ig

def erdos(n=300, p=0.2, directed=False):
    random_graph = ig.Graph.Erdos_Renyi(n=n, p=p, directed=directed)
    return random_graph

def watts_strogatz(n=300, k=4, p=0.1):
    ws_graph = ig.Graph.Watts_Strogatz(dim=1, size=n, nei=k, p=p)
    return ws_graph

def stochastic_block_model(n=300, p_matrix=[[0.5, 0.1], [0.1, 0.5]]):
    blocks = [n // 2, n // 2]  # Assuming two equal-sized blocks for simplicity
    sbm_graph = ig.Graph.SBM(n=blocks, pref_matrix=p_matrix)
    return sbm_graph

def price(n=300, m=3):
    price_graph = ig.Graph.Barabasi(n=n, m=m)
    return price_graph