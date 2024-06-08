from igraph import Graph

def degree_centrality(G: Graph):
    return G.degree()

def closeness_centrality(G: Graph):
    return G.closeness()

def betweenness_centrality(G: Graph):
    return G.betweenness()

def eigenvector_centrality(G: Graph):
    return G.eigenvector_centrality()

def pagerank(G: Graph):
    return G.pagerank()