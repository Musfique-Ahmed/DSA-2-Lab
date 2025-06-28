from random import *

n = 200 #number of nodes
p = 0.2 #probability of edge creation
minEdgeWeight = 1 #minimum edge weight
maxEdgeWeight = 100 #maximum edge weight

def dfs(node, n, edges):
    visited = [False] * n
    stack = [node]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for edge in edges:
                if edge[0] == current and not visited[edge[1]]:
                    stack.append(edge[1])
                elif edge[1] == current and not visited[edge[0]]:
                    stack.append(edge[0])
    return all(visited)

# Create a random graph
edges = []
connected = False
while not connected:
    for i in range(n):
        for j in range(i + 1, n):
            if random() < p:
                edges.append((i, j, randint(minEdgeWeight, maxEdgeWeight)))
    # Check if the graph is connected
    connected = dfs(0, n, edges)
    
# Shuffle the edges to create a random order
shuffle(edges)
# Write the sparse graph to a file
with open("sparseGraph.txt", "w") as f:
    f.write(f"{n} {len(edges)}\n")
    for edge in edges:
        f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
        
# Write the dense graph to a file
# with open("denseGraph.txt", "w") as f:
#     f.write(f"{n} {len(edges)}\n")
#     for edge in edges:
#         f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

