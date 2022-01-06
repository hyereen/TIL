# -*- coding: utf-8 -*-
"""2606.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jIRtdD0ijmHh3XnqqcO9cvgaGnNbAhMB
"""

# 2606
# https://www.acmicpc.net/problem/2606

# dfs 함수 정의
def dfs(graph, n, visited):
  visited[n] = True
  
  for i in graph[n]:
    if not visited[i]:
      dfs(graph, i, visited)

node = int(input())
edge = int(input())

# 방문 표시 리스트 생성
visited = [False] * (node+1)

# 빈 2차원 리스트 생성
graph = []

for j in range(node+1):
  graph.append([])

# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍 입력받아 그래프를 2차원 리스트로 표현
for k in range(edge):
  n, e = map(int, input().split())
  graph[n].append(e)
  graph[e].append(n)

dfs(graph, 1, visited)

#  1번 컴퓨터를 제외하고 바이러스에 걸린 컴퓨터의 수 
print(visited.count(True) - 1)

