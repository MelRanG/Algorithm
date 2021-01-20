n = input()
result = [0] * 26
for i in n:
    result[ord(i) - 97] += 1
for i in result:
    print(i, end=' ')
