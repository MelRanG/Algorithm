#트리의 지름
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    path = list(map(int, input().split()))
    path_len = len(path)
    for i in range(1, path_len // 2):
        graph[path[0]].append([path[2*i-1], path[2*i]])

# 첫번째 DFS 결과
result1 = [0 for _ in range(n + 1)]

def dfs(start, graph, result):
    for n, d in graph[start]: # 노드랑 거리를 입력받음
        if result[n] == 0:
            result[n] = result[start] + d
            dfs(n, graph, result)

dfs(1, graph, result1) # 아무 노드에서 시작한다.
result1[1] = 0 # 루트노드가 정해져 있지않아 양방향으로 입력을 받는다.

tmpmax = 0 # 최대값
index = 0 # 최장경로

for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

# 최장경로 노드에서 다시 dfs를 통해 트리지름 구하기
result2 = [0 for _ in range(n + 1)]
dfs(index, graph, result2)
result2[index] = 0
print(max(result2))

