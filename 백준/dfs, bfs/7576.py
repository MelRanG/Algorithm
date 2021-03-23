# 토마토
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(q):
    while q:
        x, y, count = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny, count + 1))
    for i in graph:
        if 0 in i:
            return -1
    return count


m, n = map(int, input().split())
graph = []
q = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))

print(bfs(q))
