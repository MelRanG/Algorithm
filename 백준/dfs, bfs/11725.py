import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s,e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

parents = [0 for _ in range(n + 1)]

def dfs(start, tree, parents):
    for i in tree[start]: #연결된 노드 모두 탐색
        if parents[i] == 0: # 방문한 적이 없다면
            parents[i] = start # 부모노드 저장
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, n + 1):
    print(parents[i])
