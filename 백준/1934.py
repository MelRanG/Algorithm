from collections import deque
from math import gcd
n = int(input())
q = deque([])
for i in range(n):
    q.append((map(int, input().split())))
while q:
    a, b = q.popleft()
    c = gcd(a, b)
    print(a * b // c)
