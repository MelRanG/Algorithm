import queue
import sys

n = int(sys.stdin.readline())
q = queue.deque()

for _ in range(n):
    s = sys.stdin.readline().split()
    op = s[0]

    if op == 'push':
        q.append(s[1])
    elif op == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif op == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif op == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
