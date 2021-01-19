import sys

n = int(sys.stdin.readline())
stack = []

def check_stack(stack, y, n):
    if stack == 0:
        return y
    else:
        return n

for i in range(n):
    order = sys.stdin.readline().split()
    op = order[0]
    len_stack = len(stack)

    if op == 'push':
        stack.append(order[1])
    elif op == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif op == 'size':
        print(len_stack)
    elif op == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif op == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
        
