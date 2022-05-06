# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=407

import sys

K, P, N = map(int, input().split())

for n in range(N):
    K = K * P
    K = K % 1000000007

print(K)