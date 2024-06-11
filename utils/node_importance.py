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

def mu_corrected_clustering(graph):
    local_cc = graph.transitivity_local_undirected(mode="zero")
    degrees = graph.degree()
    mu_corrected_cc = [cc / (degree if degree > 1 else 1) for cc, degree in zip(local_cc, degrees)]
    return mu_corrected_cc

def personalized_pagerank(graph, nodes, damping_factor=0.85):
    # Create a vector for the restart distribution
    restart_distribution = [0] * len(graph.vs)
    for node in nodes:
        restart_distribution[node] = 1

    # Compute Personalized PageRank
    scores = graph.personalized_pagerank(damping=damping_factor, reset=restart_distribution)
    return scores

def top_n_similar_nodes(graph, nodes, n=10):
    scores = personalized_pagerank(graph, nodes)
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    for node in nodes:
        sorted_indices.remove(node)
    return sorted_indices[:n], scores

def top_n_betweenness_nodes(G: Graph, n=10):
    betweenness = betweenness_centrality(G)
    sorted_indices = sorted(range(len(betweenness)), key=lambda i: betweenness[i], reverse=True)
    return sorted_indices[:n], betweenness