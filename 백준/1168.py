#요세푸스 문제2
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])

answer = []
x = k - 1

while q:
    q.rotate(-x)
    answer.append(str(q.popleft()))

print('<' + ', '.join(answer) + '>')