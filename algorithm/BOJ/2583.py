# -*- coding: utf-8 -*-
"""2583.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17nqmm2vwglBSom1VC_dbam3hVt0QfxfJ
"""

# 2583
# https://www.acmicpc.net/problem/2583

# dfs
import sys
sys.setrecursionlimit(10**6) # 런타임 에러 (RecursionError) 해결

m, n, k = map(int, input().split())

graph = []

# 빈 행렬 만들기
for i in range(m): # m이 세로 
  graph.append([])
  for j in range(n): # n이 가로
    graph[i].append(0)

# 행렬 색칠하기
def coloring(x, y, z, w):
  global m
  for i in range(y, w): # 주의
    for j in range(x, z): # 주의
      graph[i][j] = 1


# 직사각형 입력받기
for a in range(k):
  x, y, z, w = map(int, input().split())
  coloring(x, y, z, w)

# 그래프 출력 -> 위아래로 뒤집혀서 나옴
#for i in range(m):
#  print(graph[i])

uncolor_cnt = 0
uncolor_list = []

def dfs(x, y):
  global m, n, uncolor_cnt
  if x <=-1 or x>=m or y <=-1 or y >=n: # 주의
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    uncolor_cnt += 1
    return True
  return False

ans = 0
for i in range(m): # m이 세로 
  for j in range(n): # n이 가로
    if dfs(i, j) == True:
      ans +=1
      uncolor_list.append(uncolor_cnt)
      uncolor_cnt = 0

uncolor_list.sort()

print(ans)
for i in uncolor_list:
  print(i, end=' ')

# bfs
from collections import deque

m, n, k = map(int, input().split())

graph = []

# 빈 행렬 만들기
for i in range(m): # m이 세로 
  graph.append([])
  for j in range(n): # n이 가로
    graph[i].append(0)

# 행렬 색칠하기
def coloring(x, y, z, w):
  global m
  for i in range(y, w): # 주의
    for j in range(x, z): # 주의
      graph[i][j] = 1


# 직사각형 입력받기
for a in range(k):
  x, y, z, w = map(int, input().split())
  coloring(x, y, z, w)

# 그래프 출력 -> 위아래로 뒤집혀서 나옴
#for i in range(m):
#  print(graph[i])

ans=0
uncolor_cnt = 0
uncolor_list = []

dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

def bfs(x, y):
  global uncolor_cnt
  graph[x][y] = 1
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x, y = queue.popleft()
    uncolor_cnt +=1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or nx>=m or ny<0 or ny>=n:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        queue.append((nx,ny))

for i in range(m): # m이 세로 
  for j in range(n): 
    if graph[i][j] == 0:
      bfs(i, j)
      uncolor_list.append(uncolor_cnt)
      uncolor_cnt = 0
      ans +=1


uncolor_list.sort()

print(ans)
for i in uncolor_list:
  print(i, end=' ')