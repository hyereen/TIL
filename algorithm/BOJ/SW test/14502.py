# 빈 칸에 3개 벽 세우는 조합 구하기
# 그때마다 바이러스 퍼지게하고
# 0의 수 초 만큼 지났는데도 0이 남아있다면 그때 안전영역 개수 세기 => 맥스값 출력하기
# 0이 안남아있으면 바이러스가 다 퍼져서 안전영역 0
from collections import deque

n,m = map(int, input().split())

graph = []
visited_comb = []
visited_vir = []

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp[:]) # 그냥 temp로 넣어주면 나중에 값 변경했을때 값이 똑같이 복사됨
    visited_comb.append(temp[:])
    visited_vir.append(temp[:])


# for i in range(n):
#     visited_comb.append([])
#     for j in range(m):
#         visited_comb[i].append(0)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 그래프에서 0 인 곳, 바이러스 찾기 찾기
zero_space = []
vir_space = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_space.append((i, j))
        elif graph[i][j] == 2:
            vir_space.append((i, j))

# 빈 칸중에 벽을 세울 3가지를 뽑기
chosen = []
wall_cases = []
def comb(zero_space):
    global chosen, visited_comb

    if len(chosen) == 3: # 무조건 벽은 3개
        wall_cases.append(chosen[:]) # 그냥 chosen을 append하면 wall_cases에 빈 리스트만 저장됨 ㅠㅠ 주의!!!
        return

    for i in range(len(zero_space)):
        x, y = zero_space[i]
        if visited_comb[x][y] == 0:
            visited_comb[x][y] = 1
            chosen.append(zero_space[i])
            comb(zero_space[i:])
            visited_comb[x][y] = 0
            chosen.pop()


comb(zero_space)

# 한 케이스마다 바이러스 퍼지게하기
def bfs_vir(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        #print("q", queue)
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0: # n,m 범위 주의
                continue
            if visited_vir[nx][ny] == 1:
                continue
            if visited_vir[nx][ny] == 0:
                #print("nx, ny", nx, ny)
                visited_vir[nx][ny] = 2
                queue.append((nx, ny))

def bfs_safe(x, y):
    queue = deque()
    visited_vir[x][y] = 3 # 큐에 넣을때 비짓 체크
    queue.append((x, y))
    safe_cnt = 1 # 넣을때 이미 안전영영이므로 개수 카운트 +1

    while queue:
        #print("q", queue)
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0: # n,m 범위 주의
                continue
            if visited_vir[nx][ny] == 1:
                continue
            if visited_vir[nx][ny] == 2:
                continue
            if visited_vir[nx][ny] == 0:
                visited_vir[nx][ny] = 3
                queue.append((nx, ny))
                safe_cnt = safe_cnt + 1 # 큐에 넣을 때 비짓체크

    return safe_cnt

# 케이스마다 벽 세우기
safe_cnt_max = 0
for i in range(len(wall_cases)):
    #print("case", i, wall_cases[i])
    x_1, y_1 = wall_cases[i][0]
    x_2, y_2 = wall_cases[i][1]
    x_3, y_3 = wall_cases[i][2]


    visited_vir[x_1][y_1] = 1
    visited_vir[x_2][y_2] = 1
    visited_vir[x_3][y_3] = 1

    # 바이러스 퍼지게하기
    for x,y in vir_space:
        if visited_vir[x][y] == 2:
            #print("x,y", x,y)
            bfs_vir(x,y)

    # 안전영역 찾기
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if visited_vir[i][j] == 0:
                tmp_cnt = bfs_safe(i,j)
                #print("tmp_cnt", tmp_cnt)
                safe_cnt = safe_cnt + tmp_cnt

    if safe_cnt_max < safe_cnt:
        safe_cnt_max = safe_cnt

    #print(visited_vir)

    # visited_vir 원래 그래프대로 되돌리기
    visited_vir = []
    for i in graph:
        visited_vir.append(i[:])

    #print(safe_cnt_max)
    if safe_cnt_max == 25:
        break

print(safe_cnt_max)
# (0, 4), (1, 3), (3, 3) => 9


