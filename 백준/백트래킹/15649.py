# n과m 1

n, m = map(int, input().split())
check = [False] * (n + 1)
graph = []

def dfs(s):
    if s == m:
        print(' '.join(map(str, graph)))
        return
    
    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        graph.append(i)
        dfs(s + 1)
        graph.pop()
        check[i] = False
dfs(0)


    

