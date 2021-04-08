def binary(n):
    b = ""
    while n > 0:
        n, mod = divmod(n, 3)
        b += str(mod)
    return b

def solution(n):
    n = binary(n)
    return int(n, 3)

print(solution(45))

