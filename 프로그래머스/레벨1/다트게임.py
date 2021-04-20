def solution(dartResult):
    stack = []
    d = ['S','D','T','*','#']
    for i in dartResult:
        if not i in d:
            if len(stack) > 0 and type(stack[-1]) == int:
                j = stack.pop()
                i = str(j) + i
            stack.append(int(i))
        else:
            stack.append(i)
    answer = 0
    result = []
    for i in stack:

        if type(i) == int:
            if answer != 0:
                result.append(answer)
            answer = i
            continue
        if i == 'D':
            answer = answer * answer
        elif i == 'T':
            answer = answer ** 3
        if i == '*':
            if len(result) == 0:
                answer *= 2
            else:
                x = result.pop()
                result.append(x * 2)
                answer *= 2
        if i == '#':
            answer = -answer
    result.append(answer)

    return sum(result)


print(solution('1D2S#10S'))