# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

def solution(operations):
    answer = [0, 0]
    lst = []

    for o in operations:
        al, num = o.split()
        num = int(num)
        if al == 'I':
            lst.append(num)
        else:
            if len(lst) == 0:
                continue
            if num == 1:
                max_num = max(lst)
                lst.remove(max_num)
            else:
                min_num = min(lst)
                lst.remove(min_num)
    if len(lst) == 0:
        return answer
    else:
        answer[0] = max(lst)
        answer[1] = min(lst)
        return answer

