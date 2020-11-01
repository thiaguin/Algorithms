# Title -> K-th Beautiful String
# Description -> codeforces.com/problemset/problem/1328/B

t = input()


def get_result(n, k):
    count = 0
    aux = 1

    while (k > count):
        count += aux
        aux += 1

    return [k - ((aux - 1) * (aux - 2) / 2), aux]


for i in range(t):
    n, k = map(int, raw_input().split())
    indexes = get_result(n, k)
    first_a = 'a' * (n - max(indexes))
    second_a = 'a' * (max(indexes) - min(indexes) - 1)
    last_a = 'a' * (min(indexes) - 1)
    result = first_a + 'b' + second_a + 'b' + last_a

    print(result)
