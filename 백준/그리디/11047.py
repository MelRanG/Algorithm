# 동전 0
n, k = map(int, input().split())
money = []

for i in range(n):
    money.append(int(input()))

count = 0

for i in sorted(money, reverse=True):
    if k // i != 0:
        count += k // i
        k %= i
print(count)