INF = 999

n = int(input("Enter number of vertices: "))
print("Enter cost matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]
source = int(input("Enter source vertex: "))

if n < 1 or any(len(row) != n for row in graph) or not 0 <= source < n:
    raise SystemExit("Invalid graph or source vertex.")

distance = [INF] * n
visited = [False] * n
parent = [-1] * n
distance[source] = 0

for _ in range(n):
    vertex = -1
    for i in range(n):
        if not visited[i] and (vertex == -1 or 
                               distance[i] < distance[vertex]):
            vertex = i

    if vertex == -1 or distance[vertex] == INF:
        break

    visited[vertex] = True
    for neighbor in range(n):
        cost = graph[vertex][neighbor]
        if cost and not visited[neighbor] and distance[vertex] + cost < distance[neighbor]:
            distance[neighbor] = distance[vertex] + cost
            parent[neighbor] = vertex

print("\nShortest Paths:")
for vertex in range(n):
    if distance[vertex] == INF:
        print(f"Vertex {vertex} is unreachable")
        continue

    path = []
    current = vertex
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(" -> ".join(map(str, path)), "=", distance[vertex])
