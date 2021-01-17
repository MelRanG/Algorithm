#재귀로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

#반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

#원소의 개수와 찾고자 하는 문자 입력받기
n, target = list(map(int, input.split()))
#전체 원소 입력
array = list(map(int, input().split()))

#결과 출력
result = binary_search(array, target, 0, n-1)
if result = None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) #인덱스는 0번부터 시작하므로
