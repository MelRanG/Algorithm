#2 x n타일링 2
import sys
sys.setrecursionlimit(10**6)

def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if a[n] != 0:
        return a[n]
    a[n] = (dp(n - 1) + dp(n - 2) * 2) % 10007
    return a[n]
n = int(input())
a = [0] * (n+1)

print(dp(n))