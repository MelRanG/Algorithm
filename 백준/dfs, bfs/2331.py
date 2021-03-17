#반복수열
n, p = map(int, input().split())
dp = []

def dfs(n):
    dp.append(n)

    d = [i for i in str(n)]
    sum = 0
    for i in d:
        sum += (int(i) ** p)
    for i in range(len(dp)):
        if dp[i] == sum:
            print(i)
            return False
    dfs(sum)    

dfs(n)