def check(arr):
    l = len(arr) // 3
    for i in range(l, l * 2):
        for j in range(l, l * 2):
            if arr[i][j] != 1:
                return False
    return True

def rotation(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = key[i][j]
    return result
    
def solution(key, lock):
    #시작범위 지정
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            #3배크기의 lock에 기존 lock을 복사함
            new_lock[n + i][n + j] = lock[i][j]
    #회전
    for _ in range(4):
        key = rotation(key)
        #lock배열 전체 탐색
        for x in range(n * 2):
            for y in range(n * 2):
                #자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True
                #자물쇠에 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)