"""
게임개발 P120
"""
#n 세로 m 가로
n, m = map(int, input().split())
#방문한 위치를 저장하기 위한 맵 생성
d = [[0] * m for _ in range(n)]
#현재 캐릭터 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문처리

#전체 맵 정보 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0 #주변이 다 1이라 갈 수 있는 칸이 없는 경우(=한바퀴를 돌았기 때문에 turn_time = 4가됨)를 표시하기 위한 변수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동, array는 1일경우 바다이기때문에 0이어야함
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        y = ny
        x = nx
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면이 가본칸이거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        #뒤로 한칸
        nx = x - dx[direction]
        ny = y - dy[direction]

        #뒤쪽이 바다가 아닌 경우 (방문한 칸인 경우는 이동가능)
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0


#좌표를 배열로 입력하는 것과 한바퀴 돌았을 때 확인하는 변수를 선언할줄 알아야함