def solution(number, k):
    n = ""
    count = 0
    number_length = len(number)
    visited = [False] * number_length
    index = 0
    while True:
        if count == number_length - k:
            break
        x = '0'
        check = False
        for i in range(index, k + 1 + count):
            if number[i] == '9' and visited[i] == False:
                n += number[i]
                visited[i] = True
                check = True
                index = i
                break
            if int(x) < int(number[i]) and not visited[i]:
                x = number[i]
                index = i
        visited[index] = True
        if not check:
            n += x
        check = False
        count += 1
    return n
print(solution("1924", 2))

