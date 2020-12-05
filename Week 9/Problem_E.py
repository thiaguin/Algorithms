# Title -> Xenia and Ringroad
# Description -> codeforces.com/problemset/problem/339/B

n, m = map(int, raw_input().split())
tasks = map(int, raw_input().split())

aux = [tasks[0] - 1]
current = tasks[0]


for i in range(1, m):
    if tasks[i - 1] < tasks[i]:
        aux.append(tasks[i] - tasks[i - 1])
    elif tasks[i - 1] > tasks[i]:
        aux.append(n - tasks[i - 1] + tasks[i])

print(sum(aux))
