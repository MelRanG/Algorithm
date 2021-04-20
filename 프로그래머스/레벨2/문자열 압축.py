from collections import deque

def solution(s):
    
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        l = ""
        count = 1
        start = s[:i]

        for j in range(i, len(s), i):
            if start == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    l += str(count) + start 
                else: l += start
                start = s[j:j+i]
                count = 1
        l += str(count) + start if count >= 2 else start    
        answer = min(answer, len(l)) 
    return answer
print(solution("aabbaccc"))