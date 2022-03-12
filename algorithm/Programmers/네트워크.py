# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def bfs(links, start, visited):
  queue = deque([start])

  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in links[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

def solution(n, computers):
    answer = 0
    links = []
    for i in range(n):
      links.append([])
      for j in range(n):
        if (i != j) and (computers[i][j] == 1):
          links[i].append(j)

    visited = [False] * n

    for i in range(n):
      if visited[i] == False:
        bfs(links, i, visited)
        answer +=1


    return answer