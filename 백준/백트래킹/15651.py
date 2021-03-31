# n과m3
n, m = map(int, input().split())
graph = []

def dfs(s):
    if m == s:
        print(*graph)
        return
    for i in range(1, n + 1):
        graph.append(i)
        dfs(s + 1)
        graph.pop()
dfs(0)
