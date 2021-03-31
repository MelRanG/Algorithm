# 트리의 지름
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append([c, d])
    graph[c].append([p, d])

# 가장 값이 큰 노드 찾기
result1 = [0 for _ in range(n + 1)]

def dfs(start, graph, result):
    for n, d in graph[start]:
        
        if result[n] == 0:
            result[n] = result[start] + d
            dfs(n, graph, result)

dfs(1, graph, result1)

result1[1] = 0
tmpmax = 0
index = 0

for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

result2 = [0 for _ in range(n + 1)]

dfs(index, graph, result2)
result2[index] = 0

print(max(result2))
