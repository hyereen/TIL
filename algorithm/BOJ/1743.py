# -*- coding: utf-8 -*-
"""1743.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18L04A10kKDkhYwRgVts0SmZpIDUWQ6r6
"""

from collections import deque

n, m, k = map(int, input().split())

graph = []
for i in range(n):
  graph.append([])
  for j in range(m):
    graph[i].append(0)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  cnt = 0
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  cnt += 1

  while queue:
    cx, cy = queue.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if nx <0 or ny <0 or nx >= n or ny >=m: # 주의! 가로길이는 m, 세로길이는 n
        continue
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0
        cnt += 1
  
  return cnt

max_size = 1
for i in range(k):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1: # 주의! 이 조건 빼먹지 말기
      size = bfs(i, j)
      if max_size < size:
        max_size = size

print(max_size)

2 max_size

graph

0 0
0 1
1 0
1 1
2 1