n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter number of edges: "))
for i in range(e):
    u, v = map(int, input("Enter edge: ").split())
    graph[u].append(v)
    graph[v].append(u)
print("\nGraph:")
for i in range(n):
    print(i, "->", graph[i])
start = int(input("\nEnter starting vertex: "))
visited = [False] * n
queue = [start]
visited[start] = True

print("\nBFS Traversal:")
while queue:
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)
visited = [False] * n
stack = [start]
print("\n\nDFS Traversal:")
while stack:
    vertex = stack.pop()

    if not visited[vertex]:
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbour in reversed(graph[vertex]):
            if not visited[neighbour]:
                stack.append(neighbour)
