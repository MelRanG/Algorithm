#2×n 타일링
import sys
sys.setrecursionlimit(10**6)
n = int(input())
a = [0 for _ in range(n + 1)]
def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if a[n] != 0:
        return a[n]
    a[n] = (dp(n - 1) + dp(n - 2)) % 10007
    return a[n]
print(dp(n))

