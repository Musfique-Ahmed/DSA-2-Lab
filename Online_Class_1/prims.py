import heapq
import networkx as nx
import matplotlib.pyplot as plt

def primsAlgorithm(adjlist, root):
    parentArray = [-1]  * len(adjacency_list)
    key = [float('inf')] * len(adjacency_list)
    treeVertex = [False] * len(adjacency_list)

    key[root] = 0

    minHeap = [(key[root],root)] #(key, vertex)

    while minHeap:
        minkey , u = heapq.heappop(minHeap)
        treeVertex[u] = True

        for v, w in adjacency_list[u]:
            if not treeVertex[v] and key[v] > w:
                key[v] = w
                parentArray[v] = u
                heapq.heappush(minHeap, (key[v], v))

    return key, parentArray




# n = no of vertex, m = no of edge (50034)

with open("C:/Musfique's Folder/Python/DSA-2-Lab/Online_Class_1/sparseGraph.txt", "r") as f:
    # hi = f.readline()
    # print(repr(hi))
    # print(f.readline().split())
    # 1. Read the next line: f.readline() -> "5 10\n"
    # 2. Split the string into a list: .split() -> ['5', '10']
    # 3. Map the int function to each item in the list -> (an iterator for 5 and 10)
    n, m = map(int, f.readline().split())

    # print(n,m)

    adjacency_list = {i:[] for i in range(n)}
    # print(adjacency_list)

    for _ in range(m):
        u,v,w = map(int, f.readline().split())
        adjacency_list[u].append((v,w))
        adjacency_list[v].append((u,w))

    key, parent = primsAlgorithm(adjacency_list, 0)
    print(sum(key))

    # print(len(adjacency_list))




G = nx.Graph()

for u in range(n):
    if parent[u] != -1:
        G.add_edge(parent[u], u, weight = key[u])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True, node_size = 10, node_color='lightblue', font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
plt.show()