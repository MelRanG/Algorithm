# 미로 탐색
#q에 count변수를 넣어서 계속 돌렸으니 시간초과가 떠서 배열자체에 이동횟수만큼 카운트하는 방식 사용
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []
visited = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip())))
    visited.append([0] * m)

q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


