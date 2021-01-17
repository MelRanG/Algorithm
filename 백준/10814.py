n = int(input())
result = []
for i in range(n):
    x, y = input().split()
    result.append((int(x), y))
result.sort(key=lambda x:(x[0]))
for i in result:
    print(i[0], i[1])