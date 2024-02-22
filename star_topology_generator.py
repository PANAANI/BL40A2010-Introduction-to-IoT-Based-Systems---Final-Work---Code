import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

Nodes = 6 # Defines how many nodes are created

# This part creates the star topology graph
G = nx.Graph()

for i in range(Nodes):
    G.add_node(i + 1)

for i in range(Nodes - 1):
    G.add_edge(1, i + 2)

# Print out some information regarding the graph
print("The Adjacency Matrix")
print(nx.adjacency_matrix(G).todense())
print("The degrees:", G.degree())
print("Clustering", nx.clustering(G))
print("The diameter:", nx.diameter(G))

# Show the result
nx.draw_networkx(G, node_color="black", font_color="white", edge_color="black", font_weight="bold", node_size=700)
plt.show()
