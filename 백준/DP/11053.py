#가장 긴 증가하는 부분 수열
n = int(input())
dp = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    for j in range(i):
        if dp[i] > dp[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] += 1
print(max(result))
