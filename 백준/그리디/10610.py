# 30
# 30의 배수는 1의자리에 0이있고 각 자리수의 합이 3이되면 된다.
n = input()
n = sorted(n, reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))