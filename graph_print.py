import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.DiGraph()

# Add edges with capacity
edges = [
    (0, 2, 25),  # Terminal 1 -> Storage 1
    (0, 3, 20),  # Terminal 1 -> Storage 2
    (0, 4, 15),  # Terminal 1 -> Storage 3
    (1, 3, 10),  # Terminal 2 -> Storage 2
    (1, 4, 15),  # Terminal 2 -> Storage 3
    (1, 5, 30),  # Terminal 2 -> Storage 4
    (2, 6, 15),  # Storage 1 -> Shop 1
    (2, 7, 10),  # Storage 1 -> Shop 2
    (2, 8, 20),  # Storage 1 -> Shop 3
    (3, 9, 15),  # Storage 2 -> Shop 4
    (3, 10, 10),  # Storage 2 -> Shop 5
    (3, 11, 25),  # Storage 2 -> Shop 6
    (4, 12, 20),  # Storage 3 -> Shop 7
    (4, 13, 15),  # Storage 3 -> Shop 8
    (4, 14, 10),  # Storage 3 -> Shop 9
    (5, 15, 20),  # Storage 4 -> Shop 10
    (5, 16, 10),  # Storage 4 -> Shop 11
    (5, 17, 15),  # Storage 4 -> Shop 12
    (5, 18, 5),  # Storage 4 -> Shop 13
    (5, 19, 10),  # Storage 4 -> Shop 14
]

# Add all edges to the graph
G.add_weighted_edges_from(edges)

# Positions for drawing the graph
pos = {
    0: (1, 2),  # Terminal 1
    1: (5, 2),  # Terminal 2
    2: (2, 3),  # Storage 1
    3: (4, 3),  # Storage 2
    4: (2, 1),  # Storage 3
    5: (4, 1),  # Storage 4
    6: (0, 4),  # Shop 1
    7: (1, 4),  # Shop 2
    8: (2, 4),  # Shop 3
    9: (3, 4),  # Shop 4
    10: (4, 4),  # Shop 5
    11: (5, 4),  # Shop 6
    12: (0, 0),  # Shop 7
    13: (1, 0),  # Shop 8
    14: (2, 0),  # Shop 9
    15: (3, 0),  # Shop 10
    16: (4, 0),  # Shop 11
    17: (5, 0),  # Shop 12
    18: (6, 0),  # Shop 13
    19: (7, 0),  # Shop 14
}

# Paint the graph
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()