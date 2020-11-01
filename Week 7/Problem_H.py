# Title -> Ice Skating
# Description -> codeforces.com/problemset/problem/217/A

MOD = 10 ** 9 + 7
maximum = 10 ** 6
fats = [1]

n = input()
graph = []
visited = []
result = -1


def dfs(node):
    if (not visited[node]):
        visited[node] = True
        for i in range(n):
            if (graph[node][0] == graph[i][0] or graph[node][1] == graph[i][1]):
                dfs(i)


for i in range(n):
    x, y = map(int, raw_input().split())
    graph.append((x, y))
    visited.append(False)

for i in range(n):
    if (not visited[i]):
        result += 1
        dfs(i)

print(result)
