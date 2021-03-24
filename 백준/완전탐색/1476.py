# 날짜 계산
e, s, m = map(int, input().split())
ec, sc, mc = 0, 0, 0
count = 0
while True:
    if ec > 15:
        ec = 1
    if sc > 28:
        sc = 1
    if mc > 19:
        mc = 1
    
    if ec == e and sc == s and mc == m:
        break
    ec += 1
    sc += 1
    mc += 1
    count += 1

print(count)
