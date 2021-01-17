from itertools import combinations

n, m = map(int, input().split())

chicken, home = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i,j))

#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    #모든 집에 대해서
    for hx, hy in home:
        #가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)


"""
내가 푼 코드
from itertools import combinations

n, m = map(int, input().split())

chicken, home = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i,j))

#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))
# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = []
    for i in home:
        answer = []
        for j in candidate:
            answer.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        result.append(min(answer))
    return sum(result)

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)

"""
