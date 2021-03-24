# 다리 만들기
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]* n for _ in range(n)]
ocean = deque()
gid = -1

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def grouping(x, y):
    q = deque([(x, y)])
    graph[x][y] = gid
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = gid
                    q.append((nx, ny))
                # 상하좌우가 바다라면, 즉 섬의 끝부분이라면
                elif graph[nx][ny] == 0 and not (x,  y) in ocean:
                    ocean.append((x, y))

def get_distance(): # 모든 섬이 동시에 확장
    loop = 0
    ans = sys.maxsize
    while ocean:
        # 전체 섬을 한 번 확장할 때 마다 카운트하기 위해 loop를 증가시킴
        # 한 번씩 확장하기 위해서 ocean의 길이만큼만 돔
        loop += 1
        length = len(ocean)
        for _ in range(length):
            x, y = ocean.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < n and 0 <= nx < n:
                    # 옆이 바다라면 섬을 확장한 후 다시 섬의 끝부분을 큐에 넣는다.
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        ocean.append((nx, ny))
                    # 낮은숫자(-1)가 높은숫자(-2)를 덮칠 때 = 다음차례에 겹침
                    elif graph[nx][ny] < graph[x][y]:
                        ans = min(ans, (loop - 1) * 2)
                    # 높은숫자가 낮은숫자를 덮칠 때 = 이번차례에 겹침
                    elif graph[nx][ny] > graph[x][y]:
                        ans = min(ans, loop * 2 - 1)
    return ans


# 같은섬은 같은숫자로 (ex -1) 그룹핑한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            grouping(i, j)
            gid -= 1

print(get_distance())