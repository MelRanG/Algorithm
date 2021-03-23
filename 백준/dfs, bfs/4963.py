# 섬의 개수
import sys
sys.setrecursionlimit(111111)

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, 1, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == 1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    dfs(nx, ny)
        return True
    return False

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = []
    visited = []
    result = []

    for i in range(m):
        graph.append(list(map(int, input().split())))
        visited.append([False] * n)

    for x in range(m):
        for y in range(n):
            count = 0
            if visited[x][y] == False:
                if dfs(x, y):
                    count += 1
            result.append(count)
    print(sum(result))