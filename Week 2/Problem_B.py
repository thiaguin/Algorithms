# Title -> Kuriyama Mirai's Stones
# Description -> codeforces.com/problemset/problem/433/B

n = input()
stones = map(int, raw_input().split())
questions = input()

stones_ordered = stones[:]
stones_ordered.sort()

sums = [stones[0]]
sums_ordered = [stones_ordered[0]]

for i in range(1, n):
    sums.append(sums[i - 1] + stones[i])
    sums_ordered.append(sums_ordered[i - 1] + stones_ordered[i])


def getAnswer(left, right, question_type):
    if (question_type == 1):
        return sums[right - 1] - sums[left - 1] + stones[left - 1]
    else:
        return sums_ordered[right - 1] - sums_ordered[left - 1] + stones_ordered[left - 1]


for i in range(questions):
    question_type, left, right = map(int, raw_input().split())
    print(getAnswer(left, right, question_type))
