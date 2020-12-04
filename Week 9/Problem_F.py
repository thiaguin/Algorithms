# Title -> Sereja and Suffixes
# Description -> codeforces.com/problemset/problem/368/B

t = int(input())


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


def kruskal(edges, aux):
    forest = []
    total = 0

    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            forest.append(edge)
            union(edge[0], edge[1])
            total += aux[edge]

    return total


for test in range(t):
    break_line = input()
    n = int(input())
    cities = []
    edges = {}
    representatives = [0] * (n + 1)
    total = 0

    for el in range(n):
        city = input()
        p = int(input())
        representatives[el + 1] = el + 1

        for i in range(p):
            neigh, cost = map(int, input().split())
            x, y = min(el + 1, neigh), max(el + 1, neigh)

            if ((x, y) in edges):
                edges[(x, y)] = min(cost, edges[(x, y)])
            else:
                edges[(x, y)] = cost

    edges_sorted = sorted(edges.items(), key=lambda x: x[1])
    result = kruskal([x for x, _ in edges_sorted], edges)

    print(result)
