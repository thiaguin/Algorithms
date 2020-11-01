# Title -> Fox And Two Dots
# Description -> codeforces.com/problemset/problem/510/B

n, m = map(int, raw_input().split())
puzzle = []
graph = []
flag = False


def get_graph():
    row = [False] * m
    result = []

    for i in range(n):
        result.append(row[:])

    return result


def dfs(x, y, value, graph, original, target):
    if (x < n and y < m and x >= 0 and y >= 0 and not graph[x][y]):
        if (puzzle[x][y] == value and (x, y) != original):
            graph[x][y] = True
            if ((x, y) == target):
                return True

            return dfs(x - 1, y, value, graph, original, target) or dfs(x, y - 1, value, graph, original, target) or dfs(x, y + 1, value, graph, original, target) or dfs(x + 1, y, value, graph, original, target)

    return False


def get_result(graph):
    for i in range(n - 1):
        for j in range(m - 1):
            graph = get_graph()
            result = dfs(i, j + 1, puzzle[i][j], graph, (i, j), (i + 1, j))

            if (result):
                return True

    return False


for i in range(n):
    row = list(raw_input())
    puzzle.append(row)


result = 'Yes' if get_result(graph) else 'No'
print(result)
