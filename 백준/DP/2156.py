#2156 포도주 시식
n = int(input())
arr = [int(input()) for x in range(n)]

dp = [0]
dp.append(arr[0])

if(n > 1):
    dp.append(arr[0] + arr[1])

# 연속 3잔을 마시지 않아야 하므로
# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3 : 이번 포도주를 먹지 않아야 하는 경우
# 위 세가지 경우를 고려하여 max

for i in range(3, n + 1):
    #arr은 0부터 시작하므로 1을 빼준다.
    dp.append(max(dp[i - 1], dp[i - 2] + arr[i - 1], dp[i - 3] + arr[i - 1] + arr[i - 2]))
print(dp[n])

