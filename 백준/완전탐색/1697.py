# 숨바꼭질
from collections import deque
n, k = map(int, input().split())
m = 100001
time = [0] * m

def bfs():
    q = deque([n])

    while q:
        v = q.popleft()

        if v == k:
            print(time[v])
            return
        
        for i in (v-1, v+1, v*2):
            if 0 <= i < m and not time[i]:
                q.append(i)
                time[i] = time[v] + 1
bfs()
