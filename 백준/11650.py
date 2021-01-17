n = int(input())
result = []
for i in range(n):
    x, y = map(int, input().split())
    result.append((x, y))
result.sort(key=lambda x: (x[0],x[1]))
for i in sorted(result):
    print(i[0], i[1])