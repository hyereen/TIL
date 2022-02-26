# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
  answer = 0
  while True:
    max_num = max(priorities) # 리스트에서 가장 큰 수
    for i in range(len(priorities)):
      if max_num == priorities[i]: # 최댓값과 i와 일치하면
        answer += 1 # 프린트한 것으로 간주하고 프린터의 순서를 의미하는 answer에 1 더함
        print(i, answer)
        priorities[i] = 0 # 프린트한 것은 최댓값 구하는 거에 영향을 안주도록 0으로 표시
        max_num = max(priorities) # 최댓값 프린트했으니까 다시 나머지 중에서 최댓값을 구함
        print(priorities)
        if i == location:
          return answer