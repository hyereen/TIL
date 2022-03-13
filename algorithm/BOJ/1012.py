from collections import deque

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = []

    # 배추밭(그래프) 만들기
    for a in range(m+1):
        graph.append([])
        for b in range(n+1):
            graph[a].append(0)

    # 배추 위치 표시
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    answer = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(x, y):
        graph[x][y] = 0
        queue = deque()
        queue.append((x,y))

        while queue:
            w, z = queue.popleft()
            graph[w][z] = 0

            for i in range(4):
                cx = w + dx[i]
                cy = z + dy[i]

                if cx >= 0 or cx <= m or cy >= 0 or cy <= n:
                    pass
                if graph[cx][cy] == 1:
                    graph[cx][cy] = 0
                    queue.append((cx,cy))

    for a in range(m + 1):
        for b in range(n + 1):
            if graph[a][b] == 1:
                bfs(a, b)
                answer += 1

    print(answer)