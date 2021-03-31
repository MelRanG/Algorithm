# n과m4
n, m = map(int, input().split())
graph = []
visited = [False] * (n + 1)

def dfs(s):
    if s == m:
        print(*graph)
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        graph.append(i)
        for j in range(i):
            visited[j] = True
        dfs(s + 1)
        for j in range(n + 1):
            visited[j] = False
        graph.pop()
dfs(0)
