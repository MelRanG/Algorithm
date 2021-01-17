n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
#1번부터 시작할지 2번부터 시작할지 정하기 위해 두 값 비교
d[1] = max(array[0], array[1])
for i in range(2, n):
# 전값, 전전값 중 큰 값과 현재값 더하기
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])