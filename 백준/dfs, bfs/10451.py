#순열 사이클
import sys
sys.setrecursionlimit(10000)

n = int(input())

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)
        return True


for i in range(n):
    m = int(input())
    k = list(map(int, input().split()))
    graph = [[] for _ in range(m + 1)]
    visited = [False] * (m + 1)
    count = 0
    
    for j in range(m):
        graph[j + 1].append(k[j])
    for i in range(1, m + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
    