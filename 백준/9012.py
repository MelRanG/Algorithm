n = int(input())
for i in range(n):
    ps = input()
    count = 0
    index = True
    for i in range(len(ps)):
        if ps[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0 and index == True:
        print("YES")
    else:
        print("NO")
        index = True

#스택을 사용한 풀이
n = int(input())
def check(ps):
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print('NO')
            else:
                stack.pop()
    if not stack:
        print("YES")
        return
    else:
        print("NO")
        return

for _ in range(n):
    ps = input()
    check(ps)