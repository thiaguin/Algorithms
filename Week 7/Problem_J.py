# Title -> Mr. Kitayuta's Colorful Graph
# Description -> codeforces.com/problemset/problem/505/B

n, m = map(int, raw_input().split())
graph = []
edges = {}
vertex_edges = {}
visited = [False] * n


def dfs(u, edge):
    if (not visited[u]):
        visited[u] = True
        for i in range(len(graph)):
            vertex_1 = (min(graph[i][1], u + 1), max(graph[i][1], u + 1))
            vertex_2 = (min(graph[i][0], u + 1), max(graph[i][0], u + 1))

            if (graph[i][0] == u + 1 and vertex_1 in edges and edge in edges[vertex_1]):
                dfs(graph[i][1] - 1, edge)
            if (graph[i][1] == u + 1 and vertex_2 in edges and edge in edges[vertex_2]):
                dfs(graph[i][0] - 1, edge)


for i in range(m):
    a, b, c = map(int, raw_input().split())
    graph.append((a, b))
    vertex = (min(a, b), max(a, b))

    if (vertex in edges):
        edges[vertex].append(c)
    else:
        edges[vertex] = [c]

    if (a in vertex_edges):
        vertex_edges[a].append(c)
    else:
        vertex_edges[a] = [c]

    if (b in vertex_edges):
        vertex_edges[b].append(c)
    else:
        vertex_edges[b] = [c]

q = input()

for i in range(q):
    u, v = map(int, raw_input().split())
    count = 0

    if (u in vertex_edges):
        vertex_edges[u] = list(set(vertex_edges[u]))

        for j in vertex_edges[u]:
            visited = [False] * n
            dfs(u - 1, j)
            if (visited[v - 1]):
                count += 1

    print(count)
