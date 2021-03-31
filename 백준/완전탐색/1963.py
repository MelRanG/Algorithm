# 소수 경로
from collections import deque
import math, copy

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def bfs(a, b):
    # 한자리 값을 다루기 위해 int 를 string으로 변경
    q = deque([[list(str(a)), 0]])
    visited = {a}

    while True:
        val, cnt = q.popleft()
        if int("".join(map(str, val))) == b:
            return cnt
        else:
            for i in range(4): # 각 자리 변환
                for j in range(10): # 변환 값
                    if val[i] == str(j): # 자리수가 같은 경우
                        continue
                    else:
                        temp = copy.deepcopy(val)
                        temp[i] = str(j)
                        temp_value = int("".join(map(str, temp)))
                        if temp_value not in visited and temp_value >= 1000 and prime_check(temp_value):
                            visited.add(temp_value)
                            q.append([temp, cnt + 1])


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(bfs(a, b))