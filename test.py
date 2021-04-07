import copy


def solution(rows, columns, queries):
    answer = []
    graph = [[]]
    count = 0
    
    for i in range(1, (rows * columns) + 1):
        graph[count].append(i)
        if i == rows * columns:
            break
        if i % rows == 0:
            graph.append([])
            count += 1

    for i in queries:
        y1, x1 = i[0], i[1]
        y2, x2 = i[2], i[3]
        for r in range(y1-1, y2):
            for c in range(x1-1, x2):
                if r == y1-1 and c == x2:
                    ret[r+1][c] = graph[r][c]
                elif r == 
                ret[r][c+1] = graph[r][c]


def rotation(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = key[i][j]
    return result


        graph[y1 - 1][x1 - 1]
        x2 - x1
        y2 - y1
    return graph
r = 6
c = 6
q = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(r, c, q))