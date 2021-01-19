n, k = map(int, input().split())
result = list(map(int, input().split()))
result.sort()
print(result[k-1])