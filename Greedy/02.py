"""
5 8 3
2 4 5 4 6
    큰 수의 법칙 P92
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]

i = 0
result = 0
for v in range(m):
    if (i + 1) % k == 0:
        result += second
        print("%부분: ",result)
    else:    
        result += first
        print("result: ", result)
        print("i: ",i)
    i+=1
print(result)