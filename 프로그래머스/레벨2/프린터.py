from collections import deque
import copy

def solution(priorities, location):
    count = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])

    while q:
        v, n = q.popleft()
        v_list = [i for i , j in q]
        if q and v < max(v_list):
            q.append((v, n))
        else:
            count += 1
            if location == n:
                return count

     