# Title -> Social Network (hard version)
# Description -> codeforces.com/problemset/problem/1234/B2

n, k = map(int, raw_input().split())
ids = raw_input().split()

queue = []
aux = {}
count = 0
index = 0

for i in ids:
    if (not aux.has_key(i)):
        aux[i] = True

        if (count < k):
            count += 1
            queue.append(i)
        else:
            last = queue[index]
            index += 1
            queue.append(i)
            del aux[last]

result = []
max_range = len(queue)
conversations_shown = min(k, max_range)

for j in range(conversations_shown):
    result.append(queue[max_range - j - 1])

print(conversations_shown)
print(' '.join(result))
