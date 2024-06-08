import igraph as ig
import networkx as nx

def read_ajd(file_path):
    with open(file_path, 'r') as file:
        for _ in range(4):
            next(file) # skip line
            
        edges = [tuple(map(int, line.split())) for line in file]
    return ig.Graph.TupleList(edges, directed=True)


def read_pajek(path):
    nx_graph = nx.read_pajek(path)
    mapping = {node: i for i, node in enumerate(nx_graph.nodes())}
    g_ig = ig.Graph()
    g_ig.add_vertices(len(mapping))
    g_ig.add_edges((mapping[u], mapping[v]) for u, v in nx_graph.edges())
    # g_ig.vs['label'] = list(mapping.keys())
    g_ig.vs['name'] = list(mapping.keys())
    return g_ig