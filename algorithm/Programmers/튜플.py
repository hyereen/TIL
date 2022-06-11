# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

def solution(s):
    answer = []
    # 입력이 문자열이므로 양쪽 중괄호 지우기
    s = s.strip("{{}}")

    # 중간에 중괄호를 이용해 원소 쪼개기
    s = s.split("},{")

    # 숫자로 만들어서 리스트에 넣기
    s_list = []
    for i in s:
        temp = list(map(int, i.split(",")))
        s_list.append(temp)

    # 원소를 원소길이 순서대로 정렬
    s_list = sorted(s_list, key=lambda x: len(x))

    # 순서대로 넣으면서 이미 존재하는 숫자는 넣지 않기
    for s in s_list:
        for i in s:
            if i not in answer:
                answer.append(i)

    return answer