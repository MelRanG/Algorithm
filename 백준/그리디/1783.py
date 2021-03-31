# 병든 나이트
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2)) # 홀수를 짝수로 만들기위해서 1을 더함
elif m < 7:
    print(min(4, m))
else:
    print(m - 7 + 5)