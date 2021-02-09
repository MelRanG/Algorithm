#소수 구하기
def isPrime(v):
    if v == 1:
        return False
    for i in range(2, int(v**0.5) + 1):
        if v % i == 0:
            return False
    return True

n, m = map(int, input().split())

for i in range(n, m + 1):
    if isPrime(i):
        print(i)