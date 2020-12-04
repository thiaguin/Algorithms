# Title -> Bear and Friendship Condition
# Description -> codeforces.com/problemset/problem/771/A

n, m = map(int, raw_input().split())
graph = {}
visiteds = {}

for i in range(m):
    a, b = map(int, raw_input().split())

    if (a in graph):
        graph[a][b] = True
    else:
        graph[a] = {b: True, a: True}

    if (b in graph):
        graph[b][a] = True
    else:
        graph[b] = {a: True, b: True}


def get_result(value):
    for key in graph[value]:
        visiteds[key] = True
        if graph[value] != graph[key]:
            return False

    return True


def return_result():
    for i in graph:
        if not i in visiteds:
            result = get_result(i)
            if (not result):
                return 'NO'

    return 'YES'


print(return_result())
