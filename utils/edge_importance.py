from igraph import Graph

def edge_betweenness(G: Graph):
    return G.edge_betweenness()

def edge_closeness(G: Graph):
    # There's no direct method for edge closeness in igraph, but it can be computed
    # based on the closeness of the nodes that the edge is connecting.
    return [(G.closeness(v=source) + G.closeness(v=target)) / 2 for source, target in G.get_edgelist()]

def edge_eigenvector_centrality(G: Graph):
    # There's no direct method for edge eigenvector centrality in igraph, but it can be computed
    # based on the eigenvector centrality of the nodes that the edge is connecting.
    node_eigenvector_centrality = G.eigenvector_centrality()
    return [(node_eigenvector_centrality[source] + node_eigenvector_centrality[target]) / 2 for source, target in G.get_edgelist()]

def random_walk_accessibility(G: Graph, steps=3):
    # There's no direct method for random walk accessibility in igraph, but it can be computed
    # based on the adjacency matrix and the number of steps.
    adjacency_matrix = G.get_adjacency()
    accessibility_matrix = adjacency_matrix ** steps
    return [(accessibility_matrix[source, target] + accessibility_matrix[target, source]) / 2 for source, target in G.get_edgelist()]