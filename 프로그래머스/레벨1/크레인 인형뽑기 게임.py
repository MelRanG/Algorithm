def solution(board, moves):
    answer = 0
    stack = []

    for j in moves:
        for i in range(len(board)):
            if not board[i][j-1] == 0:
                stack.append(board[i][j-1])
                board[i][j-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break
    return answer

b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b, m))
