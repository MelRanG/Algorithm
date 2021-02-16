#골드바흐 추측
import sys
r = 1000000
a = [True for _ in range(r)]

for i in range(2, int(r**0.6)):
    if a[i]:
        for j in range(2*i, r, i):
            a[j] = False

while(True):
    n = int(sys.stdin.readline)
    if n == 0 :
        break
    for i in range(3, r):
        if a[i] == True:
            if a[n - i] == True:
                print("{} = {} + {}".format(n, i, n - i))
                break
