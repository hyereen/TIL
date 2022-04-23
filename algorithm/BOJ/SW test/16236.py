from collections import deque
n = int(input())

graph = []
queue = deque()

# 좌표 그래프를 입력받으면서 아기상어의 위치를 큐에 넣어주고(시작점), 그 시작점은 0으로 만들어서 진행에 방해물이 안되도록 만들어준다
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append([])
    for j in range(n):
        graph[i].append(temp[j])
        if graph[i][j] == 9:
            queue.append((i,j, 0))
            graph[i][j] = 0

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 상태에서 먹을 수 있는 물고기의 위치와 그 거리를 구하기
def get_fishes(cgraph, x, y, s_size):
    # 갔던 곳을 또 가면 그래프를 뱅뱅도니까 방문체크를 위한 visited 2차원 배열을 만들어준다
    visited = []
    for i in range(n):
        visited.append([])
        for j in range(n):
            visited[i].append(0)
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    fish_list = [] # 먹을 수 있는 물고기의 x,y좌표와 거리를 저장해둘 리스트
    shark_size = s_size # 상어의 크기에 따라 먹을 수 있는 물고기의 종류가 달라진다

    while q:
        cx, cy = q.popleft()
        if (cgraph[cx][cy] != 0) and (cgraph[cx][cy] < shark_size):
            # 0은 물고기가 없는 곳이니까 0이 아니면서 상어 크기보다 작은 물고기들을 먹을 수 있다
            fish_list.append([cx, cy, visited[cx][cy] -1])
            # visited check로 인해 시작점이 1이므로 표시한 값보다 -1한 값이 거리가 된다

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= n or ny >=n or nx <0 or ny <0: # 그래프 경계
                continue
            if cgraph[nx][ny] > shark_size: # 사이즈보다 큰경우 지나갈 수 없음
                continue
            if visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1

    return fish_list

# 큐에는 다음으로 가야할 곳을 저장해두는 용도
sec = 0
shark_size = 2
confirm = 0
while queue:
    eat = 0 # 상어가 먹은 물고기 수, 물고기의 크기가 변할때마다 다시 세야하므로 안에서 초기화해줌
    # if confirm == 10:
    #     break
    #print("shark_size", shark_size, eat)

    while eat < shark_size: # 상어의 사이즈 마다 먹을 수 있는 물고기의 수가 정해진다 최대로 크기만큼만 물고기를 먹을 수 있고, 0부터 시작하므로 <
        cx, cy, csec = queue.popleft() # 현재 x,y와 xy좌표까지 오는데 걸리는 시간
        sec = sec + csec # 전체 시간에 계속 더해줌
        graph[cx][cy] = 0 # 방문처리
        fish_list = get_fishes(graph, cx, cy, shark_size) # 먹을 수 있는 물고기 리스트를 구함

        if len(fish_list) >= 2: # 먹을 수 있는 물고기가 1마리보다 많다면
            # x[2] 가장 가까운 거리 순,
            # x[0] 가까운 물고기가 많다면 행이 작은 순
            # x[1] 그래도 많다면 열이 작은 순
            fish_list = sorted(fish_list, key=lambda x: (x[2], x[0], x[1])) # ★이 정렬로 다 풀었다고 해도 과언이 아니다 !
            queue.append(fish_list[0]) # 그때의 첫번째 값이 다음 목적지가 된다
        elif len(fish_list) == 1: #1마리라면 그 물고기를 먹을 감
            queue.append(fish_list[0])
        elif len(fish_list) == 0: # 먹을 수 있는 물고기가 없다면 도움요청, 반복을 멈춘다
            break
        eat += 1

    shark_size =shark_size + 1


print(sec)