from math import ceil

def solution(progresses, speeds):
    answer = []

    #각 progresses당 남은날짜 표기 7,8번라인 같은 의미
    days = [ceil((100-p) / s) for p, s in zip(progresses, speeds)]
    days = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])),
                    range(len(progresses))))
    max_days = days[0]
    count = 1
    #i+1값을 미리검사해야하지만 index out of range에러 때문에 0번값을 사전에 넣고 1번부터 계산함
    #이방법이 안떠오를경우 try catch활용가능
    for i in range(1, len(days)):
        
        #첫 번째 작업이 끝날동안 두번 째 또는 그 이상의 작업이 끝나지 않았다면 1번째 작업만 추출
        if max_days < days[i]:
            answer.append(count)
            max_days = days[i]
            count = 0
        
        #첫 번째와 두 번째 또는 그 이상의 작업이 같이 끝낫다면 그 수만큼 count 증가

        count += 1
    if count > 0:
        answer.append(count)
    return answer

pro = [93, 30, 55]
spe = [1, 30, 5]
result = solution(pro, spe)
print(result)