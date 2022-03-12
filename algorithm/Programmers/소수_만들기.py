# https://programmers.co.kr/learn/courses/30/lessons/12977
def solution(nums):
    answer = -1
    result = []

    length = len(nums)
    for i in range(0, length):
        first = nums[i]
        for j in range(i + 1, length):
            second = nums[j]
            for k in range(j + 1, length):
                third = nums[k]
                if is_prime_num(first + second + third):
                    # if first+second+third not in result: # 이걸 안해야 통과가 되네..왜지
                    result.append(first + second + third)

    answer = len(result)
    return answer

# 소수 판별 함수
def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # i로 나누어 떨어지면 소수가 아니므로 False 리턴

    return True  # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴