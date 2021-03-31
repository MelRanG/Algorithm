# 차이를 최대로
from itertools import permutations

n = int(input())
graph = permutations(list(map(int, input().split())))
ans = 0

for i in graph:
    sum = 0
    for j in range(n - 1):
        sum += abs(i[j] - i[j+1])
    ans = max(ans, sum)
print(ans)