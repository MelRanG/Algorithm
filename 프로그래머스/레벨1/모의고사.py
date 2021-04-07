def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i in range(len(answers)):
        x = i
        if len(answers) > 4:
            x = i % 5            
        if answers[i] == a[x]:
            count[0] += 1
        if len(answers) > 7:
            x = i % 8   
        if answers[i] == b[x]:
            count[1] += 1
        if len(answers) > 9:
            x = i % 10   
        if answers[i] == c[x]:
            count[2] += 1

    answer = []
    m = max(count)
    for i in range(len(count)):
        if m == count[i]:
            answer.append(i+1)
    return answer
n = [1,2,3,4,5]
print(solution(n))
