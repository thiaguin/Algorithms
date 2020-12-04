# Title -> The Two Routes
# Description -> codeforces.com/problemset/problem/601/A

from heapq import heappush, heappop

n, m = map(int, raw_input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, raw_input().split())
    graph[u] += [v]
    graph[v] += [u]


def return_aux(index):
    return [x for x in range(1, n + 1) if x not in graph[index] and x != index]


graph_aux = [return_aux(i) for i in range(n + 1)]


def dijkstra(n, queue, graph):
    distances = [-1] * (n + 1)
    heappush(queue, (0, 1))

    while len(queue) > 0:
        size, vertex = heappop(queue)
        if distances[vertex] == -1:
            distances[vertex] = size
            for next_vertex in graph[vertex]:
                if distances[next_vertex] == -1:
                    heappush(queue, (size + 1, next_vertex))

    return distances


graph_distances = dijkstra(n, [], graph)
graph_aux_distances = dijkstra(n, [], graph_aux)

value_1 = graph_distances[n]
value_2 = graph_aux_distances[n]

result = -1 if -1 in [value_1, value_2] else max(value_1, value_2)
print(result)
