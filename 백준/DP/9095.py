#1, 2, 3 더하기
def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if a[n] != 0:
        return a[n]
    a[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
    return a[n]

n = int(input())
a = [0] * (11)
for i in range(n):
    x = int(input())
    print(dp(x))