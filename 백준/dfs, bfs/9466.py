# 텀 프로젝트
import sys
sys.setrecursionlimit(111111)

def dfs(v):
    global result
    visited[v] = True
    term.append(v)
    num = s[v]

    if visited[num]:
        if num in term:
            result += term[term.index(num):] # 사이클 되는 구간 부터만 팀을 구성
        return
    else:
        dfs(num)
    

for i in range(int(input())):
    k = int(input())
    s = [0] + list(map(int, input().split()))
    visited = [True] + [False] * k
    result = []

    for i in range(1, k + 1):
        if not visited[i]:
            term = []
            dfs(i)
    print(k - len(result))

