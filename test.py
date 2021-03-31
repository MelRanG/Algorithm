n = 1033
sieve = [True] * n

for _ in range(n):
    b = 8179
    m = int(b ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

# while True:
#     if str(n) == str(b):
#         break
#     n = 8179

num = []
for i in str(n):
    num.append(i)
for i in range(len(num)):
    int(num[i]) += 1