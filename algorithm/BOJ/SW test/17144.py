from collections import deque

R, C, T = map(int, input().split())

# 맨 처음 미세먼지 입력받기
graph = []
for i in range(R):
    temp = list(map(int, input().split()))
    graph.append(temp)

# 에어컨 위치
air_con = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_con.append([i,j])

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 미세먼지 주변에 퍼지는 함수 -> 큐는 필요없음! 밖에서 이중 포문으로 돌면서 그 좌표의 주변 사방만 살펴보면 되니까
def spread(graph, cr,cc):
    global graph_1s

    #minu = graph[cr][cc] // 5
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if nr >= R or nc >= C or nr <0 or nc< 0: # 경계 밖
            continue
        if graph[nr][nc] == -1: # 공기청정기
            continue
        graph_1s[nr][nc] = graph_1s[nr][nc] + graph[cr][cc] // 5
        graph_1s[cr][cc] = graph_1s[cr][cc] - graph[cr][cc] // 5
    return graph_1s

# 공기청정기로 인해 미세먼지가 회전하는 함수
def air(graph_1s, up, down):
    # 회전한 먼지를 저장할 2차원 배열
    new = []
    for i in range(R):
        new.append([])
        for j in range(C):
            new[i].append(0)


    for i in range(R):
        for j in range(C):
            # 공기청정기인 경우 패스
            if graph_1s[i][j] == -1:
                new[i][j] = graph_1s[i][j]
            # <-
            elif i == 0 or i == (R-1):
                if j == 0:# 모서리이면
                    if i < up:
                        new[i+1][j] = graph_1s[i][j]
                    else:
                        new[i-1][j] = graph_1s[i][j]
                else:
                    new[i][j-1] = graph_1s[i][j]
            # ->
            elif i == up or i == down:
                if j == (C-1) and i <= up:# 모서리면
                    new[i-1][j] = graph_1s[i][j]
                elif j == (C-1) and i >= up:
                    new[i+1][j] = graph_1s[i][j]
                else:
                    new[i][j+1] = graph_1s[i][j]

            elif j == 0:
                # ↑
                if i <= up:
                    new[i+1][j] = graph_1s[i][j]
                # ↓
                elif i >= down:
                    new[i-1][j] = graph_1s[i][j]
            elif j == (C-1):
                # ↑
                if i <= up:
                    new[i-1][j] = graph_1s[i][j]
                # ↓
                elif i >= down:
                    new[i+1][j] = graph_1s[i][j]
            else:
                new[i][j] = graph_1s[i][j]
    return new


# 공기청정기 위치
up = 0
down = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            up = i-1
            down = up+1
            break



# 시간 초 만큼 반복
for t in range(T):

    # 원본은 유지하고 원본을 복사하여 새로운 변수에 퍼진 미세먼지를 저장
    graph_1s = []
    for i in range(R):
        graph_1s.append([])
        for j in range(C):
            graph_1s[i].append(graph[i][j])

    # print("==초기==")
    # print("graph")
    # for r in range(R):
    #     print(graph[r])
    #
    # print("graph_1s")
    # for r in range(R):
    #     print(graph_1s[r])

    # 원본을 기준으로 원본에서 미세먼지가 있는 곳에 들어가서 미세먼지를 퍼뜨려줌
    for i in range(R):
        for j in range(C):
            if (graph[i][j] != 0) and (graph[i][j] != -1):
                # for i in range(R):
                #     graph_1s.append([])
                #     for j in range(C):
                #         graph_1s[i].append(graph[i][j])

                graph_1s = spread(graph, i, j)

    # print("==스프레드==")
    # print("graph")
    # for r in range(R):
    #     print(graph[r])
    #
    # print("graph_1s")
    # for r in range(R):
    #     print(graph_1s[r])

    graph_1s = air(graph_1s, up, down)
    # 공기청정기 위치에 다시 -1로 표시
    for i in range(R):
        for j in range(C):
            if [i, j] in air_con:
                graph_1s[i][j] = -1

    # print("==회전==")
    # print("graph")
    # for r in range(R):
    #     print(graph[r])

    # print("graph_1s")
    # for r in range(R):
    #     print(graph_1s[r])

    # graph_1s가 다음 초의 원본(graph)가 될테니까 복사해줌 -> 주의 !!!
    graph = []
    for i in range(R):
        graph.append([])
        for j in range(C):
            graph[i].append(graph_1s[i][j])


# for i in range(R):
#     print(graph[i])
#
# print()
# for i in range(R):
#     print(graph_1s[i])

# 미세먼지가 있는 곳만 미세먼지의 갯수를 셈
dust = 0
for i in range(R):
    for j in range(C):
        if graph_1s[i][j] > 0: #and [i,j] not in air_con:
            dust += graph_1s[i][j]
print(dust)