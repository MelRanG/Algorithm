from collections import Counter

def solution(nums):
    n = len(nums) // 2

    if len(Counter(nums)) < n:
        return len(Counter(nums))
    else: 
        return n 

print(solution([3,3,3,2,2,2]))