# n과m2

n, m = map(int, input().split())
graph = []
visited = [False] * (n + 1)

def dfs(s):
    if s == m:
        print(*graph)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            graph.append(i)
            dfs(s + 1)
            graph.pop()
            for j in range(i + 1, n + 1):
                visited[j] = False

dfs(0)