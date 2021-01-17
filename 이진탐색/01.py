#이진탐색으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    #해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

#이 문제는 특정한 수가 한 번이라도 등장했는지를 검사하면 되므로 set함수로 구현 가능
n = int(input())
array = set(map(int, input().split()))
x = list(map(int, input().split()))
m = int(input())

for i in x:
    if i in array:
        print('yes')
    else:
        print('no')
