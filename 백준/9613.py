#gcd 합
from itertools import combinations

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

for i in range(n):
    result = list(map(int, input().split()))
    result = result[1:]
    ans = 0
    for a, b in combinations(result, 2):
        ans += gcd(a, b)
    print(ans)
    