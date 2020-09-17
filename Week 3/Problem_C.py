# Title ->  A and B and Compilation Errors
# Description -> codeforces.com/problemset/problem/519/B

n = input()
initial = map(int, raw_input().split())
second = map(int, raw_input().split())
third = map(int, raw_input().split())

initial_sum = sum(initial)
second_sum = sum(second)
third_sum = sum(third)

print(initial_sum - second_sum)
print(second_sum - third_sum)
