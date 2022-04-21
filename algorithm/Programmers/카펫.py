

# 정답
def solution(brown, yellow):
    answer = []
    num = brown + yellow

    for i in range(1, num):
        if num % i == 0: 전체 합
            b = i
            y = num // i
            if (b >= y) and ((b - 2) * (y - 2) == yellow):
                answer = [b, y]
    return answer