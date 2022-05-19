# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=409

from collections import deque

N = int(input())

graph = []
for i in range(N):
    temp = list(map(int, input()))
    graph.append(temp)

visited = []
for i in range(N):
    visited.append([])
    for j in range(N):
        visited[i].append(0)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt_list = []


def bfs(x, y):  # 시작점
    cnt = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt += 1

    while q:
        cx, cy = q.pop()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:  # 이 조건이 중요!
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    cnt_list.append(cnt)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:  # 이 조건이 중요!
            bfs(i, j)

print(len(cnt_list))
cnt_list = sorted(cnt_list)  # 각 블록에 속하는 장애물의 수를 오름차순으로 정렬하여
for i in cnt_list:
    print(i)
