# -*- coding: utf-8 -*-
"""7576.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m8D6wPrre0huwqeopSGziVrGz1vlrbuK
"""

# 7576
# https://www.acmicpc.net/problem/7576

from collections import deque
m, n = map(int, input().split())

# 2차원 그래프 만들기
graph = []

# bfs
for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
  queue = deque()
  queue.extend(start)


  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위 똑바로 써주기
        continue
      if graph[nx][ny] == -1: # 토마토 없는 경우
        continue
      if graph[nx][ny] > graph[x][y] + 1: # 1이 여러개인 경우, 더 가까운 1이 있는 경우, 작은 수로 업데이트 해줌
        graph[nx][ny] = graph[x][y] + 1
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

start = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      start.append((i,j))

bfs(start)

# 최댓값 구하기
max_day = graph[0][0]

for i in range(n):
  for j in range(m):
    if graph[i][j] > max_day:
      max_day = graph[i][j]

untomato = False

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      untomato = True
      break

if untomato == True:
  print(-1)
else:
  print(max_day-1)