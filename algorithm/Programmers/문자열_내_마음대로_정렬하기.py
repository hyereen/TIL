# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x)) # 정렬 첫번째 조건은 n번째 문자열, 그 다음 정렬 조건은 원소 그 자체(사전순)
    return answer