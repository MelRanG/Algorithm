# 대회 or 인턴
n, m, k = map(int, input().split())

count = 0

while n >= 0 and m >= 0 and n + m >= k:
    n -= 2
    m -= 1
    count += 1
print(count-1)
