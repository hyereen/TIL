import heapq
import sys

input =  sys.stdin.readline # 시간초과 없애기
heap = []

n = int(input())

for i in range(n):
  x = int(input())
  if x != 0:
    heapq.heappush(heap, (abs(x), x)) # (우선순위, 값)
  elif x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap)[1])