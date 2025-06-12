

# n = no of vertex, m = no of edge

with open("C:/Musfique's Folder/Python/DSA-2-Lab/Online_Class_1/sparseGraph.txt", "r") as f:
    # hi = f.readline()
    # print(repr(hi))
    # print(f.readline().split())
    # 1. Read the next line: f.readline() -> "5 10\n"
    # 2. Split the string into a list: .split() -> ['5', '10']
    # 3. Map the int function to each item in the list -> (an iterator for 5 and 10)
    n, m = map(int, f.readline().split())

    # print(n,m)

    adjacency_matrix = {i:[] for i in range(n)}
    print(adjacency_matrix)