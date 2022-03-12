# -*- coding: utf-8 -*-
"""2644.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UzmgExtUQMCPrvlb7otAjq8zujuOCF1U
"""

# 2644
# https://www.acmicpc.net/problem/2644

# dfs로 시도 -> 예시는 맞는데 반례가 있어서 틀림
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = []
edge = []
chonsu = []

for i in range(n+1):
  graph.append([])

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n+1)

def dfs(graph, v, visited, edge, b):
    if v == b:
      global chonsu
      chonsu = edge.copy()
    else:
      visited[v] = True

      for i in graph[v]:
        if not visited[i]:
          edge.append(i)
          dfs(graph, i, visited, edge, b)


dfs(graph, a, visited, edge, b)

if not chonsu:
  print(-1)
else:
  print(len(chonsu))

# bfs
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = []

for i in range(n+1):
  graph.append([])

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [0] * (n+1)

def bfs(graph, start, visited):
   queue = deque([start])
   while queue:
     v = queue.popleft()
     for i in graph[v]:
       if not visited[i]:
         queue.append(i)
         visited[i] = visited[v] + 1 # 여기가 중요
         # 부모 노드에서 촌수 하나가 더 늘어난 것 



bfs(graph, a, visited)
 
if visited[b] == 0:
  print(-1)
else:
  print(visited[b])

visited = [0] * (n+1)
visited


