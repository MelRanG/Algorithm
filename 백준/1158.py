#요세푸스 문제
n, k = map(int, input().split())
q = [i for i in range(1, n + 1)]
answer = []
x = k - 1
while q:
    if x > len(q):
        x %= len(q)
    answer.append(q.pop(x))
    x += k - 1

print('<' + ', '.join(map(str, answer)) + '>')