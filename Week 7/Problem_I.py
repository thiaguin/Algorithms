# Title -> Alyona and the Tree
# Description -> codeforces.com/problemset/problem/682/C

n = input()
vertices = map(int, raw_input().split())
graph = {}
nodes = [(1, 0)]
visiteds = {1: False}
count = 0
removeds = {}


def add_removes(node):
    if (not node in removeds):
        array = graph[node] if node in graph else []
        removeds[node] = True
        visiteds[node] = True

        while len(array) > 0:
            index, _ = array.pop()

            if (not index in removeds):
                removeds[index] = True
                aux = graph[index] if index in graph else []

                for element, value in aux:
                    array.append((element, value))


for i in range(2, n + 1):
    p, c = map(int, raw_input().split())
    visiteds[i] = False

    if (p in graph):
        graph[p].append((i, c))
    else:
        graph[p] = [(i, c)]

while len(nodes) > 0:
    node, distance = nodes.pop()

    if (not visiteds[node]):
        visiteds[node] = True

        if (vertices[node - 1] < distance and not node in removeds):
            add_removes(node)

        else:
            array = graph[node] if node in graph else []
            for index, value in array:
                nodes.append((index, max(0, distance + value)))

print(len(removeds))
