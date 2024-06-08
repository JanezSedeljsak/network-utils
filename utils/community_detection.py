import igraph as ig

def detect_communities_louvain(graph):
    partition = graph.community_multilevel()
    return partition

def detect_communities_girvan_newman(graph):
    dendrogram = graph.community_edge_betweenness()
    clusters = dendrogram.as_clustering()
    return clusters

def detect_communities_infomap(graph):
    clusters = graph.community_infomap()
    return clusters

def detect_communities_lpa(graph):
    clusters = graph.community_label_propagation()
    return clusters