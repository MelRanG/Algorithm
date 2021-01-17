n = int(input())
result = []
for i in range(n):
    x, y, z, g = input().split()
    result.append((x, int(y), int(z), int(g)))
result.sort(key=lambda x:(-x[1],x[2], -x[3], x[0]))
for i in result:
    print(i[0])