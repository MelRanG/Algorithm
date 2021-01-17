n = input()
column = int(ord(n[0])) - int(ord('a')) + 1
row = int(n[1])

steps = [
    (-2, -1), (-1, -2), (2, -1), (-2, 1), (2, 1), (1, 2),
        (1, -2), (-1, 2)
        ]
result = 0
for i in steps:
    next_column = column + i[1]
    next_row = row + i[0]
    if next_column > 0 and next_row > 0 and next_row < 9 and next_column < 9:
        result += 1
    
print(result)