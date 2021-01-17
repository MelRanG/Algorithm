n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        print("j : ",j)
        print("arrayj: ", array[i])
        print("dj ",d[j - array[i]])
        d[j] = min(d[j], d[j - array[i]] + 1)

print(d[m])