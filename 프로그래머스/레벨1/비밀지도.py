def solution(n, arr1, arr2):
    arr = []
    for i, j in zip(arr1, arr2):
        s = ""
        x = format(i, 'b')
        y = format(j, 'b')
        if len(x) < n:
            x = '0' * (n - len(x)) + x
        if len(y) < n:
            y = '0' * (n - len(y)) + y
        for k in range(n):
            if x[k] == '0' and y[k] == '0':
                s += ' '
            else:
                s += '#'
        arr.append(s)
    return arr

a = [9, 20, 28, 18, 11]
b = [30, 1, 21, 17, 28]
print(solution(5, a, b))
