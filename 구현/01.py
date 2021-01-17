n = int(input())
move = input().split()
x,y = 1,1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(result)):
        if i == result[j]:
            move_x = dx[j] + x
            move_y = dy[j] + y
    if move_x < 1 or move_y < 1 or move_x > n or move_y > n:
        continue
    x = move_x
    y = move_y    
print(x, y)