<h3>Some terminology</h3>

- **Degree**: The degree of a vertex is the number of edges connected to it. In directed graphs, we distinguish between in-degree (number of incoming edges) and out-degree (number of outgoing edges).
- **Pendant Vertex**: A pendant vertex is a vertex that has a degree of 1. This means it is connected to the graph by a single edge.
- **Isolated Vertex**: An isolated vertex is a vertex with a degree of 0, meaning it has no edges connecting it to any other vertex in the graph.
- **Adjacent Vertices**: Two vertices are said to be adjacent if they are both endpoints of the same edge.
- **Incident Edges**: An edge is said to be incident to a vertex if the vertex is one of the endpoints of the edge.

<h3>Random facts</h3>

- The density `ρ` of an undirected graph `G` is defined as:
$$ρ = \frac{m}{{n \choose 2}} = \frac{2m}{n(n-1)} = \frac{\langle k \rangle}{n-1}$$

- The density `ρ` of a directed graph `G` is defined as:
$$ρ = \frac{m}{n(n-1)} = \frac{\langle k_{in} \rangle}{n-1} = \frac{\langle k_{out}\rangle}{n-1}$$

- For an undirected graph `G`, the node clustering coefficient `Ci` of a node `i` is defined as:
$$Ci = \frac{ti}{{ki \choose 2}}$$
where `ti` is the number of linked neighbors or triangles of `i`. `Ci` is 0 for `ki ≤ 1`.

- The average clustering coefficient `<C>` is defined as:

$$\langle C \rangle = \frac{1}{n} \sum_{i} Ci$$

- **Geodesic Path**: The shortest path between two nodes in a graph, with the smallest number of edges (unweighted) or smallest sum of edge weights (weighted).

- **Distance**: The length of the geodesic path between two nodes, counted by edges (unweighted) or sum of edge weights (weighted).

- **Graph Diameter**: The greatest distance between any pair of nodes, i.e., the length of the longest geodesic path.

- **Average Distance**: The mean distance between all node pairs, calculated by summing all distances and dividing by the total number of pairs. It indicates the overall connectivity of the graph.


- **Small world**:
    - Random graphs are "small-world" as $\langle d \rangle \approx \frac{\ln n}{\ln \langle k \rangle}$
    - Random graphs are not small-world as $\langle C \rangle = \frac{\langle k \rangle}{n-1}$
    - Scale-free networks $\gamma = 3$ are "small-world" as $\langle d \rangle \sim \frac{\ln n}{\ln \ln n}$
    - $G(n, c)$ scale-free model is not small-world as $\langle C \rangle \approx \frac{(\ln n)^2}{n}$

- **Strongly Connected Components**: A strongly connected component of a directed graph is a subgraph where there is a directed path from any node to any other node. In other words, you can get from any node in the subgraph to any other node in the subgraph by following the directed edges.

- **Weakly Connected Components**: A weakly connected component of a directed graph is a subgraph where there is a path from any node to any other node if we ignore the direction of the edges. In other words, if you replace all directed edges with undirected edges, all nodes in the subgraph are connected.

- **High modularity and low clustering coefficient** (e.g., a network of star-shaped communities)

- **Low modularity and high clustering coefficient** (e.g., a network with a lot of triangles but no larger communities).

<h3>Graph types in the core</h3>

- **Directed Graphs**: In these graphs, edges have a direction. That is, the edge from node A to node B is not the same as the edge from node B to node A.

- **Undirected Graphs**: In these graphs, edges do not have a direction. The edge between node A and node B is the same as the edge between node B and node A.

- **Multipartite Graphs**: These are graphs whose vertices can be divided into multiple disjoint sets such that no two graph vertices within the same set are adjacent.

- **Multigraphs**: These are graphs which permit multiple edges (also called parallel edges), i.e., edges that have the same end nodes. Thus, two vertices may be connected by more than one edge.

- **Weighted Graphs**: These are graphs in which each edge is assigned a numerical value or weight.

- **Trees**: These are a type of graph that has no cycles and is completely connected.

- **Planar Graphs**: These are graphs that can be embedded in the plane, i.e., they can be drawn on the plane in such a way that its edges intersect only at their endpoints.

- **Hypergraphs**: In these graphs, an edge can connect any number of nodes, not just two.

- **Complete graphs**: Graph where every node is directly connected to every other node. We can calculate the number of edges from the number of nodes as $\mathbf{m = \frac{n(n-1)}{2}}$.

- **Isomorphic graphs**: In graph theory, two graphs are said to be isomorphic if there is a one-to-one correspondence between their vertices and edges that preserves the connectivity of the graphs. In other words, two graphs are isomorphic if they have the same structure, but possibly different labels and/or different arrangements in the plane. (There has to be bijective function $f$ from the verticies of $G1$ to $G2$).

- **Cliques**: A clique in a graph is a subset of vertices such that every two distinct vertices in the clique are adjacent. In other words, a clique is a complete subgraph of the original graph. This means that every node in the clique is connected to every other node in the clique.


<h3>Types of networks</h3>

- **Social Networks**: Nodes represent people or animals, and links represent interactions. Examples include Facebook, offline and online social networks, affiliation networks, and author/actor collaboration networks.

- **Information Networks**: Nodes represent information sources, and links represent information flow. Examples include the Web, Twitter, citation networks, communication networks, and peer-to-peer networks.

- **Technological Networks**: These are human-made infrastructures with technological constraints. Examples include the Internet, telephone networks, transportation networks, power grids, and software networks.

- **Biological Networks**: These represent interactions between genes, cells, neurons in living beings. Examples include gene regulatory networks, metabolic networks, protein interaction networks, and neural networks.

- Other types of networks include ecological networks, lexical networks, financial networks, sports networks, etc.

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


<h3>Generative models</h3>

<i>(Reasoning network evolution).</i>

Generative models in graphs are algorithms or methods that are used to generate synthetic networks that resemble real-world networks. These models are designed to capture the underlying patterns or structures in the data, and they can be used to create new data that has similar statistical properties to the original data.

- **Forest fire**: This model generates graphs that have a heavy-tailed distribution of in-degrees, out-degrees, and sizes of connected components, which is a common property of many real-world networks. The model starts with a single node and grows the graph by randomly "burning" edges, which is analogous to the spread of a forest fire.

- **Author dynamics**: This model is used to generate co-authorship networks. It assumes that authors are more likely to collaborate with others who have a similar number of previous collaborations. The model starts with a small number of authors and grows the network by adding new authors and collaborations over time.

- **Citation model**: This model is used to generate citation networks, where nodes represent papers and edges represent citations. The model assumes that papers are more likely to cite other papers that have a high number of previous citations. The network grows by adding new papers and citations over time.

- **Butterfly**: This model generates graphs that have a high clustering coefficient and a small average shortest path length, similar to many real-world networks. The model starts with a small number of nodes and grows the network by adding new nodes and edges in a way that maintains the "butterfly" structure.

<h3>Random graphs</h3>

<i>(Reasoning network structure).</i>

**Erdos-Renyi Model**: This is one of the simplest random graph generation models. In the G(n, p) model, a graph is constructed by connecting nodes randomly. Each edge is included in the graph with probability p independent from every other edge. A large "giant" component emarges when $\langle k \rangle = 1$. Random graphs substantially underestimate $\langle C \rangle$.

- **Subcritical**: $n_S \sim \ln n$
- **Critical Point**: $n_S \sim n^{2/3}$
- **Supercritical**: $n_S \sim n \frac{\langle k \rangle -1}{n-1}$
- **Fully Connected**: $n_S \approx n$

**Watts-Strogatz Model**: This model generates small-world networks which exhibit properties of high clustering coefficient and small shortest path length. It starts with a regular lattice where each node is connected to k nearest neighbors and then rewires the edges randomly with a probability p. Friendship paradox: $\langle neighbor(k) \rangle > \langle k \rangle$. 

| Network | n | $\langle C \rangle$ | $\frac{(\langle k^2 \rangle - \langle k \rangle)^2}{n \times \langle k \rangle ^ 3}$ | $\frac{\langle k \rangle}{n - 1}$ |
|---------|---|-----|-------------|-------------------|
| Southern women | 32 | 0.000 | 0.204 | 0.179 |
| Karate club | 34 | 0.571 | 0.294 | 0.139 |
| American football | 115 | 0.403 | 0.078 | 0.094 |
| Java dependencies | 1368 | 0.497 | 0.879 | 0.012 |
| Facebook circles | 4039 | 0.606 | 0.063 | 0.011 |
| Physics collaboration | 36458 | 0.657 | 0.002 | 0.000 |
| Enron e-mails | 36692 | 0.497 | 0.106 | 0.001 |
| Internet map | 75885 | 0.160 | 2.985 | 0.000 |
| Actors collaboration | 382219 | 0.780 | 0.006 | 0.000 |
| Physics citation | 438943 | 0.227 | 0.001 | 0.000 |
| Patent citation | 3774768 | 0.076 | 0.000 | 0.000 |
| Facebook snowball | 8217272 | 0.019 | 0.001 | 0.000 |

- **Rand. net. Poisson dist.**: $p_k = \frac{{\langle k \rangle^k e^{-\langle k \rangle}}}{{k!}}$
- **Real net. Power-law Degree dist.**: $p_k \sim k^{-\gamma}$
- **Probability of a link**: $p_{ij} = (ki \times kj) / 2m$

**Stochastic Block Model**: This model generates graphs with community structure. Nodes are divided into groups or "blocks", and the probability of an edge existing between two nodes depends on the blocks that those nodes belong to.

**Price Model**: Also known as the preferential attachment model, it is a model for generating networks with scale-free properties. New nodes are added to the graph one at a time, and each new node is connected to existing nodes with a probability proportional to their degree.

<b>Preferential attachment</B> is a principle often used to describe a process in which some quantity, such as wealth or the number of links in a network, is distributed among a number of individuals or nodes.

In the context of network theory, preferential attachment refers to the likelihood that a new link of a network connects to a node with a degree that is already large. In other words, nodes with more connections have a higher probability of gaining even more, leading to the "rich get richer" phenomenon.

This principle is used in the Barabási–Albert (BA) model, a model that generates random scale-free networks using a preferential attachment mechanism. The BA model simulates the growth of a network by attaching new nodes to existing nodes with a probability proportional to their degree, resulting in a power-law degree distribution, a common property of scale-free networks.


<h3>Network properties</h3>

**Regular Lattices**: These are networks where each node is connected to its nearest neighbors, forming a regular structure (like a grid). In these networks:
- High Clustering: $\langle C_i \rangle \gg 0$
- Long Distances: $\langle d_i \rangle \approx n^{1/D}$

**Random Graphs**: These are networks where each pair of nodes is connected with a certain probability. In these networks:
- Low Clustering: $\langle C_i \rangle = \frac{\langle k_i \rangle}{n-1}$
- Short Distances: $\langle d_i \rangle \approx \frac{\ln n}{\ln \langle k_i \rangle}$

**Real Small-World Networks**: These are networks that exhibit both high local clustering and short global separation. In these networks:
- High Clustering: $\langle C \rangle \gg 0$
- Short Distances: $\langle d_i \rangle \approx \frac{\ln n}{\ln \langle k_i \rangle}$

**Small-World Networks**: These are a type of graph where most nodes are not neighbors of one another, but the neighbors of any given node are likely to be neighbors of each other, and most nodes can be reached from every other node by a small number of hops or steps. In other words, small-world networks have high clustering coefficient and small average path length. The Watts-Strogatz model is a famous model for generating small-world networks.

**Scale-Free Networks**: These are networks whose degree distribution follows a power law, at least asymptotically. That is, the fraction P(k) of nodes in the network having k connections to other nodes goes for large values of k as $P(k) \sim k^{-\gamma}$. In these networks, some nodes (called "hubs") have a significantly higher degree than others. The Barabasi-Albert model is a well-known model for generating scale-free networks.

| Network | n | $\langle C \rangle$ | $\frac{\langle k \rangle}{n-1}$ | $\langle d \rangle$ | $\frac{\ln n}{\ln \langle k \rangle }$ |
|---------|---|-----|-----------|-----|-------------|
| Southern women | 32 | 0.000 | 0.179 | 2.31 | 2.02 |
| Karate club | 34 | 0.571 | 0.139 | 2.41 | 2.31 |
| American football | 115 | 0.403 | 0.094 | 2.51 | 2.00 |
| Java dependencies | 1368 | 0.497 | 0.012 | 2.21 | 2.59 |
| Facebook circles | 4039 | 0.606 | 0.011 | 3.69 | 2.20 |
| Physics collaboration | 36458 | 0.657 | 0.000 | 5.50 | 4.68 |
| Enron e-mails | 36692 | 0.497 | 0.001 | 3.39 | 3.51 |
| Internet map | 75885 | 0.160 | 0.000 | 5.83 | 5.01 |
| Actors collaboration | 382219 | 0.780 | 0.000 | ≈ 3.6 | 2.94 |
| Physics citation | 438943 | 0.227 | 0.000 | ≈ 5.0 | 4.23 |
| Patent citation | 3774768 | 0.076 | 0.000 | ≈ 8.1 | 6.98 |
| Facebook snowball | 8217272 | 0.019 | 0.000 | ≈ 6.8 | 14.23 |

**Gamma Values**: The gamma value is the exponent in the power-law degree distribution P(k) ~ k^(-gamma) of scale-free networks.

For scale-free networks, the gamma value is typically between 2 and 3. This means that there are a few nodes with a very high degree and many nodes with a low degree.

For small-world networks, the concept of gamma is not typically used, as their degree distribution does not follow a power law. Instead, they are characterized by a high clustering coefficient and a small average path length.


<h3>Community detection</h3>

Most social networks and information networks contain communities. Many biological networks contain communities.Technological networks rarely contain communities. Random graphs lack community structure.

- Removal of local bridge $\{i, j\}$ causes $d_{ij} > 2$
- Removal of bridge $\{i, j\}$ causes $d_{ij} = \infty$
- Embedded tie $\{i, j\}$ has $C_{ij} > 0$
- A **clique** is a complete subgraph of some graph. This also includes k-plexes, k-cores, k-cliques, k-clubs, k-clans.
- A **community** is a dense subgraph of a sparse network.
- **Community detection** is essentially graph partitioning.

<b>Modularity</b>

Modularity is a measure in network science that quantifies the strength of division of a network into communities (also called modules or clusters). It was designed to measure the strength of partitioning of a network into communities, but it can also be viewed as a measure of the community structure found in the network.

<hr/>

Modularity is a measure that quantifies the strength of division in a network into communities or clusters. It is based on a null model represented by the configuration model, a type of random graph that maintains the same degree distribution as the original network. This model is used to simulate a scenario where the network's edges are distributed randomly, while still preserving the degree of each node.

If a different graph model is used as the null model, the interpretation of the modularity measure would be altered. The modularity would then represent the degree to which the actual network deviates from this alternative null model in terms of its community structure.

For instance, if the null model is a lattice graph, a high modularity would suggest that the actual network has a more pronounced community structure than a lattice. Conversely, if the null model is a scale-free network, a high modularity would imply that the actual network exhibits a stronger community structure than a scale-free network.

In essence, the modularity measure is based on a comparison between the actual network and a null model, which is typically represented by the configuration model. A high modularity indicates that the network's community structure is stronger than what would be expected if the edges were distributed randomly while maintaining the degree of each node.

<hr/>

$$Q = \frac{1}{2m} \sum_{ij} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)$$

- modularity $Q \gg 0$ also in random graphs
- modularity $Q$ has resolution limit at $k_c \leq
\sqrt{2m}$
- modularity $Q$ lacks clear optimum in real networks.

<b>Partitioning bisection</b>

Partitioning bisection is a method used in graph theory to divide a graph into two subgraphs (or partitions) of equal size. The goal is to minimize the number of edges that are cut, i.e., the number of edges that have one endpoint in each partition.

This problem is known to be NP-hard, meaning that there is no known efficient algorithm to solve it exactly for all graphs. However, there are several heuristic algorithms that can find good (but not necessarily optimal) solutions in a reasonable amount of time. These include the Kernighan–Lin algorithm, the Fiduccia-Mattheyses algorithm, and spectral partitioning methods.

**Kernighan-Lin**: This is a heuristic algorithm used for partitioning a graph into two equal-sized sets while minimizing the cut size (the number of edges between the two sets). It works by iteratively swapping pairs of nodes to improve the cut size. It's a local search method, meaning it starts with an initial solution and tries to improve it through local changes.

**Fiedler graph bisection**: This is a spectral method for graph partitioning. It uses the eigenvector corresponding to the second smallest eigenvalue of the Laplacian matrix of the graph (known as the Fiedler vector) to partition the graph. Nodes are sorted based on their values in the Fiedler vector, and the graph is split at the point that minimizes the cut size. This method can reveal global properties of the graph and is often used as a preprocessing step for other algorithms.

**Standard equivalence blockmodeling**: This is a method used in social network analysis to identify roles and positions in a network. It works by partitioning the nodes into blocks such that nodes in the same block are structurally equivalent, meaning they have identical patterns of connections to other nodes. The goal is to simplify the network into a blockmodel, which is a smaller graph that preserves the essential structure of the original network. This method is more focused on the structure of the network and the roles of nodes, rather than simply dividing the network into parts.

<hr/>

**Louvain Method**: The Louvain method is a greedy optimization method that attempts to optimize the "modularity" of a partition of the network. Modularity is a scalar value between -1 and 1 that measures the density of links inside communities as compared to links between communities. The higher the modularity, the better the partition.

**Girvan-Newman Algorithm**: This algorithm detects communities by progressively removing edges from the original graph. The algorithm removes the "most valuable" edge, traditionally the edge with the highest betweenness centrality, at each step. As the graph breaks down into pieces, the tightly knit community structure is exposed.

**Infomap**: Infomap is based on the idea that information flows through a network and often gets stuck in densely connected parts of the network, i.e., communities. The algorithm uses the probability flow of random walks as a proxy for information flows in the real system and decomposes the network into modules that minimize the expected description length of a random walker's movements on the network.

**Label Propagation Algorithm (LPA)**: The algorithm doesn’t require a priori information about the number of clusters and can unveil hierarchies of communities, where each node is assigned a unique label and at every step each node adopts the label that most of its neighbors currently have. In this iterative procedure, densely connected groups of nodes form a consensus on a unique label to form communities.

**Ravasz Hierarchical Clustering**: This is a method used for detecting hierarchical structure in networks. It's based on the idea of "hierarchical modularity", a property of many complex networks where nodes form tightly knit groups that are hierarchically organized. The method works by iteratively grouping nodes into modules based on their connections, and then treating each module as a single node in the next level of the hierarchy. This process is repeated until all nodes are grouped into a single module at the top of the hierarchy. The result is a dendrogram that shows the hierarchical organization of the nodes.

**Leiden Modularity Optimization**: This is a method used for community detection in networks. It's an improvement over the Louvain method, which is a popular method for optimizing modularity. The Leiden method also optimizes modularity, but it includes an additional refinement phase that improves the quality of the detected communities. The method works by iteratively assigning nodes to communities in a way that maximizes the gain in modularity, and then refining the communities to ensure that each node is in the community where it contributes most to modularity. The process is repeated until no further improvement can be made. The Leiden method is known for its high quality results and its ability to detect communities in large networks.

<hr/>

<b>Measures</b>

**Normalized Mutual Information (NMI)**: This is a measure used to compare the similarity of two clusterings. The formula for NMI is:

$$NMI(X, Y) = \frac{2 * I(X; Y)}{H(X) + H(Y)}$$

where I(X; Y) is the mutual information between X and Y, and H(X) and H(Y) are the entropies of X and Y, respectively. The range of NMI is [0, 1]. A value of 0 indicates that the two clusterings are completely independent, while a value of 1 indicates that they are identical. Therefore, a larger value is better.

**Normalized Variation of Information (NVI)**: 
The Normalized Variation of Information (NVI) is a measure of the dissimilarity between two clusterings. It is defined as the Variation of Information (VI) between the two clusterings, divided by the logarithm of the total number of elements (n).

The Variation of Information is defined as the sum of the conditional entropies of the two clusterings, which measures the amount of information lost when changing from one clustering to the other.

$$NVI(C, D) = \frac{VI(C, D)}{log(n)} = \frac{H(C|D) + H(D|C)}{log(n)}$$

- $C$ and $D$ are the two clusterings
- $VI(C, D)$ is the Variation of Information between $C$ and $D$
- $H(C|D)$ is the conditional entropy of $C$ given $D$
- $H(D|C)$ is the conditional entropy of $D$ given $C$
- $log(n)$ is the logarithm of the total number of elements

The range of NVI is [0, log(n)]. A value of 0 indicates that the two clusterings are identical, while a value of log(n) indicates that they are completely dissimilar. Therefore, a smaller value is better.

<h3>Node importance</h3>

Centrality measures for (un)directed networks
- clustering coefficients
- geodesic-based measures (closeness centrality, betweenness centrality)
- spectral analysis measures
- fragment-based measures

<hr/>

1. **Degree Centrality**: This is the simplest measure of node centrality. It is calculated as the number of edges connected to a node. In directed networks, you can further distinguish between in-degree and out-degree centrality.
$$C_D(v) = \frac{\text{deg}(v)}{n-1}$$

2. **Closeness Centrality**: This measure calculates the average length of the shortest path from a node to all other nodes in the network. Nodes with lower average shortest paths have higher closeness centrality.
$$C_C(i) = \frac{1}{\frac{1}{n-1} \sum_{j \neq i} d_{ij}}$$
$d_{ij}$ is the distance between node i and j.


3. **Betweenness Centrality**: This measure calculates the number of shortest paths from all nodes to all others that pass through a particular node. Nodes that occur on many shortest paths have higher betweenness centrality. The sum is the fraction of shortest paths that go through the current node.

$$C_B(i) = \frac{1}{n^2} \sum_{s \neq t} \frac{g_{st}^{\lq i}}{g_{st}}$$

4. **Eigenvector Centrality**: This measure assigns relative scores to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes.
$$e_i = \frac{1}{\lambda} \sum_{j} A_{ij} e_j$$

5. **PageRank**: This is a variant of Eigenvector Centrality, used by Google to rank websites in their search engine results. It measures the importance of each node within the network.
$$p_i = \alpha + \sum_j (A_{ij} \frac{p_j}{k_j^{out}}) + \beta_i$$,
for convenience $\beta_i = \frac{1 - \alpha}{n}$ (teleportation probability) and $\alpha = 0.85$ (damping factor). $k_j^{out}$ is the out-degree of node $j$, which is the number of links going out from the node. $p_j$ is the <b>PageRank</b> of node $j$. The nature of PageRank is thus recursive and is calculate iteratively slowly adjusting the PageRank of every node.
\
In this formula, d is the damping factor, which represents the probability of continuing the random walk to a randomly chosen neighbor. $1 - d$ is the probability of "jumping" back to the restart node. The restart node is represented by $β_i$, which is a vector where all elements are 0 except for the element corresponding to the restart node, which is 1. $A_{ij}$ is the adjacency matrix of the graph, p_j is the PageRank of node j, and $k_j^{out}$ is the out-degree of node j.
$$p_i = (1 - d) \cdot \beta_i + d \cdot \sum_j (A_{ij} \frac{p_j}{k_j^{out}})$$
6. **Katz Centrality**: This measure assigns relative scores to all nodes in the network based on the sum of the number of walks of different lengths, with shorter walks contributing more than longer ones. It is similar to Eigenvector Centrality but it also considers the shorter paths.
$$k_i = \alpha \sum_{j} A_{ij} k_j + \beta$$
where:
    - $k_i$ is the Katz centrality of node $i$.
    - $\alpha$ is a factor that determines the influence of longer walks (it should be less than the reciprocal of the largest eigenvalue of the adjacency matrix for the series to converge) $a \lt \lambda_1^{-1}$ (leading eigenvalue of $A$).
    - $A_{ij}$ is the element at the $i$-th row and $j$-th column of the adjacency matrix $A$.
    - $k_j$ is the Katz centrality of node $j$.
    - $\beta$ is a constant representing an initial centrality ($\beta = 1).

<hr/>

7. **Clustering Coefficient (C)**: This measure gives an indication of the degree to which nodes in a graph tend to cluster together. Evidence suggests that in most real-world networks, and in particular social networks, nodes tend to create tightly knit groups characterized by a relatively high density of ties.

   $$C_i = \frac{2t_i}{k_i(k_i-1)}$$

   where:
   - $C_i$ is the clustering coefficient of node $i$.
   - $t_i$ is the number of triangles connected to node $i$.
   - $k_i$ is the degree of node $i$.
   - $C_i = 0$ for $k_i \leq 1$.

8. **ω-corrected Clustering Coefficient (Cω)**: This is a variant of the clustering coefficient that takes into account the maximum possible number of triangles with respect to the degree distribution.

   $$C_{\omega i} = \frac{t_i}{\omega_i}$$

   where:
   - $C_{\omega i}$ is the ω-corrected clustering coefficient of node $i$.
   - $t_i$ is the number of triangles connected to node $i$.
   - $\omega_i$ is the maximum possible number of triangles with respect to the degree distribution.
   - $C_{\omega i} = 0$ for $\omega_i = 0$.

9. **µ-corrected Clustering Coefficient (Cµ)**: This is another variant of the clustering coefficient that takes into account the maximum number of triangles over links.

   $$C_{\mu i} = \frac{2t_i}{k_i\mu}$$

   where:
   - $C_{\mu i}$ is the µ-corrected clustering coefficient of node $i$.
   - $t_i$ is the number of triangles connected to node $i$.
   - $k_i$ is the degree of node $i$.
   - $\mu$ is the maximum number of triangles over links.
   - $C_{\mu i} = 0$ for $k_i = 0$. 

<h3>Edge importance</h3>

1. **Edge Betweenness**: This is a measure of centrality and is defined as the number of shortest paths between pairs of nodes that run along it. If an edge has high betweenness then it controls a high amount of flow between nodes.

$$\sigma_{ij} = \sum_{st \notin \{i, j\}} \frac{g_{st}^{ij}}{g_{st}}$$

2. **PageRank**: This is a ranking algorithm originally used by Google to determine the importance of web pages, based on their incoming links. It can be thought of as a measure of the probability that a random surfer (who randomly clicks on links) will land on a particular page. It's also used in various types of network analysis to measure node importance.

    The PageRank rank \(p\) for node \(i\) in a directed graph \(G\) is defined as follows:

    $$
    p_i = \alpha \sum_j \frac{A_{ij} p_j}{k_{out_j}} + \frac{1 - \alpha}{n}
    $$

    Where:
    - \(\alpha\) is a positive constant, traditionally set to 0.85.
    - \(A_{ij}\) is the adjacency matrix of the graph, indicating whether there is a link from node \(j\) to node \(i\).
    - \(p_j\) is the PageRank of node \(j\).
    - \(k_{out_j}\) is the out-degree of node \(j\), or the number of links going out from node \(j\).
    - \(n\) is the total number of nodes in the graph.

    In this formula, \(p_i\) represents the probability that a random surfer with teleports lands on node \(i\). The teleporting mechanism (represented by the \(\frac{1 - \alpha}{n}\) term) prevents the random walk from getting stuck in loops or dead ends by allowing the surfer to jump to a random node with a small probability.

3. **Random Walk Accessibility**: This measure is based on the idea of a random walker traversing the network and uses the probability of reaching each node from a given starting node in a certain number of steps. In the context of a directed graph G, the random walk rank w for node t of node i is defined as follows:

    $$
    w_i = \alpha \sum_j \frac{A_{ij} w_j}{k_{out_j}} + (1 - \alpha)\delta_{it}
    $$

    Where:
    - \(\alpha\) is a positive constant, traditionally set to 0.85.
    - \(A_{ij}\) is the adjacency matrix of the graph, indicating whether there is a link from node j to node i.
    - \(w_j\) is the random walk rank of node j.
    - \(k_{out_j}\) is the out-degree of node j, or the number of links going out from node j.
    - \(\delta_{it}\) is the Kronecker delta, which is 1 if i = t and 0 otherwise.

    In this formula, \(w_i\) represents the probability that a random surfer with teleport t lands on node i.


4. **Bridgeness**: This formula calculates the bridgeness of an edge {i, j} as the difference between the total number of shortest paths σ_{ij} and the sum of the ratios of the number of shortest paths through {i, j} to the total number of shortest paths, for all pairs of nodes {s, t} in the union of the neighborhoods of i and j. The second part of the formula calculates the same quantity, but for all pairs of nodes {s, t} not in the union of the neighborhoods of i and j.
\
$$
\sigma_{e_{ij}} = \sigma_{ij} - \sum_{st \in \Gamma_i \cup \Gamma_j} \frac{g_{ij}^{st}}{g_{st}} = \sum_{st \notin \Gamma_i \cup \Gamma_j} \frac{g_{ij}^{st}}{g_{st}}
$$
\
Gammas represent the neighborhoods of both nodes.

5. **Embeddedness**:
Bridging Embeddedness is a measure used in network analysis to quantify how much a link (or edge) between two nodes is embedded within the network. It's particularly useful for understanding the importance of a link in the context of the overall network structure.
\
The formula for calculating the Bridging Embeddedness (θ) of a link {i, j} in an undirected graph G is:
\
$$\theta_{ij} = \frac{|\Gamma_i \cap \Gamma_j|}{k_i - 1 + k_j - 1 - |\Gamma_i \cap \Gamma_j|} \\
\mu-corrected(\theta_{ij}) = \frac{|\Gamma_i \cap \Gamma_j|}{\mu + \max(k_i, k_j) - 1 - |\Gamma_i \cap \Gamma_j|}$$
\
where
    - $\mu$ is the maximum number of triangles over links
    - $\Gamma_i$ and $\Gamma_j$ are the neighborhoods
    - $k_i k_j$ are the degrees


<h3>Node mixing</h3>

- Node mixing = correlations between linked nodes
- In assortative mixing nodes are linked to similar others
- In disassortative mixing nodes linked to dissimilar others

<b>Effects</b>
- Degree mixing impacts connectivity and distances
- Assortative mixing coexists with community structure
- Mixing influences resilience  and controllability

The <b>assortativity degree</b> of a graph is a measure of how its nodes' degrees correlate with the degrees of their neighbors. It's a way to quantify the tendency of nodes to connect with other nodes that have similar degrees.

- A positive assortativity degree means that nodes tend to connect with other nodes of similar degree. This is known as assortative mixing. For example, in a social network, this might mean that people with many friends tend to be friends with other people who have many friends.

- A negative assortativity degree means that nodes tend to connect with nodes of dissimilar degree. This is known as disassortative mixing. For example, in an ecological network, this might mean that predators (which have few connections) tend to prey on species that are preyed upon by many other species (which have many connections)


<h3>Block modeling</h3>

Blockmodeling is a method used in network analysis to simplify the structure of a network by grouping together nodes that have similar connection patterns. The goal is to represent the network as a smaller graph, known as a blockmodel, which preserves the essential structure of the original network.

$$r = \frac{\frac{1}{m}\sum_{ij}(A_{ij}k_{i}k_{j}) - \left[\frac{1}{2m}\sum_{ij}(A_{ij}(k_{i}+k_{j}))\right]^2}{\frac{1}{2m}\sum_{ij}(A_{ij}(k_{i}^2+k_{j}^2)) - \left[\frac{1}{2m}\sum_{ij}(A_{ij}(k_{i}+k_{j}))\right]^2}$$

Here are various models used for generating or representing networks:

- **Random Graph Model G(n, m)**: This model generates a random graph with `n` nodes and `m` links. Each pair of nodes is connected by an edge with equal probability, independent of the other edges.

  1. Start with n isolated nodes.
  2. Randomly select two nodes and add an edge between them, repeat this m times.

- **Configuration Model G({k})**: This model generates a random graph with a given degree sequence `{k}`. Each node `i` has `k_i` stubs (half-edges), and pairs of stubs are randomly connected to form edges.
  1. Start with n isolated nodes, where n is the length of the degree sequence {k}.
  2. Assign to each node i a number of "stubs" (half-edges) equal to k_i.
  3. Randomly select two stubs and connect them to form an edge, repeat until all stubs are connected.

- **Exponential p\*-model** $\mathbf{G(n, {\langle x \rangle})}$: This model generates a random graph with `n` nodes and expected values $\langle xi \rangle$. The probability of each possible graph is proportional to the exponential of a graph statistic (such as the number of edges or triangles) multiplied by a parameter.
  1. Start with n isolated nodes.
  2. For each possible edge, calculate the probability of its existence based on the exponential of a graph statistic multiplied by a parameter.
  3. Add the edge to the graph with the calculated probability.

- **Stochastic Block Model G({C})**: This model generates a random graph with node clusters `{C}`. Each node belongs to one cluster, and edges between nodes are generated with probabilities that depend on their clusters.
  1. Partition the set of n nodes into clusters {C}.
  2. For each pair of nodes, calculate the probability of an edge between them based on their cluster memberships.
  3. Add the edge to the graph with the calculated probability.

- **Hierarchical Model G(H)**: This model generates a random graph with a given node hierarchy `H`. The hierarchy is a tree structure, and edges between nodes are more likely if their lowest common ancestor in the hierarchy is closer to them.
  1. Assign each of the n nodes to a position in the hierarchy H.
  2. For each pair of nodes, calculate the probability of an edge between them based on their positions in the hierarchy.
  3. Add the edge to the graph with the calculated probability.


<h3>Core preiphery</h3>

A core-periphery structure in network analysis divides the network into a densely connected "core" and a less connected "periphery". The core nodes have many interactions, while periphery nodes are less central and typically connect to the core. This structure, often seen in social networks, suggests an underlying structure rather than randomness.

- <b>Core/periphery</b> nodes have <b>higher/lower</b> degrees `k`
- <b>Core/periphery</b> nodes are on <b>shorter/longer</b> distances
- <b>Core/periphery</b> nodes have <b>higher/lower</b> clustering `C`

<hr/>

- k-cores are subgraphs of nodes with $\geq k$ neighbors <small>Remove nodes with degree < k until no such node remains</small>
- k-shells are nodes of k-cores that are not in k + 1-cores
- k-cores are nested while k-shells form decomposition
- Holme’s k∗-core maximizes closeness centrality $l^{(-1)}$

The core-periphery coefficient quantifies a network's core-periphery structure, where the "core" nodes are densely connected and "periphery" nodes are less so. It's calculated by assigning each node a "coreness" score (often between 0 and 1), then aggregating these scores. Higher coefficients indicate a stronger core-periphery structure. The specifics can vary based on the network and context.

<h3>Subgraphs / fragments</h3>

Small graphs are building blocks of networks and characterize local network structure.

- <b>Fragments</b>: Fragments are connected subgraphs of a larger network. They are a subset of nodes and the edges between them that form a connected structure. For example, in a social network, a fragment could represent a group of friends who are all connected to each other.


- <b>Motifs</b>: Motifs are recurring and statistically significant patterns of non-induced subgraphs in a network. They represent common local connection patterns between nodes. For instance, in a biological network, a motif might represent a common pattern of interactions between proteins. It has a very low probability of appearing in random graph ($ \lt 0.01$). 
\
Motif significance has a normal distribution $N(0, 1)$. $n_i$ is the number of motifs i in a real network. And $\lq n_i$ - the number of motifs in a random network (with variance $\lq \sigma_{i}$).
$$Z_i = \frac{n_i - \langle \lq n_i \rangle }{\lq \sigma_{i}} \\
n_i - \langle \lq n_i \rangle \gt 0.1 \times \langle \lq n_i \rangle
$$
We also have have motif significance profile $\mathbf{SP}$, which is defined as $SP_i = Z_i / \sqrt{\sum_i {Z_i}^2}$. 
\
And there is also an abundance/ratio profile, defined as $A_i$ is the abundance of motif $i$ in a real network. $RP_i = A_i / \sqrt{\sum_i {A_i}^2}$, where $A_i$ is $(n_i - \langle \lq n_i \rangle) / (n_i + \langle \lq n_i \rangle + \epsilon_i)$
 

- <b>Graphlets</b>: Graphlets are specific induced subgraphs, meaning they include all the edges that exist between the selected nodes in the larger network. They are often used in network analysis to capture and compare local network topology. For example, in a citation network, a graphlet could represent a specific pattern of citations between a group of papers.
\
In other words, if you select a set of nodes from a graph to form a graphlet, you must also include any edge from the original graph that connects two nodes in this set. This can result in a variety of different structures, depending on the connections between the selected nodes in the original graph.
\
Relative graphlet frequency F is defined as $F_i = n_i / \sum_i n_i$, this measures the number of occurances of a specific graphlet compared to other types.
\
Graphlets are small subgraphs of a larger network, and orbits are essentially the roles that nodes can play within a graphlet. For example, in a triangle graphlet, each node has the same role, so there is only one orbit. But in a star-shaped graphlet with four nodes, the center node has a different role than the three peripheral nodes, so there are two orbits. The i-th orbit graphlet degree distribution gives the degree distribution for node.
    - $p_k^i$ is graphlet degree distribution for i-th orbit
    - $p_k^{\lq i}$ is a scaled graphlet degree distribution for i-th orbit, which is defined as  $p_k^{\lq i} = p_k^i / k$.
    - i-th orbit graphlet agreement $A_i$ is defined as $$A_i = 1 - \sqrt{\frac{1}{2} \sum_k (\log q_k^{\lq i} - \log p_k^{\lq i})^2}$$, where p and q are two networks.
    -  arithmetic/geometric graphlet agreeement $A$ is defind as $$A = \frac{1}{73} \sum_i A_i \\ 
        A = (\prod_i A_i)^{\frac{1}{73}}
    $$

<h3>Sampling</h3>

Network sampling is a crucial aspect of network analysis, especially when dealing with large or hidden populations. It involves selecting a subset of individuals from a network to infer properties of the entire network.

One common method of network sampling is <b>snowball sampling</b>, often used in sociology. This method involves starting with a small, initial group of individuals and then expanding the sample by including their contacts. This process continues, with the sample 'snowballing' as more and more contacts are included. This method is particularly useful when studying hidden or hard-to-reach populations.

Another method is <b>contact tracing</b>, which is similar to snowball sampling but focuses on tracking and studying the contacts of individuals within a network. This method is often used in epidemiology to understand the spread of diseases.

Network sampling also involves understanding the properties of the network, such as its fractality and self-similarity. A fractal network is one where a part of the network is similar to the whole, a property that can help in understanding the network's structure and behavior. Self-similarity, on the other hand, requires the network to exhibit power-law size scaling under renormalization, a property often observed in real-world networks.

It's important to note that any real network we observe and analyze is just a sample of the true, underlying network. This underscores the importance of effective sampling methods in accurately capturing the properties of the network.

</hr>

- **Snowball Sampling** is similar to a breadth-first search. In this method, nodes are sampled proportional to their eigenvector centrality. 

- **Contact Tracing** is similar to a biased best-first search. In this method, nodes are sampled according to some hidden variable.

- **Respondent-Driven Sampling** is similar to a random walk. In this method, nodes are sampled proportional to their degree.

The average of a property $x_i$ over the sampled nodes can be estimated as:

$$
\hat{x} = \frac{\sum_i x_i}{n}
$$

However, this estimate can be biased if the probability of sampling each node is proportional to some property of the node. To correct for this bias, we can use the following estimate:

$$
\hat{x}_{\text{corrected}} = \frac{\sum_i \frac{x_i}{k_i}}{\sum_i \frac{1}{k_i}}
$$

</hr>

<h5>Sampling methods</h5>

- **Random Selection Methods for Global Network Sparsification**
  - Random node/link selection with or without induction

- **Network Exploration Methods for Local Network Sampling**
  - Random walks
  - Snowball sampling
  - Expansion sampling

- **Merging/Aggregation Methods for Network Simplification**
  - Box covering
  - Cluster growing
  - Community aggregation


<h3>Backbones & Skeletons</h3>

- **Network Backbone**: A technique that retains the most significant links in a network by removing less important ones. It's useful in large networks to focus on the most influential connections.

- **Network Skeleton**: Aims to preserve the network's structure at all scales. Unlike the backbone, it tries to retain as many links as possible, preserving the structure from individual nodes to the entire network. This method is useful when the goal is to preserve the overall structure and characteristics of the network at different scales, from individual nodes (micro) to communities (meso) and the entire network (macro).

    - Betweenness/Salience Skeletons: Based on betweenness centrality, it identifies and retains the most important edges in the network, forming a simplified representation of the network's structure.

    - Convex Skeleton: The largest subgraph that includes the most influential nodes and all nodes on the shortest paths between them. It forms a 'convex hull' in the network space (tree of cliques, each subraph is convex).

    - Large-Scale Statistics: Involves studying the properties and characteristics of the network skeleton across many nodes and edges, providing insights into the overall structure and behavior of the network.

    - Node Distributions: Refers to the statistical distribution of nodes within the network skeleton, providing insights into its structure and characteristics, such as heterogeneity, connectivity, and robustness.

    - Node Centralities: Measures of a node's importance within the network skeleton, providing insights into which nodes are most influential or critical to the network's structure and function.

<hr/>

- **Communities in Skeletons**: Groups of densely connected nodes in the network skeleton, representing functional or structural units. Analyzing these can provide insights into the modular structure of the network.

- **Robustness of Skeletons**: The skeleton's ability to maintain its structure and function when faced with perturbations. Analyzing the robustness can provide insights into the network's resilience and its ability to withstand failures or attacks.


<h3>Inference</h3>

Network inference refers to the process of predicting or discovering unknown aspects of a network based on known information. This can involve inferring missing, spurious, or hidden nodes and links that may be due to sampling errors, noise, or other factors. The goal is to reconstruct the true network structure or dynamics as accurately as possible. Network inference can be used in various applications, such as:

- **Predicting Future Links**: One popular application of network inference is predicting future links that are likely to occur. This can be used, for example, to recommend potential friendship ties on social networks like Facebook, based on the existing network of connections.

- **Predicting Product Ratings**: Network inference can also be used to predict product ratings on platforms like Amazon. This can be based on the network of users and their past ratings, using techniques such as collaborative filtering.

- **Predicting Protein Interactions**: In bioinformatics, network inference can be used to predict interactions between proteins. This can be particularly useful when experimental determination of these interactions is costly or difficult.

<hr/>

<h4>Link prediction</h4>

- **Link Prediction by Local Structure/Dynamics**: For example, if two users on a social network have many mutual friends (a local structure), they are likely to become friends in the future.

- **Link Prediction by Global Structure/Dynamics**: For instance, in a citation network, if two papers are often cited together by other papers (a global structure), it's likely that there is a direct citation link between them.

- **Link Prediction by Maximum Likelihood Methods**: For example, in a protein-protein interaction network, a hierarchical block model might predict that proteins within the same functional group are more likely to interact.

- **Link Prediction by Probabilistic Inference Methods**: For instance, a probabilistic relational model might predict future collaborations between researchers based on their past collaborations and their areas of expertise.

<hr/>

<h4>Prediction equivalence</h4>

- **Common Neighbors Index**: This method predicts links between two nodes (i and j) based on the number of common neighbors they have.

- **Jaccard Neighbors Index**: This method predicts links between two nodes (i and j) based on the similarity of their neighbor sets. It's calculated as the size of the intersection divided by the size of the union of the two sets.

- **Salton Cosine Similarity**: This method predicts links between two nodes (i and j) based on the cosine of the angle between their adjacency vectors. It's a measure of orientation and not magnitude.

- **Leicht Similarity Index**: This method predicts links between two nodes (i and j) based on the ratio of their common neighbors to the product of their degrees. 


<hr/>

<h4>Prediction overlap</h4>

- **Sørensen Neighbors Index**: This method predicts links between two nodes (i and j) based on the size of the intersection of their neighbor sets, normalized by the average degree of the two nodes.

- **Hub Promoted Index**: This method predicts links between two nodes (i and j) based on the size of the intersection of their neighbor sets, normalized by the degree of the node with fewer connections (the "hub").

- **Hub Depressed Index**: This method predicts links between two nodes (i and j) based on the size of the intersection of their neighbor sets, normalized by the degree of the node with more connections.

<hr/>

<h4>Prediction models</h4>

- **Configuration Model Index**: This method predicts links between two nodes (i and j) based on the ratio of their common neighbors to the product of their degrees, normalized by the total number of nodes. It's a model that generates a random graph with a given degree sequence.

- **Preferential Attachment Index**: This method predicts links between two nodes (i and j) based on the product of their degrees. It's based on the principle that the more connected a node is, the more likely it is to receive new links.

- **Random Graph Index**: This method predicts links between two nodes (i and j) based on the degree of one node, normalized by the total number of nodes minus one. It's a model that generates a graph of n nodes, each pair of nodes being connected with equal probability.

<hr/>
<h4>Prediction dynamics</h4>

- **Resource Allocation Index**: This method predicts links between two nodes (i and j) based on the sum of the reciprocal of the degree of their common neighbors. It's a measure that considers the resources that can be transferred through common neighbors.

- **Adamic-Adar Similarity Index**: This method predicts links between two nodes (i and j) based on the sum of the reciprocal of the logarithm of the degree of their common neighbors. It gives more weight to uncommon features.

- **Random Walk Similarity Index**: This method predicts links between two nodes (i and j) based on the probability that a random walk starting from node i will end at node j, and vice versa. It's a measure that considers the structure of the entire network.

<hr/>
<h4>Prediction clusters</h4>

- **Community Structure Index**: This method predicts links between two nodes (i and j) based on the number of links within their community, normalized by the total possible number of links within the community, if they belong to the same community. It's a measure that considers the community structure of the network.

- **Block Model Index**: This method predicts links between two nodes (i and j) based on the number of links within their community, normalized by the total possible number of links within the community, if they belong to the same community. If they belong to different communities, it's based on the number of links between their communities, normalized by the product of the sizes of their communities. It's a measure that considers the block structure of the network.

<hr/>
<h4>Prediction framework</h4>

- **Standard Link Prediction Setting**: This framework involves three steps:
  1. Randomly sample a set of unlinked nodes.
  2. Remove a random set of node links.
  3. Compute the similarity score for the union of the unlinked nodes and the removed links on the resulting network.

- **Temporal Link Prediction Setting**: This framework involves three steps:
  1. Randomly sample a set of unlinked nodes equal to the size of the removed links.
  2. Remove node links after a certain time t.
  3. Compute the similarity score for the union of the unlinked nodes and the removed links on the network at time t.

- **Pearson/Spearman Correlation or AUC Measure**: This framework involves comparing the ideal similarity scores for the unlinked nodes and the removed links. The ideal scores for the unlinked nodes are all zeros, while the ideal scores for the removed links are all ones.

<h3>Machine learning on graphs</h3>

Machine learning on graphs is a subfield of machine learning that focuses on learning from graph data. Graphs provide a natural representation for data in many real-world applications, such as social networks, biological networks, and the World Wide Web. Machine learning tasks on graphs can be broadly categorized into node-level tasks, edge-level tasks, and graph-level tasks.

- **Node-level tasks**: These tasks involve making predictions for individual nodes in the graph. Examples include:
  - **Node classification**: This involves assigning a label to a node based on its attributes and connections. For example, identifying hoaxes on Wikipedia.
  - **Node ranking**: This involves ranking nodes based on their importance or influence in the network. For example, finding top influencers on Instagram.
  - **Network clustering**: This involves grouping similar nodes together. For example, identifying research areas of scientific papers.

- **Edge-level tasks**: These tasks involve making predictions for individual edges in the graph. Examples include:
  - **Link prediction**: This involves predicting whether a link will form between two nodes. For example, product recommendation on Amazon.
  - **Strength of ties**: This involves predicting the strength or weight of a connection between two nodes. For example, distinguishing between close friends and acquaintances on Facebook.

- **Graph-level tasks**: These tasks involve making predictions for entire graphs. Examples include:
  - **Graph classification**: This involves assigning a label to an entire graph based on its structure and the attributes of its nodes and edges. For example, identifying playing strategies in football.
  - **Graph generation**: This involves generating new graphs that resemble a given set of graphs. This can be used, for example, to generate new social networks or chemical structures.

<hr/>
<h4>Node Ranking Tasks</h4>

Node ranking tasks involve determining the importance of nodes in a graph. Techniques used include node centrality, link analysis, graphlets, and egonets.

<h4>Link Prediction Tasks</h4>

Link prediction tasks involve predicting the likelihood of a relationship between two nodes. Techniques used include link bridging, prediction indices, and matrix factorization.

<h4>Network Clustering Tasks</h4>

Network clustering tasks involve grouping similar nodes together in a graph. Techniques used include community detection and (stochastic) blockmodeling.


<h3>Network visualization</h3>

1. **Circular Layout**: This layout positions nodes in a circle. This can be useful for small graphs and is a simple way to visualize the overall structure of the network. However, it may not be as informative for larger, more complex networks as it does not take into account the relationships between nodes.

2. **Spring Layout (Fruchterman-Reingold)**: This layout is based on the Fruchterman-Reingold algorithm, which treats edges as springs holding nodes apart, and nodes as objects repelling each other. The algorithm iteratively adjusts the positions of the nodes in order to minimize the energy of the system, resulting in a visually pleasing layout that reveals the structure of the network.

3. **Kamada-Kawai Layout**: This layout is based on the Kamada-Kawai algorithm for network drawing. It is a force-directed method, similar to the Spring Layout, but it uses a different energy function. The Kamada-Kawai algorithm aims to position nodes in such a way that the geometric distance between nodes (as displayed in the layout) is as close as possible to the graph-theoretic distance (i.e., the shortest path between nodes in the graph). This often results in layouts that reflect the underlying structure of the network.


<h3>Time complexities</h3>

$m$ are edges and $n$ are nodes

| Measure/Algorithm                  | Time Complexity | Method |
|-----------------------------------|-----------------|--------|
| Clustering Coefficient            | O(n^2)          | Measures the degree to which nodes in a graph tend to cluster together. |
| Average Distance                  | O(n^3)          | Calculates the average distance between every pair of nodes in the graph. |
| Approximated Average Distance     | O(n log n)      | Approximates the average distance between nodes in a graph. |
| Diameter                          | O(n^3)          | Finds the longest shortest path between any two nodes in the graph. |
| Gamma (Transitivity)              | O(n^2)          | Measures the likelihood that the adjacent vertices of a vertex are connected. |
| Finding the Largest Connected Component | O(n + m)    | Finds the largest subgraph in which any two vertices are connected to each other. |
| Page Rank                         | O(n log n)      | Measures the importance of each node in the network, based on the structure of incoming links. |
| Betweenness Centrality            | O(n^3)          | Measures the extent to which a node lies on paths between other nodes. |
| Louvain Community Detection       | O(n log n)      | Detects communities in large networks. |
| Infomap                           | O(n log n)      | Detects community structure in complex networks. |
| Girvan-Newman                     | O(n^3)          | Detects communities by progressively removing edges from the original graph. |
| Breadth-First Search (BFS)        | O(n + m)        | Traverses the graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search when a dead end occurs in any iteration. |
| Depth-First Search (DFS)          | O(n + m)        | Traverses the graph in a depthward motion and uses a stack to remember to get the next vertex to start a search when a dead end occurs in any iteration. |
| Dijkstra's Algorithm              | O((n + m) log n)| Finds the shortest path from a node to all other nodes in the graph. |
| Bellman-Ford Algorithm            | O(n * m)        | Computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. |
| Kruskal's Algorithm               | O(m log m)      | Finds a minimum spanning forest of an undirected edge-weighted graph. |
| Floyd-Warshall Algorithm          | O(n^3)          | Finds shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles). |
| Prim's Algorithm                  | O(n^2)          | Finds a minimum spanning tree for a weighted undirected graph. |
| Edmonds-Karp Algorithm            | O(n * m^2)      | Implements the Ford-Fulkerson method for computing the maximum flow in a flow network. |
| Ford-Fulkerson Algorithm          | O(max_flow * m) | Computes the maximum flow in a flow network. |
| Johnson's Algorithm               | O(n^2 log n + n * m) | Finds the shortest paths between all pairs of vertices in a sparse, edge-weighted, directed graph. |
| Graph Isomorphism (General)       | 2^(O((log n)^2))| Determines if two finite graph are isomorphic. |


<h3>Network properties</h3>

|                              |   Average Degree |   Max Degree |   Clustering Coefficient |   Number of Vertices |   Number of Edges |   Gamma |   LCC |   Avg. Path Length |
|:-----------------------------|-----------------:|-------------:|-------------------------:|---------------------:|------------------:|--------:|------:|-------------------:|
| Complete                     |          299     |          299 |                    1     |                  300 |             44850 |   1.238 |  1    |              1     |
| Stochaistic block model      |           88.773 |          105 |                    0.389 |                  300 |             13316 |   1.336 |  1    |              1.703 |
| Configuration model          |           10     |           10 |                    0.028 |                  300 |              1500 |   2.252 |  1    |              2.733 |
| Small world (wattz)          |            8     |           13 |                    0.088 |                  300 |              1200 |   2.745 |  1    |              3.045 |
| Scale-free gamma=2.5 (price) |            5.96  |           55 |                    0.075 |                  300 |               894 |   2.764 |  1    |              3.071 |
| Random <k> = 2               |            2.1   |            8 |                    0.01  |                  300 |               315 |   6.193 |  0.81 |              6.662 |
| Cycle                        |            2     |            2 |                    0     |                  300 |               300 | nan     |  1    |             75.251 |
| Tree                         |            1.993 |            7 |                    0     |                  300 |               299 |   3.295 |  1    |              5.495 |
