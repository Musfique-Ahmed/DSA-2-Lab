import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush
import argparse

def dijkstra(adjList, root):
    n = len(adjList) # number of vertices
    # Initialization
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[root] = 0
    minHeap = [(0, root)]  # (distance, vertex)

    while minHeap:
        d, u = heappop(minHeap)
        if d > dist[u]: # If the distance is not optimal, skip (Duplicate touple)
            continue
        for v, w in adjList[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                parent[v] = u
                heappush(minHeap, (dist[v], v))
    
    return dist, parent

def printCycle(node, parent):
    cycle = []
    current = parent[node]
    while current != node:
        cycle.append(current)
        current = parent[current]
    cycle.append(node)
    cycle.reverse()
    print("Negative weight cycle detected:", " -> ".join(map(str, cycle)))

def bellmanFord(adjList, root):
    n = len(adjList)  # number of vertices
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[root] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in adjList[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parent[v] = u

    # Check for negative weight cycles
    for u in range(n):
        for v, w in adjList[u]:
            if dist[v] > dist[u] + w:
                printCycle(u, parent)
                raise ValueError("Graph contains a negative weight cycle")

    return dist, parent


def graphInput(filename):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        graph = nx.Graph()
        adj = {i: [] for i in range(n)}
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph.add_edge(u, v, weight=w)
            adj[u].append((v, w))
            # adj[v].append((u, w))
    return graph, adj
        
            
def show_graph(graph, title="Graph Visualization"):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)  
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_color='black', edge_color='gray')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='black', font_size=6)
    plt.title(title)
    plt.show()
    
def showShortestPath(graph, parent, root):
    mst_edges = [(parent[i], i) for i in range(len(parent)) if parent[i] != -1]
    mst_graph = nx.DiGraph()
    mst_graph.add_edges_from(mst_edges)
    
    plt.figure(figsize=(10, 8))
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=400, node_color='lightblue', font_size=10, font_color='black', edge_color='gray')
    nx.draw_networkx_edges(mst_graph, pos, edge_color='red', width=2)
    plt.title(f"Shortest Path Tree from Node {root}")
    plt.show()
    
graph, adj = graphInput('graph.txt')
show_graph(graph, title="Sparse Graph Visualization")
#dist, parent = dijkstra(adj, 0)
dist, parent = bellmanFord(adj, 0)
showShortestPath(graph, parent, 0)

# print(dist[13])

# destination = 7
# route = []
# while destination != -1:
#     route.append(destination)
#     destination = parent[destination]
# print(dist[7])
    
# print(*route[::-1], sep=' -> ')

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Run single source shortest path algorithm on a graph.")
#     parser.add_argument('n', type=int, default=20, help='Number of nodes in the graph')
#     parser.add_argument('p', type=float, default=0.5, help='Probability of edge creation')
#     parser.add_argument('minEdgeWeight', type=int, default=1, help='Minimum edge weight')
#     parser.add_argument('maxEdgeWeight', type=int, default=100, help='Maximum edge weight')
#     parser.add_argument('--directed', action='store_true', help='If the graph is directed')
#     parser.add_argument('filename', type=str, help='Input file containing the graph data')
#     parser.add_argument('--algorithm', type=str, choices=['dijkstra', 'bellman-ford'], default='dijkstra', help='Algorithm to use for finding shortest paths')