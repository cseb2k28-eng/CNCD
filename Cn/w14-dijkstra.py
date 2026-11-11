INF = 9999

def dijkstra(graph, n, source):
    dist = [INF] * n
    visited = [False] * n
    parent = [-1] * n

    dist[source] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if not visited[v] and graph[u][v] != INF:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u

    print("\nShortest distances from vertex", source)
    for i in range(n):
        print("Vertex", i, "=", dist[i])

    print("\nShortest Paths:")
    for i in range(n):
        path = []
        v = i

        while v != -1:
            path.append(v)
            v = parent[v]

        path.reverse()
        print(" -> ".join(map(str, path)), "=", dist[i])


n = int(input("Enter number of vertices: "))

print("Enter the cost matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0 and i != j:
            row[j] = INF
    graph.append(row)

source = int(input("Enter source vertex: "))

dijkstra(graph, n, source)


# Input:
# Enter number of vertices: 4
# Enter the cost matrix:
# 0 3 0 7
# 8 0 2 0
# 5 0 0 1
# 2 0 0 0
# Enter source vertex: 0

# Output:
# Shortest distances from vertex 0
# Vertex 0 = 0
# Vertex 1 = 3
# Vertex 2 = 5
# Vertex 3 = 6

# Shortest Paths:
# 0 = 0
# 0 -> 1 = 3
# 0 -> 1 -> 2 = 5
# 0 -> 1 -> 2 -> 3 = 6
