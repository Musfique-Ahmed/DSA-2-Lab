with open('sparseGraph.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    edgeList = []
    for _ in range(m):
        u, v, w = map(int, f.readline().split())
        edgeList.append((w, u, v))
    

# Disjoint Set Union (DSU) or Union-Find data structure implementation
parent = [i for i in range(n)]
rank = [0] * n

def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]
def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
def kruskal(edgeList):
    edgeList.sort()  # Sort edges by weight
    total_weight = 0
    mst_edges = [] # List to store edges in the MST
    
    for w, u, v in edgeList:
        if find(u) != find(v):  # If u and v are not connected
            union(u, v)  # Connect u and v
            total_weight += w
            mst_edges.append((u, v, w))  # Store the edge in the MST
            
    return total_weight, mst_edges

kruskal_weight, mst_edges = kruskal(edgeList)

print(f"MST(Kruskal) total weight: {kruskal_weight}")