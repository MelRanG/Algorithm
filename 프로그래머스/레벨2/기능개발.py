def solution(progresses, speeds):
    progresses = [x+y for x, y in zip(progresses, speeds)]
    result = []
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        count = 0
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break
        if count:
            result.append(count)
    return result
p = [93, 30, 55]
s = [1, 30, 5]

print(solution(p,s))