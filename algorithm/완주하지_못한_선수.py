# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 아래 코드는 효율성 0점..
def solution(participant, completion):
    answer = ""
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = participant[0]
    return answer

# 효율성을 높이려면 해시 이용하기
def solution(participant, completion):
    answer = {}

    for i in participant:
        answer[i] = answer.get(i, 0) + 1

    # completion 에 포함되는 이름의 key 의 value 를 -1 한다.
    for j in completion:
        answer[j] -= 1

    # participant 에는 있지만 completion 에는 없는 이름만 value 가 1로 남는 것 리턴
    for k in answer:
        if answer[k]: return k