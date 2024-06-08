import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

def info(graph):
    print(f"{'Is Directed:'.ljust(25)} {graph.is_directed()}")
    print(f"{'Average Degree:'.ljust(25)} {sum(graph.degree()) / len(graph.degree())}")
    print(f"{'Max Degree:'.ljust(25)} {max(graph.degree())}")
    print(f"{'Clustering Coefficient:'.ljust(25)} {graph.transitivity_avglocal_undirected(mode='zero')}")
    print(f"{'Number of Vertices:'.ljust(25)} {graph.vcount()}")
    print(f"{'Number of Edges:'.ljust(25)} {graph.ecount()}")

def plot_degree_distribution(graph):
    degrees = graph.degree()
    values, counts = np.unique(degrees, return_counts=True)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.bar(values, counts, width=0.80, color='b')
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.subplot(1, 2, 2)
    plt.loglog(values, counts, 'b-', marker='o')
    plt.title('Log-Log Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()