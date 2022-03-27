
from collections import deque 
def bfs(i, visited): 
  q = deque() 
  q.append(i) 
  visited[i] = True 
  
  while q: 
    x = q.popleft() 
    if x == K: 
      return line[x] 
      
    for nx in (x*2, x-1, x+1): 
      if 0 <= nx <= 100000 and not visited[nx]: 
        if nx == x*2: 
          line[nx] = line[x] 
        else: 
          line[nx] = line[x] + 1 
          
        q.append(nx) 
        visited[nx] = True 
      
N, K = map(int, input().split()) 
line = [0] * 100001 
visited = [False] * 100001 
print(bfs(N, visited))


# ======================================================
# 220327 또 다른 방법

from collections import deque

n, k = map(int, input().split()) # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()

q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
  print(q)
  s = q.popleft()
  if s == k:
    print(visited[s])
    break
  if 0 <= s-1 < 100001 and visited[s-1] == -1:
    visited[s-1] = visited[s] + 1
    q.append(s-1)
  if 0 < s*2 < 100001 and visited[s*2] == -1:
    visited[s*2] = visited[s]
    q.appendleft(s*2) # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
  if 0 <= s+1 < 100001 and visited[s+1] == -1:
    visited[s+1] = visited[s] + 1
    q.append(s+1)


