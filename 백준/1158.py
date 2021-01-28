#요세푸스 문제

n, k = map(int, input().split())
q = [i for i in range(1, n + 1)]
answer = []
i = k - 1

while q:
    if i >= len(q):
        i %= len(q)
    answer.append(q.pop(i))
    i += k - 1
print('<' + ', '.join(map(str, answer)) + '>')