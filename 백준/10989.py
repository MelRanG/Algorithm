import sys
n = int(sys.stdin.readline())
result = [0] * 10001
for i in range(n):
    a = int(sys.stdin.readline())
    result[a] += 1
for i in range(len(result)):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)