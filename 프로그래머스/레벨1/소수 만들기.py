def solution(nums):
    a = [False,False] + [True]*(3000-1)
    primes = []
    answer = 0
    for i in range(2, 3000):
        if a[i]:
            primes.append(i)
            for j in range(2*i, 3000, i):
                a[j] = False
    check = [False] * (len(nums)+1)
    
    for i in range(len(nums)):
        check[i] = True
        for j in range(i, len(nums)):
            if not check[j]:
                check[j] = True
                for k in range(j, len(nums)):
                    if not check[k]:
                        check[k] = True
                        x = nums[i] + nums[j] + nums[k]
                        if x in primes:
                            answer += 1
                        check[k] = False
                check[j] = False
        check[i] = False
    return answer