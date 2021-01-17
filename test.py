import sys
n = int(sys.stdin.readline())

result = [0] * 100001
for i in range(n):
    a = int(sys.stdin.readline())
    result[a] += 1
m = 0
index = 0
print("-----------")
for i in range(len(result)):
    if result[i] > m:
        m = max(m, result[i])
        index = i
print(index)