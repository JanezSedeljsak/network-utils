<h3>Graph representations</h3>

**Adjacency Matrix**: This is a two-dimensional matrix where the cell at the intersection of row i and column j indicates the presence (and possibly the weight) of an edge between vertices i and j.
Strengths:
- Quick lookup of the presence of specific edges, which is an O(1) operation.
- Directly supports operations that involve pairs of vertices, such as determining whether two vertices are connected.
- Useful for dense graphs where most pairs of vertices are connected.

**Adjacency List**: This is a list or array where the element at position i is a list of the vertices that vertex i is connected to.
Strengths:
- Efficient memory usage for sparse graphs where most pairs of vertices are not connected.
- Quick iteration over the neighbors of a vertex, which is useful for graph traversal algorithms like depth-first search (DFS) and breadth-first search (BFS).
- Adding or removing edges is efficient.

**Edge List**: This is a list of pairs (or tuples) representing the edges of the graph. Each pair contains two vertices that are connected by an edge.
- Simple and flexible representation that's easy to manipulate.
- Efficient memory usage for both sparse and dense graphs.
- Useful for algorithms that need to iterate over all edges of the graph, such as Kruskal's algorithm for finding a minimum spanning tree.
- Adding or removing edges is straightforward and efficient.


<h3>Random graphs</h3>

**Erdos-Renyi Model**: This is one of the simplest random graph generation models. In the G(n, p) model, a graph is constructed by connecting nodes randomly. Each edge is included in the graph with probability p independent from every other edge.

**Watts-Strogatz Model**: This model generates small-world networks which exhibit properties of high clustering coefficient and small shortest path length. It starts with a regular lattice where each node is connected to k nearest neighbors and then rewires the edges randomly with a probability p.

**Stochastic Block Model**: This model generates graphs with community structure. Nodes are divided into groups or "blocks", and the probability of an edge existing between two nodes depends on the blocks that those nodes belong to.

**Price Model**: Also known as the preferential attachment model, it is a model for generating networks with scale-free properties. New nodes are added to the graph one at a time, and each new node is connected to existing nodes with a probability proportional to their degree.


<h3>Network properties</h3>

**Small-World Networks**: These are a type of graph where most nodes are not neighbors of one another, but the neighbors of any given node are likely to be neighbors of each other, and most nodes can be reached from every other node by a small number of hops or steps. In other words, small-world networks have high clustering coefficient and small average path length. The Watts-Strogatz model is a famous model for generating small-world networks.

**Scale-Free Networks**: These are networks whose degree distribution follows a power law, at least asymptotically. That is, the fraction P(k) of nodes in the network having k connections to other nodes goes for large values of k as P(k) ~ k^(-gamma). In these networks, some nodes (called "hubs") have a significantly higher degree than others. The Barabasi-Albert model is a well-known model for generating scale-free networks.

**Gamma Values**: The gamma value is the exponent in the power-law degree distribution P(k) ~ k^(-gamma) of scale-free networks.

For scale-free networks, the gamma value is typically between 2 and 3. This means that there are a few nodes with a very high degree and many nodes with a low degree.

For small-world networks, the concept of gamma is not typically used, as their degree distribution does not follow a power law. Instead, they are characterized by a high clustering coefficient and a small average path length.


<h3>Community detection</h3>

**Louvain Method**: The Louvain method is a greedy optimization method that attempts to optimize the "modularity" of a partition of the network. Modularity is a scalar value between -1 and 1 that measures the density of links inside communities as compared to links between communities. The higher the modularity, the better the partition.

**Girvan-Newman Algorithm**: This algorithm detects communities by progressively removing edges from the original graph. The algorithm removes the "most valuable" edge, traditionally the edge with the highest betweenness centrality, at each step. As the graph breaks down into pieces, the tightly knit community structure is exposed.

**Infomap**: Infomap is based on the idea that information flows through a network and often gets stuck in densely connected parts of the network, i.e., communities. The algorithm uses the probability flow of random walks as a proxy for information flows in the real system and decomposes the network into modules that minimize the expected description length of a random walker's movements on the network.

**Label Propagation Algorithm (LPA)**: The algorithm doesn’t require a priori information about the number of clusters and can unveil hierarchies of communities, where each node is assigned a unique label and at every step each node adopts the label that most of its neighbors currently have. In this iterative procedure, densely connected groups of nodes form a consensus on a unique label to form communities.

<h3>Node importance</h3>

1. **Degree Centrality**: This is the simplest measure of node centrality. It is calculated as the number of edges connected to a node. In directed networks, you can further distinguish between in-degree and out-degree centrality.

2. **Closeness Centrality**: This measure calculates the average length of the shortest path from a node to all other nodes in the network. Nodes with lower average shortest paths have higher closeness centrality.

3. **Betweenness Centrality**: This measure calculates the number of shortest paths from all nodes to all others that pass through a particular node. Nodes that occur on many shortest paths have higher betweenness centrality.

4. **Eigenvector Centrality**: This measure assigns relative scores to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes.

5. **PageRank**: This is a variant of Eigenvector Centrality, used by Google to rank websites in their search engine results. It measures the importance of each node within the network.