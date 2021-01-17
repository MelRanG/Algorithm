s = "aaaabbabbabb"

answer = len(s)
#1개 단위부터 압축 단위를 늘려가며 확인
for step in range(1, len(s) // 2 + 1): #절반이상 확인할 경우 반복이 되지 않으므로(x2할시 초과함) 절반까지만 확인함.
    result = ""
    prev = s[0:step] #0부터 압축단위값까지가 prev값
    count = 1
    #단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
        #이전 상태와 동일하다면 압축 횟수(count) 증가
        if prev == s[j:j + step]:
            count += 1
        #다른 문자열이 나왔다면(더 이상 압축 불가능)
        else:
            result += str(count) + prev if count >= 2 else prev
            prev = s[j:j + step] #상태 다시 초기화
            count = 1
    #남아 있는 문자열에 대해서 처리
    result += str(count) + prev if count >= 2 else prev
    #만든 것 중에 가장 짧은 것이 정답
    answer = min(answer, len(result))
print(answer)