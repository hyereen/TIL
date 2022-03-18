from collections import deque

n, m = map(int, input().split())
graph = []
visited = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, cate):
    cnt = 0
    queue = deque()

    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        cnt +=1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n: # 조건, nx, ny가 m,n과의 맵핑 주의
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == cate:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return cnt

# 그래프 만드는거 주의!!
for i in range(m):
    temp = list(input())
    graph.append(temp)
    visited.append([0]*n)

w_temp = 0
w_squared = 0

b_temp = 0
b_squared = 0

for a in range(m):
    for b in range(n):
        if visited[a][b] == 0 and graph[a][b] == 'W':
            w_temp = bfs(a, b, 'W')
            w_squared = w_squared + w_temp * w_temp
            w_temp = 0
        elif visited[a][b] == 0 and graph[a][b] == 'B':
            b_temp = bfs(a, b, 'B')
            b_squared = b_squared + b_temp * b_temp
            b_temp = 0




print(w_squared, b_squared)

