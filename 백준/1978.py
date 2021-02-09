#소수 찾기
n = int(input())
num_list = map(int, input().split())
num = 0
for i in num_list:
    count = 0
    if(i == 1):
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        num += 1
print(num)