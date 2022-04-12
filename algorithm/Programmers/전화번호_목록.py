# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

# 맨 처음 풀이
# 실패: 테케 8, 9, 19
# 효율성 테스트: 시간초과 1, 2, 3, 4
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if phone_book[i] == j[:len(phone_book[i])]:
                answer = False
                break
    return answer

# 참고: https://programmers.co.kr/questions/17360
# 테케 8, 9, 19 성공
def solution(phone_book):
    answer = True
    phone_book.sort(key=len) # 요소 길이 순서대로 정렬 추가
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if phone_book[i] == j[:len(phone_book[i])]:
                answer = False
                break
    return answer

# 통과
def solution(phone_book):
    answer = True
    phone_book.sort() # 길이 순서대로 정렬이 아니라 그냥 오름차순으로 해야 길이가 짧은 접두어를 가진 수가 더 앞에 오게 됨
    for i in range(len(phone_book)-1): # i와 i+1를 비교하므로 i번째에서 index error 날까봐 -1해준다
        if len(phone_book[i]) < len(phone_book[i+1]): # 만약 i가 i+1번째보다 길이가 큰 경우, 아래 if문에서 slicing이 안되므로 이 조건이 필요함
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer