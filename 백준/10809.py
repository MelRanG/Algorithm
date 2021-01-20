n = input()
result = [-1] * 26
for i in range(len(n)):
    num = ord(n[i]) - 97
    if result[num] == -1:
        result[num] = i
    
for i in result:
    print(i, end=' ')