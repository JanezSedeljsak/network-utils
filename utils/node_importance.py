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

def personalized_pagerank(graph, node, damping_factor=0.85):
    # Create a vector for the restart distribution
    restart_distribution = [0] * len(graph.vs)
    restart_distribution[node] = 1

    # Compute Personalized PageRank
    scores = graph.personalized_pagerank(damping=damping_factor, reset=restart_distribution)
    return scores

def top_n_similar_nodes(graph, node, n=10):
    scores = personalized_pagerank(graph, node)
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    sorted_indices.remove(node)
    return sorted_indices[:n]