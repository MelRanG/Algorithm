prices = [1, 2, 3, 2, 3]
stack = []

for i in range(len(prices)):
    result = 0
    for j in range(i+1, len(prices)):
        if prices[i] > prices[j]:
            stack.append(result)
            break
        if j == len(prices) - 1:
            stack.append(result)
            break
        result += 1
print(stack)