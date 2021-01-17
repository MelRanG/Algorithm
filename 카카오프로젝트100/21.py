arr = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
result = []
for i in range(0,len(command)-1):
    answer.append(arr[command[i][0]-1:command[i][1]])
    #2중리스트기 때문에 answer[i]로 각 리스트 지정
    answer[i].sort()
    #각 리스트마다 
    result.append(answer[i][command[i][2]])
print(result)