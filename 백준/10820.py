import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    result = [0, 0, 0, 0]
    if not line:
        break
    for i in line:
        if i.islower() == True:
            result[0] += 1
        if i.isupper() == True:
            result[1] += 1
        if i.isdigit() == True:
            result[2] += 1
        if i.isspace() == True:
            result[3] += 1
    print(result[0], result[1], result[2], result[3])