import igraph as ig
import random

g = ig.Graph.Erdos_Renyi(100, 0.1)

print("Assortativity before rewiring: ", g.assortativity_degree(directed=False))

for _ in range(1000):
    e1 = random.choice(g.es)
    e2 = random.choice(g.es)
    
    # Store source and target nodes before deleting edges
    e1_source, e1_target = e1.source, e1.target
    e2_source, e2_target = e2.source, e2.target
    
    # Check if rewiring would increase assortativity
    if e1_source != e2_source and e1_target != e2_target:
        if g.degree(e1_source) > g.degree(e2_source) and g.degree(e1_target) < g.degree(e2_target):
            g.delete_edges([e1, e2])
            g.add_edges([(e1_source, e2_target), (e2_source, e1_target)])

print("Assortativity after rewiring: ", g.assortativity_degree(directed=False))