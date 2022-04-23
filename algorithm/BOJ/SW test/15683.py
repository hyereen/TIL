# 시간초과

n, m = map(int, input().split())

original_graph = []
watched_graph = []
cctvs = []
cctvs_xy = []
used = []
for i in range(n):
    temp = list(map(int, input().split()))
    original_graph.append([])  # 원본
    watched_graph.append([])
    for j in range(m):
        original_graph[i].append(temp[j]) # 원본
        watched_graph[i].append(temp[j])
        if original_graph[i][j] in [1,2,3,4,5]:
            cctvs.append(original_graph[i][j])
            cctvs_xy.append([i,j])
            used.append(0)

chosen = []
cctvs_cases = []
def perm(list, r):
    global chosen, used,cctvs_cases

    if len(chosen) == r:
        if not chosen in cctvs_cases:
            cctvs_cases.append(chosen[:])
            return
    for i in range(len(list)):
        if not used[i]:
            chosen.append(list[i])
            used[i] = 1
            perm(list, r)
            used[i] = 0
            chosen.pop()

perm(cctvs, len(cctvs))
"""
1 cctv: 0좌/1하/2우/3상 4가지 
2 cctv: 0:0좌2우/1:1하3상 2가지
3 cctv: 0:2우3상/1:0좌1하 2가지
4 cctv: 0:0좌2우3상/1:0좌2우1하 2가지
5 cctv: 0좌1하2우3상 다 1가지 
"""

# cctv 방향대로 6을 만나기 전까지 주변 살펴보기
# x, y는 cctv 위치, dir_num은 cctv 방향
def watch(graph, x, y, dir_num):
    new = []

    for i in range(n):
        new.append(graph[i][:])  # 감시 표시

    cctv_num = graph[x][y]
    # dir_num 0:좌 1:하 2:우 3:상
    if dir_num == 0: # 좌
        for i in range(y-1, -1, -1):
            if new[x][i] == 6:
                break
            if (i < y) and (new[x][i] == 0):
                new[x][i] = -cctv_num
    elif dir_num == 1: # 하
        for i in range(x+1, n, +1):
            if new[i][y] == 6:
                break
            if (new[i][y] == 0): # (i > x) and
                new[i][y] = -cctv_num
    elif dir_num == 2: #우
        #print("dir_num", dir_num)
        for i in range(y+1, m, +1):
            #print(i, y)
            if new[x][i] == 6:
                break
            elif (i > y) and (new[x][i] == 0):
                new[x][i] = -cctv_num
    elif dir_num == 3: # 상
        #print("dir_num", dir_num)
        for i in range(x-1, -1, -1):
            #print(i, y)
            if new[i][y] == 6:
                break
            if (i < x) and (new[i][y] == 0):
                new[i][y] = -cctv_num
    # print("---watch함수 안 ---", dir_num)
    # print("graph", count(graph))
    # for x in range(n):
    #     print(graph[x])
    # print("new", count(new))
    # for x in range(n):
    #     print(new[x])
    return new

# c = 0
# for j in range(4):
#     watch(2, 2, j)
#     for i in range(n):
#         print(new[i])
#     print()

# 방향 정하기
# cnt가 가장 적은 방향을 찾아야 함
def direction(graph, x,y):
    final_dir = [0,n*m*4] # [0]은 방향 [1] cnt
    cnt = 0
    if graph[x][y] == 1:
        for i in [0,1,2,3]:
            temp = watch(graph, x, y, i)
            cnt = count(temp)
            if final_dir[1] > cnt:
                final_dir[0] = [i]
                final_dir[1] = cnt

    elif graph[x][y] == 2:
        for i in [[0,2], [1,3]]:
            cnt_sum = 0
            for j in i:
                temp = watch(graph,x, y, j)
                cnt = count(temp)
                #print("temp", temp)
                cnt_sum = cnt_sum + cnt
            #print(i, cnt_sum, "cnt_sum")
            #print(final_dir[1], "final_dir[1]")
            if final_dir[1] > cnt_sum:
                final_dir[0] = i
                final_dir[1] = cnt_sum
    #3 cctv: 0:2우3상/1:1하2우/2:0좌1하/3:0좌3상 4가지
    elif graph[x][y] == 3:
        for i in [[2,3], [1,2], [0,1], [0,3]]:
            cnt_sum = 0
            for j in i:
                temp = watch(graph,x, y, j)
                cnt = count(temp)
                cnt_sum = cnt_sum + cnt
            if final_dir[1] > cnt_sum:
                final_dir[0] = i
                final_dir[1] = cnt_sum
    # 4 cctv: 0:0좌2우3상/1:1하2우3상/2:0좌1하2우/3:0좌1하3상 4가지
    elif graph[x][y] == 4:
        for i in [[0, 2, 3], [1,2,3], [0, 2, 1],[0,1,3]]:
            cnt_sum = 0
            for j in i:
                temp = watch(graph,x, y, j)
                cnt = count(temp)
                #print(i,"cnt", cnt)
                cnt_sum = cnt_sum + cnt
            if final_dir[1] > cnt_sum:
                final_dir[0] = i
                final_dir[1] = cnt_sum
            #print(cnt_sum, "cnt_sum", "final_dir", final_dir)

    elif graph[x][y] == 5:
        final_dir[0] = [0,1,2,3] # 모든 방향

    #print("final_dir", final_dir)
    return final_dir[0]
"""
1 cctv: 0좌/1하/2우/3상 4가지 
2 cctv: 0:0좌2우/1:1하3상 2가지
3 cctv: 0:2우3상/1:1하2우/2:0좌1하/3:0좌3상 4가지
4 cctv: 0:0좌2우3상/1:1하2우3상/2:0좌1하2우/3:0좌1하3상 4가지
5 cctv: 0좌1하2우3상 다 1가지 
"""
def count(g): #g는 그래프
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt +=1

    return cnt

xy_num = []
num = []
zero_min = 999999
cctvs_xy_origi = cctvs_xy[:]
for c in cctvs_cases:
    # 케이스마다 초기화
    cctvs_xy = cctvs_xy_origi[:]
    watched_graph = []
    for nn in range(n):
        watched_graph.append(original_graph[nn][:])
        # for x in range(n):
        # print(watched_graph[x])

    for a in c:
        #print(c, a)
        for i in range(n):
            for j in range(m):

                #print(watched_graph[i][j])
                if (watched_graph[i][j]) == a and [i,j] in cctvs_xy:
                    #print(watched_graph[i][j], i,j, watched_graph[i][j] in [1,2,3,4,5])
                    d = direction(watched_graph, i, j)
                    #print(i, j, d)
                    for dd in d:
                        watched_graph = watch(watched_graph, i, j, dd)
                    cctvs_xy.remove([i,j])
                    break
        #for x in range(n):
            #print(watched_graph[x])
        zero = count(watched_graph)
        if zero_min > zero:
            zero_min = zero

        #print(c, a, zero, zero_min)

# print("===최종===")
# for x in range(n):
#     print(watched_graph[x])

# zero = 0
# zero = count(watched_graph)
if zero_min == 999999:
    zero_min = count(original_graph)
print(zero_min)


# 정답
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
      [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

MIN = 9999999999999999


def dfs(start, MAP, cctv):
    global MIN
    if start == len(cctv):
        cnt = 0
        for y in range(0, row):
            for x in range(0, col):
                if MAP[y][x] == 0:
                    cnt += 1
        MIN = min(MIN, cnt)
        return

    num, y, x = cctv[start]
    for dir in di[num]:
        tmp = []
        for i in range(row):
            tmp.append(MAP[i][:])
        for i in dir:
            ny, nx = y + dy[i], x + dx[i]
            while row > ny >= 0 and col > nx >= 0:
                if tmp[ny][nx] == 6:
                    break
                elif tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
                ny += dy[i]
                nx += dx[i]
        dfs(start + 1, tmp, cctv)


row, col = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(row)]
cctv = []
#block_cnt = 0
for y in range(0, row):
    for x in range(0, col):
        if MAP[y][x] not in [0, 6]:
            cctv.append([MAP[y][x], y, x])
dfs(0, MAP, cctv)
print(MIN)