from collections import deque
def solution(skill, skill_trees):
    arr = []
    count = 0
    for i in skill:
        arr.append(i)

    for sen in skill_trees:
        temp = ""
        for word in sen:
            if word in skill:
                temp += word
        if temp == skill[0:len(temp)]:
            count += 1
    print(count)

skill = "CBD"	
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)
