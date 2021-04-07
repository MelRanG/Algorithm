def solution(n, lost, reserve):
    realLost = set(lost)-set(reserve)
    realReserve = set(reserve) - set(lost)
    for i in realReserve:
        if i-1 in realLost:
            realLost.remove(i-1)
        elif i+1 in realLost:
            realLost.remove(i+1)
    return n - len(realLost)


l = [2,4]
n = 5
r = [1,3,5]
print(solution(n, l, r))