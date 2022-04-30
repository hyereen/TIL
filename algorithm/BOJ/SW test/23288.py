from collections import deque
n, m, k = map(int, input().split())

graph = []

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)


# 주사위 방향: 북 2 동 3 서 4 남 5
# 상 우 좌 하
dx=[-1, 0, 0, 1]
dy=[0, 1, -1, 0]
# 주사위
dice = [0] * 6
"""
  1
3 5 2
  4
  0
5가 항상 바닥 0이 항상 천장
"""
dice[0] = 1
dice[1] = 2
dice[2] = 3
dice[3] = 4
dice[4] = 5
dice[5] = 6


# 주사위 굴리기
def dice_roll():
    global dice, dice_x, dice_y, dice_dir

    x = dice_x
    y = dice_y
    d = dice_dir

    nx=x+dx[d-2]
    ny=y+dy[d-2]


    # 주사위 방향: 북 2 동 3 서 4 남 5
    if nx <0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어나는 경우 = 이동방향에 칸이 없다면
        # 방향을 반대로 만들어주기
        if d == 2: # 북
            d = 5 # 남
        elif d == 3: # 동
            d = 4 # 서
        elif d == 4: # 서
            d = 3 # 동
        elif d == 5: # 남
            d = 2 # 북

        nx = x + dx[d-2]
        ny = y + dy[d-2]


    if 0<=nx<n and 0<=ny<m: # 이동방향으로 한칸 굴리기
        if d==3:
            dice[0],dice[2],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[2]
        elif d==4:
            dice[0],dice[2],dice[3],dice[5]=dice[2],dice[5],dice[0],dice[3]
        elif d==2:
            dice[0],dice[1],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[1]
        elif d==5:
            dice[0],dice[1],dice[4],dice[5]=dice[1],dice[5],dice[0],dice[4]

        dice_x=nx
        dice_y=ny
        dice_dir = d

# 바닥 연결 개수 구하기
def get_cnt(x,y, num): # 시작점(x,y), 같은 정수가 나와야 함
    visited = []
    cnt = 1
    for i in range(n):
        visited.append([])
        for j in range(m):
            visited[i].append(0)

    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == num:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1

    return cnt



# 초기 주사위 상태
dice_dir = 3 # 북 2 동 3 서 4 남 5
dice_x = 0
dice_y = 0
score = 0

for i in range(k):
    # 1. 주사위가 이동방향으로 한칸 굴러간다
    dice_roll()
    # 2. 도착한 칸에 대한 점수 획득
    temp_cnt = get_cnt(dice_x, dice_y, graph[dice_x][dice_y])
    temp_score = temp_cnt * graph[dice_x][dice_y]
    score = score + temp_score
    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정
    A = dice[5]
    B = graph[dice_x][dice_y]
    if A > B:
        if dice_dir == 2:
            dice_dir = 3
        elif dice_dir == 3:
            dice_dir = 5
        elif dice_dir == 5:
            dice_dir = 4
        elif dice_dir == 4:
            dice_dir = 2
    elif A < B:
        if dice_dir == 2:
            dice_dir = 4
        elif dice_dir == 4:
            dice_dir = 5
        elif dice_dir == 5:
            dice_dir = 3
        elif dice_dir == 3:
            dice_dir = 2

    #print("temp_cnt", temp_cnt)
    #print("temp_score", temp_score)
print(score)