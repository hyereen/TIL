# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

# 맨 처음 풀이
# 통과: 테케 2, 15, 16, 17, 20, 21, 27
# 실패: 나머지..다..

def solution(clothes):
    answer = 0
    kinds = {}
    for i in clothes:
        kinds[i[1]] = []
    for i in clothes:
        kinds[i[1]] += [i[0]]
    if len(kinds.keys()) > 1:
        for i in kinds.keys():
            for j in kinds[i]:
                answer = answer + 1
    temp = 1
    for i in kinds.values():
        #print(len(i))
        temp = temp * len(i)
    answer += temp
    #answer = answer + len(list(kinds.keys()))
    return answer


# 정답

def solution(clothes):
    answer = 0
    kinds = {}
    for i in clothes: # 해시 틀 만들기
        kinds[i[1]] = []
    for i in clothes: # 각 카테고리에 해당하는 옷들 넣기
        kinds[i[1]] += [i[0]]
    lst = [] # 종류별 옷의 개수를 저장할 리스트
    for i in kinds.values(): # 종류별로
        lst.append(len(i)+1) # 옷의 개수를 세고, +1 더해줌(그 종류의 옷을 안입는 경우를 세기 위해)
    answer = 1
    for i in lst:
        answer = answer * i # 다 곱해서 경우의수를 구해줌
    answer = answer - 1 # 아무것도 다 안입는 경우 삭제
    return answer