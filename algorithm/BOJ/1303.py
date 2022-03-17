from collections import deque

n, m = map(int, input().split())
graph = []
visited = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, cate):
    queue = deque()

    visited[x][y] = cate
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 'W':
                visited[nx][ny] = cate
                queue.append((nx, ny))


for i in range(m):
    graph.append([])
    visited.append([])
    temp = input()
    for j in temp:
        graph[i].append(j)
        visited[i].append(0)

w_temp = 0
w_squared = 0
cate = 0
for a in range(m):
    for b in range(n):
        if visited[a][b] == 0 and graph[a][b] == 'W':
            cate = cate + 1
            bfs(a, b, cate)
            w_temp = max(max(visited))
            w_squared = w_squared + w_temp * w_temp
            w_temp = 0



print(visited)
print(w_squared)
print(w_temp)

