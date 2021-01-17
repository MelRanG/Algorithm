import sys
n = int(input())
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))
for i in sorted(result):
    print(i)