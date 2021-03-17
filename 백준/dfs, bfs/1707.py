# 이분 그래프

import sys
from collections import deque
input = sys.stdin.readline
k = int(input())

def bfs(start):
    bi[start] = 1
    q = deque([start])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if bi[i] == 0:
                #bi와 인접한 노드 모두 -bi
                bi[i] = -bi[a]
                q.append(i)
            else:
                #bi와 인접한 노드를 이미 방문했는데 값이 서로 같다면 False
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):
    check = True
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    bi = [0 for _ in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")