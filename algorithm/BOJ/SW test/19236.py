# 맨 처음 풀이
# 그냥 현재 상어가 갈 수 있는 물고기 중 가장 번호가 큰 번호부터 먹어서 틀렸다..!

# 큐에 0,0 넣음
# 상어정보에 0,0 물고기의 방향을 줌
# 0,0에 물고기 존재 정보 0 visited check

# 물고기 이동 1번 물고기부터
# 번호가 작은 순서대로 큐에 일단 다 넣어두고
# 빼면서 dxdy 반시계방향으로 회전 하면서 이동할 수 있는 칸 있나 없나 보기
# 없으면 이동하지 않고 그외에는 이동할 자리의 물고기와 위치를 바꿈
# 모든 물고기가 바뀌면 -> 큐가 비워지면

# 상어가 이동
# 상어의 방향 정보에 따라서 갈 수 있는 칸을 찾음(한번에 같은 방향으로 여러 칸 뛰어넘어서 이동할 수 있음)
# 상어가 먹을 수 있는 물고기 번호의 최댓값 출력


from collections import deque

graph = []
visited = [0] * 17
eaten = [0] * 17
fish_list = []

for i in range(4):
    temp = list(map(int, input().split()))
    graph.append([])
    for j in range(len(temp)):
        if j % 2 == 0:
            graph[i].append((temp[j], temp[j+1]))


# 상어 정보, 현재 위치 x,y, 상어가 먹은 물고기  번호의 합, 상어 방향
queue = deque()
queue.append(graph[0][0])
graph[0][0] = (0, 0) # 0,0이면 비어있는 칸



fish_info = queue.popleft()
current_shark = [0, 0, fish_info[0], fish_info[1]]
visited[fish_info[0]] = 1
eaten[fish_info[0]] = 1

# 다음 목적지가 될 방문 안했으면서 & 가장 작은 fish_num찾기

next_fish_num= 0
for i in range(1,17):
    if visited[i] == 0 and eaten[i] == 0:
        next_fish_num = i
        break

for i in range(4):
    for j in range(4):
        if graph[i][j][0] == next_fish_num:
            queue.append((i, j, graph[i][j][0], graph[i][j][1]))

# 원래 1 2 3 4 5 6 7 8
# 방향 0 1 2 3 4 5 6 7
# 방향 ↑ ↖ ← ↙ ↓ ↘ → ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

while queue:
    cx, cy, fn, fd = queue.popleft()
    visited[fn] = 1
    print(cx, cy, fn, fd)
    # 물고기가 이동할 수 있는 칸 찾기
    point = 0
    while point < 8: # point가 모든 방향을 확인해서 바꿀 수가 없다면 이동 X
        #print("전", fd)
        dir = fd+point -1
        if dir >= 8:
            dir = dir % 8
        nx = cx + dx[dir]
        ny = cy + dy[dir]
        if nx >= 4 or ny >= 4 or nx <0 or ny <0:
            point += 1
            continue
        if (nx == current_shark[0]) and (ny == current_shark[1]):
            point += 1
            continue
        else:
            graph[nx][ny], graph[cx][cy] = graph[cx][cy], graph[nx][ny]
            break

    next_fish_num = 0
    for i in range(1, 17):
        if visited[i] == 0:
            next_fish_num = i
            break
    # for i in range(4):
    #     print(graph[i])
    #print("visited",visited)
    #print("next_fish_num", next_fish_num)
    breaker = False
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == next_fish_num:
                breaker = True
                break
        if breaker:
            break
    if next_fish_num:
        queue.append((i, j, graph[i][j][0], graph[i][j][1]))
    breaker = False
    # for i in range(4):
    #     print(graph[i])

    if sum(visited[1:]) == 16: # 물고기가 다 이동했으면
        # 상어가 이동
        #print(current_shark)
        sx = current_shark[0]
        sy = current_shark[1]
        sd = current_shark[3] -1
        #print("sd", sd)

        # 상어가 이동할 수 있는 칸 찾기
        # 방향 중에 물고기가 있는 곳
        shark_can = []
        while True:
            sx = sx + dx[sd]
            sy = sy + dy[sd]
            if sx >= 4 or sy >= 4 or sx <0 or sy <0:
                break
            if graph[sx][sy] == (0,0):
                continue
            else:
                #print("sx,sy", sx,sy)
                a0 = graph[sx][sy][0]
                a1 = graph[sx][sy][1]
                shark_can.append((sx,sy,a0, a1))
        #print(shark_can)
        if len(shark_can) == 0:
            breaker = True
            break
        else:
            shark_can = sorted(shark_can, key=lambda x:-x[2])

        if breaker:
            break
        #print(shark_can)
        #print(shark_can[0])
        fish_info = shark_can[0]
        current_shark = [fish_info[0], fish_info[1], current_shark[2] + fish_info[2], fish_info[3]]
        print("current_shark", current_shark)

        graph[fish_info[0]][fish_info[1]] = (0,0)
        eaten[fish_info[2]] = 1

        # visited 초기화
        visited = eaten[:]
        # 다음 목적지가 될 방문 안했으면서 & 가장 작은 fish_num찾기

        next_fish_num = 0
        for i in range(1, 17):
            if visited[i] == 0 and eaten[i] == 0:
                next_fish_num = i
                break
        #print("next_fish_num", next_fish_num)
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == next_fish_num:
                    queue.append((i, j, graph[i][j][0], graph[i][j][1]))


        #print(queue)
        for i in range(4):
            print(graph[i])

print(current_shark)



# 참고한 풀이

import copy

# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기 번호, 방향]을 저장
        array[i][j] = [data[j*2], data[j*2+1]-1]


# 8가지 방향 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

result = 0 # 최종결과

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)

def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y < 4 :
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) # 리스트를 통째로 복사

    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1 # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y) # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)

