# https://programmers.co.kr/learn/courses/30/lessons/12899

from itertools import product
import re

# 맨 처음 풀이: 정확성 테스트 통과, 효율성 테스트 실패(시간초과)
# def solution(N):
#     list_cnt = 0
#     n = 1
#     while True:
#         for i in product([1,2,4], repeat=n):
#             list_cnt += 1
#             if list_cnt == N:
#                 return re.sub(r'[^0-9]', '', str(i))
#         n += 1

# 정답 풀이
def solution(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer