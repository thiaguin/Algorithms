# Title -> Xenia and Ringroad
# Description -> codeforces.com/problemset/problem/339/B

m, n = map(int, input().split())


def fill_values(graph, edges):
    total = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        x, y = min(x, y), max(x, y)
        total += z

        if ((x, y) in graph):
            graph[x][y] = z
        else:
            graph[x] = {y: z}

        if ((x, y) in edges):
            edges[(x, y)] = min(z, edges[(x, y)])
        else:
            edges[(x, y)] = z

    return total


def find(x):
    if (representatives[x] != x):
        representatives[x] = find(representatives[x])

    return representatives[x]


def union(x, y):
    xRepresentative = find(x)
    yRepresentative = find(y)

    if (yRepresentative != xRepresentative):
        if (yRepresentative > yRepresentative):
            representatives[yRepresentative] = xRepresentative
        else:
            representatives[xRepresentative] = yRepresentative


def kruskal(graph, edges, aux):
    forest = []
    total = 0

    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            forest.append(edge)
            union(edge[0], edge[1])
            total += aux[edge]

    return total


while (n != 0 and m != 0):
    graph = {}
    edges = {}
    representatives = [0] * m
    total = fill_values(graph, edges)

    for i in range(m):
        representatives[i] = i

    edges_sorted = sorted(edges.items(), key=lambda x: x[1])
    result = kruskal(graph, [x for x, _ in edges_sorted], edges)

    print(total - result)
    m, n = map(int, input().split())
