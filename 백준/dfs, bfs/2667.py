# 단지번호 붙이기
n = int(input())
graph = []
visited = []
for i in range(n):
    graph.append(list(map(int, input())))
    visited.append([False] * n)

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == True:
        return False
    if graph[x][y] == 1:
        visited[x][y] = True
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return count
    
result = []
for i in range(n):
    for j in range(n):
        count = 0
        if visited[i][j] == False and graph[i][j] == 1:
            result.append(dfs(i, j))
print(len(result))
for i in sorted(result):
    print(i)