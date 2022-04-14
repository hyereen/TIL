# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

# 맨 처음 풀이
# 실패: 테케 11

def solution(citations):
    answer = 0
    n = max(citations)
    citations.sort(reverse=True)
    for i in range(n, 0, -1):
        h = i
        above = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                above = above + 1
        print(h, above)
        if above >= h:
            answer = h
            break
    return answer

# 참고: https://programmers.co.kr/questions/25447
def solution(citations):
    answer = 0
    n = max(citations)
    citations.sort(reverse=True)
    for h in range(n, -1, -1):
        above = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                above = above + 1
        if above >= h: # 기준(h)보다 기준보다 인용횟수가 많은 논문 수(above)가 더 많아야 하므로
            answer = h
            break # 내림차순 정렬해서 맨 처음꺼가 가장 큰 수가 됨
    return answer