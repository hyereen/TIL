# https://softeer.ai/practice/info.do?idx=1&eid=389

import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# 구간 수만큼 반복한다.
for i in range(k):
    a, b = list(map(int, sys.stdin.readline().split()))

    # 구간의 크기만큼 나눠준다.
    # sum함수를 통해 구간의 모든 수를 더한다.
    slash = b - a + 1
    average = sum(s[a - 1:b]) / slash

    # 소수 셋째 자리에서 반올림한다.
    print("%0.2f" % average)