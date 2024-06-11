import igraph as ig
import numpy as np
import networkx as nx
from node2vec import Node2Vec

graph = ig.Graph.Erdos_Renyi(n=100, m=500)

nx_graph = nx.Graph()
for edge in graph.es:
    nx_graph.add_edge(edge.source, edge.target)

node2vec = Node2Vec(nx_graph, dimensions=64, walk_length=30, num_walks=200, workers=4)
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# find the most similar nodes to a given node (e.g., node '1')
# cosine similarity
def most_similar(node, topn=5):
    return model.wv.most_similar(str(node), topn=topn)

print(most_similar(1))