from collections import deque
N = int(input())

sand = []
visited = []
queue = deque()
ans = 0

for i in range(N):
    temp = list(map(int, input().split()))
    sand.append([])
    visited.append([])
    for j in range(N):
        sand[i].append(temp[j])
        visited[i].append(0)

# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 모래 이동
left = [[0, -2, 0.05], [1, -1, 0.1], [-1, -1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [2, 0, 0.02], [-2, 0, 0.02], [1, 1, 0.01], [-1, 1, 0.01], [0, -1, 1]]
right = [[r, -c, ratio] for r, c, ratio in left]
up = [[c, r, ratio] for r, c, ratio in left]
down = [[-c, r, ratio] for r, c, ratio in left]
def blow(tr, tc, dir):
    global ans
    tmp = 0
    if dir == 0:
        for r, c, ratio in left:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 1:
        for r, c, ratio in down:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 2:
        for r, c, ratio in right:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 3:
        for r, c, ratio in up:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    sand[tr][tc] = 0

# 토네이도 이동
def tornado(x,y): # x,y는 토네이도 시작점
    v = []
    for i in range(N):
        v.append([])
        for j in range(N):
            v[i].append(0)

    cnt_list = []
    for i in range(1, N):
        cnt_list.append(i)
        cnt_list.append(i)
    cnt_list.append(i)

    q = deque()
    q.append((x,y))
    v[x][y] = 1
    i = 0  # 방향
    visited = 1
    for dis in cnt_list:
        for d in range(dis):
            cx, cy = q.popleft()
            #print("cx,cy, i, d", cx,cy, i, d)

            nx = cx +dx[i]
            ny = cy + dy[i]
            blow(nx,ny, i)
            #print("nx,ny", nx, ny)
            q.append((nx,ny))
            visited+=1
            v[nx][ny] = visited
        i +=1
        if i == 4:
            i = 0

    # for i in range(N):
    #     print(v[i])




tornado(N//2, N//2)
# print(left)
# print(right)
# print(up)
# print(down)
print(ans)
