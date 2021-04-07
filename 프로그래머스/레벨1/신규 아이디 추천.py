import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z-_.]', '', new_id)
    new_id = re.sub('[.]{2,999}','.',new_id)
    # 4단계
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5단계
    if not new_id:
        new_id = 'a'
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        print(len(new_id))
        print(new_id)
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    while len(new_id) < 3:
        s = new_id[-1]
        new_id = new_id + s

    return new_id
n = "abcdefghijklmn.p"
print(solution(n))
