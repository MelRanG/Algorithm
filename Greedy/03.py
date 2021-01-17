"""
    숫자 카드 게임 P97
"""

n, m = map(int, input().split())

result = 0

for i in range (n):
    k = list(map(int, input().split()))
    data = min(k)
    result = max(result, data)       
print(result)