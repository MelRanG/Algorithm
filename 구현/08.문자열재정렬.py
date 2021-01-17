data = input()
result = []
value = 0

# 문자를 하나씩 확인함
for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        print(value)
result.sort()

# 숫자가 하나라도 존재하면 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))