def solution(p, c):
    p.sort()
    c.sort()
    for i, j in zip(p, c):
        if i != j:
            return i
    return p[-1]