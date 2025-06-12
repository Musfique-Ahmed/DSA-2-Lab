from heapq import heappop, heappush
import networkx as nx
import matplotlib.pyplot as plt

def prim(adjList, root):
    key = [float('inf') for _ in range(len(adjList))]
    parent = [-1 for _ in range(len(adjList))]
    tree = [False for _ in range(len(adjList))]  
    key[root] = 0
    pq = [(0, root)]  # (key, vertex)
    while pq:
        k, u = heappop(pq)
        if tree[u]:
            continue
        tree[u] = True
        for v, w in adjList[u]:
            if not tree[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heappush(pq, (w, v))
    return key, parent

with open('sparseGraph.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    adjList = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, w = map(int, f.readline().split())
        adjList[u].append((v, w))
        adjList[v].append((u, w))
        
key, parent = prim(adjList, 0)

print(f"MST total weight {sum(key)}")

G = nx.Graph()
for u in range(n):
    if parent[u] != -1:
        G.add_edge(parent[u], u, weight=key[u])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=10, node_color='lightblue', font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
        

