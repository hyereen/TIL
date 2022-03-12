# https://www.acmicpc.net/problem/13458

# 맨 처음에 풀었던 것 

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
super = 0

for i in range(len(A)):
  # 주감독관이 감독가능한 인원 수를 빼고, 주감독관 수를 카운트한다
  A[i] = A[i] - B
  super = super + 1
  m = A[i] // C
  A[i] = A[i] % C
  if A[i] != 0:
    m = m+1
  super = super +m

# 틀려서 다시 푼 것

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

super = 0

for i in range(len(A)):
  A[i] = A[i] - B
  super = super + 1
  if A[i] > 0:
    super = super + A[i] // C
    A[i] = A[i] % C
    if A[i] != 0:
      super = super+1

print(super)

"""
  if A[i] > 0:
이 조건이 없어서
틀렸습니다가 떴다
이 조건을 하지 않으면 A[i]이 B보다 작아서 음수가 나온 경우, A[i] // C의 값이 마이너스가 되서 감독관 수가 -명이 되어서 틀린 것!
"""

# 220313
n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().
           split())

supervisors = 0
for i in range(len(students)):
  temp = 0
  if students[i] <= b:
    supervisors +=1
  else:
    students[i] -= b
    supervisors +=1
    if students[i] <= c:
      supervisors +=1
    else:
      temp = students[i] // c
      students[i] -= c * temp
      if students[i] != 0:
        temp +=1
      supervisors +=temp

print(supervisors)