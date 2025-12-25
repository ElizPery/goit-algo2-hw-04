from collections import deque

# Function for finding an augmenting path (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        
        for neighbor in range(len(capacity_matrix)):
            # Check if there is residual capacity in the channel
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    
    return False

# Main function for calculating maximum flow
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Initialize the flow matrix to zero
    parent = [-1] * num_nodes
    max_flow = 0

    # While there is an augmenting path, add flow
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Find the minimum residual capacity along the found path (bottleneck)
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node
        
        # Update the flow along the path, considering the reverse flow
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node
        
        # Increase the maximum flow
        max_flow += path_flow

    return max_flow

# Matrix of capacity for channels in the network (capacity_matrix)
capacity_matrix = [
    [0, 0, 25, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 1
    [0, 0, 0, 10, 15, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Terminal 2
    [0, 0, 0, 0, 0, 0, 15, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Storage 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 10, 25, 0, 0, 0, 0, 0, 0, 0, 0],  # Storage 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 15, 10, 0, 0, 0, 0, 0],  # Storage 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 15, 5, 10], # Storage 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Shop 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      # Shop 14
]

# Calculate and print maximum flow from each terminal to each shop
max_flow_ter_1 = 0
max_flow_ter_2 = 0
print(f"Terminal       Shop       Max Flow")
print(f"-----------------------------------")
for terminal in range(2):
    for shop in range(1, 15):
        source = terminal
        sink = shop + 5
        if terminal == 0 and shop in [1,2,3,4,5,6,7,8,9]:
            max_flow = edmonds_karp(capacity_matrix, source, sink)
            max_flow_ter_1 += max_flow
            print(f"Terminal {terminal + 1}     Shop {shop}     {max_flow}")
        if terminal == 1 and shop in [4,5,6,7,8,9,10,11,12,13,14]:
            max_flow = edmonds_karp(capacity_matrix, source, sink)
            max_flow_ter_2 += max_flow
            print(f"Terminal {terminal + 1}     Shop {shop}     {max_flow}")

print(f"-----------------------------------")
print(f"Total Max Flow from Terminal 1: {max_flow_ter_1}")
print(f"Total Max Flow from Terminal 2: {max_flow_ter_2}")          

# 1. As it can be seen from the results, Terminal 1 and Terminal 2 have delivered the same flow to various shops that equal 130.
# 2. One of the main route that has the least capacity and affects the maximum flow is the route from Terminal 2 to Storage 2 with a capacity of 10.
# Because of that, shops 9, 11 receive less flow compared to possible.
# 3. The least capacity is the route from Terminal 2 to Shop 13 with a capacity of 5. To increase it, make the capacity of the route from Storage 2 to Shop 18 higher. 
# As well, to increase the overall flow from terminals to shops, the capacity of the route from Terminal 2 to Storage 2 can be increased.
# 4. In my opinion, to improve the efficiency of the logistics network, it needs to increase the capacity of the routes from Terminal 1 to Storage 2 to 25, 
# from Terminal 2 to Storage 2 to 25, from Terminal 1 to Storage 3 to 20, and from Terminal 2 to Storage 3 to 20.
# Overall, this algorithm reached optimal flow distribution from terminals to shops based on the given capacities that is very usefull for considered network.