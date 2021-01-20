n = input()
stack = []
count = 0

for i in range(len(n)):
    if n[i] == '(':
        stack.append(i)
    else:
        if n[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)

