# 외판원 순회2
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n)
minCost = 1e9

def dfs(v, start, cost):
    global minCost
    if start == v and visited.count(False) == 0:
        minCost = min(minCost, cost)

    for i in range(n):
        if not graph[v][i] == 0 and not visited[i]: # 그래프가 0이 아니고 방문하지 않았다면
            visited[i] = True # 방문처리
            dfs(i, start, cost+graph[v][i]) # graph가 2차원 배열이니 현재 체크한 값을 넘김으로서 다음 방향 진행
            visited[i] = False # 한 번 다 돌고나서 다음 i번 차례

dfs(0, 0, 0)
print(minCost)