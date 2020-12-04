# Title -> Cut Ribbon
# Description -> codeforces.com/problemset/problem/189/A

import sys
sys.setrecursionlimit(15000)

n = input()
r1, c1 = map(int, raw_input().split())
r2, c2 = map(int, raw_input().split())

graph = []
visiteds_by_source = {}
visiteds_by_target = {}
results = []
result = -1

for i in range(n):
    row = list(raw_input())
    graph.append(row)


def dfs(x, y, visiteds):
    valid_x = x >= 0 and x < n
    valid_y = y >= 0 and y < n
    valid_point = valid_x and valid_y

    if (valid_point and graph[x][y] == '0' and not (x, y) in visiteds):
        visiteds[(x, y)] = True
        dfs(x - 1, y, visiteds)
        dfs(x, y - 1, visiteds)
        dfs(x + 1, y, visiteds)
        dfs(x, y + 1, visiteds)

    return


def get_answer(x1, y1, x2, y2):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


dfs(r1 - 1, c1 - 1, visiteds_by_source)

if ((r2 - 1, c2 - 1) in visiteds_by_source):
    result = 0
else:
    dfs(r2 - 1, c2 - 1, visiteds_by_target)
    result = get_answer(r1, c1, r2, c2)

    for x_source, y_source in visiteds_by_source:
        for x_target, y_target in visiteds_by_target:
            answer = get_answer(x_source, y_source, x_target, y_target)
            result = min(result, answer)


print(result)
