def solution(array, commands):
    result = []
    for i, j, k in commands:
        new_arr = array[i-1:j]
        new_arr.sort()
        result.append(new_arr[k-1])
    return result
a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a, c))