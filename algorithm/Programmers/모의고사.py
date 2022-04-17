# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

# 정답
def solution(answers):
    answer = []
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thi = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    fir_ans = []
    sec_ans = []
    thi_ans = []

    for n in range(len(answers)):
        f = n % 5

        if fir[f] == answers[n]:
            scores[0] += 1
        s = n % 8
        if sec[s] == answers[n]:
            scores[1] += 1
        t = n % 10
        if thi[t] == answers[n]:
            scores[2] += 1

    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i + 1)

    answer.sort()
    return answer