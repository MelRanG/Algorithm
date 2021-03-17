#DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(v, graph, visited):
    q = deque([v])
    visited[v] = False
    while q:
        s = q.popleft()
        print(s, end=' ')
        for i in graph[s]:
            if not visited[i]:              
                visited[i] = True
                q.append(i)

dfs(v, graph, visited)
print(visited)
bfs(v, graph, visited)