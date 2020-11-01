# Title -> 	Metro
# Description -> codeforces.com/problemset/problem/1055/A

n, s = map(int, raw_input().split())
stations_1 = map(int, raw_input().split())
stations_2 = map(int, raw_input().split())

aux = []

for i in range(n):
    if (stations_1[i] and stations_2[i]):
        aux.append(i)


def get_result():
    if (not stations_1[0] or (not stations_1[s - 1] and not stations_2[s-1])):
        return False
    if (stations_1[s - 1]):
        return True
    if (stations_2[s - 1]):
        return len(aux) > 0 and max(aux) > s - 1


result = 'YES' if get_result() else 'NO'
print(result)
