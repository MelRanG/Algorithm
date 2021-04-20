def solution(numbers, hand):
    arr = [[3*i + j for j in range(1, 4)] for i in range(4)]
    right = (3,2)
    left = (3,0)
    result = []

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11

        for y in range(len(arr)):
            for x in range(len(arr[y])):
                if numbers[i] == arr[y][x]:
                    if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
                        result.append('L')
                        left = (y,x)
                        #print(left)
                        break
                    elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
                        result.append('R')
                        right = (y,x)
                        #print(right)
                        break
                    else:
                        l = abs(y - left[0]) + abs(x - left[1])
                        r = abs(y - right[0]) + abs(x - right[1])
                        if l == r:
                            if hand == "right":
                                result.append("R")
                                right = (y,x)
                            else:
                                result.append("L")
                                left = (y,x)
                            break
                        elif l > r:
                            result.append("R")
                            right = (y,x)
                        elif l < r:
                            result.append("L")
                            left = (y,x)

            
            # 값이 들어갔다면
            if len(result) == i+1:
                break

    return ''.join(result)
print(solution([0,0,0,0],"left"))
