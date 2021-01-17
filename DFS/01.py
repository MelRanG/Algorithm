def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    #처음의 경우 graph[v] = v가 1이므로 0번다음의 1번째 배열인 2,3,8중 가장 값이 적은 배열부터 들어감
    for i in graph[v]:
        if not visited[i]:
            print("graph: ", graph[v])
            print("i: ", i)
            dfs(graph, i, visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)