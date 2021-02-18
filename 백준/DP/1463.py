#1로 만들기 탑다운시 메모리초과발생하므로 바텀업으로 풀어야함
n = int(input())
a = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    a[i] = a[i - 1] + 1
    if i % 2 == 0:
        a[i] = min(a[i], a[i // 2] + 1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i // 3] + 1)
print(a[n])

