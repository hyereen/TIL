# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
      sec = 0 # 가격이 떨어지지 않는 시간을 카운트할 변수
      for j in range(i+1, len(prices)): # 현재 값을 제외하고 나머지 주식 가격들을 반복하면서
          if prices[i] <= prices[j]: # 현재 가격과 크거나 같은 경우는
              sec +=1 # 가격이 떨어지지 않을 시간을 1초씩 더해주고
          else: # 가격이 떨어지는 경우는
              sec +=1 # 1초동안은 유지되었으므로 1을 더해주고
              break # 반복을 멈추고
      answer.append(sec) # 결과 리스트에 저장해준다 
    return answer