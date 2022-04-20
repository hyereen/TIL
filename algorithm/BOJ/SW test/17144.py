from collections import deque

R, C, T = map(int, input().split())

graph = []

for i in range(R):
    temp = list(map(int, input().split()))
    graph.append(temp)



air_con = []
# 에어컨 위치
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_con.append([i,j])
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def spread(graph, a,b):
    global graph_1s
    queue = deque()
    queue.append((a,b))

    while queue:
        cr, cc = queue.popleft()
        minu = graph[cr][cc] // 5
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if nr >= R or nc >= C or nr <0 or nc< 0:
                continue
            if graph[nr][nc] == -1: # 공기청정기
                continue
            graph_1s[nr][nc] = graph_1s[nr][nc] + minu
            graph_1s[cr][cc] = graph_1s[cr][cc] - minu
            #if cr == 1 and cc == 6:
                #print(cr, cc, graph[cr][cc], graph[cr][cc] // 5)
                #print(graph_1s[nr][nc], graph[cr][cc], (graph[cr][cc] // 5))
                #print("graph_1s[nr][nc]", nr, nc, graph_1s[nr][nc])
                #print("spread 안", graph_1s)
    return graph_1s

def air(graph_1s, up, down):
    new = []
    for i in range(R):
        new.append([])
        for j in range(C):
            new[i].append(0)

    #print("up,down", up, down)

    ni = 0
    nj = 0
    for i in range(R):
        for j in range(C):
            #print(i, j, "=============================")
            #print("new[2][7]", new[2][7])
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
                #print("혹시")
                if j == (C-1) and i <= up:# 모서리면
                    #print("1")
                    new[i-1][j] = graph_1s[i][j]
                elif j == (C-1) and i >= up:
                    #print("2")
                    new[i+1][j] = graph_1s[i][j]
                else:
                    #print("3")
                    #print("graph_1s[i][j]", graph_1s[i][j])
                    new[i][j+1] = graph_1s[i][j]
                    #print("new[i][j+1]", i, j+1, new[i][j+1])


            elif j == 0:
                if i <= up:
                    new[i+1][j] = graph_1s[i][j]
                elif i >= down:
                    new[i-1][j] = graph_1s[i][j]
            elif j == (C-1):
                #print("설마",i,j)
                if i <= up:
                    new[i-1][j] = graph_1s[i][j]
                elif i >= down:
                    new[i+1][j] = graph_1s[i][j]
            else:
                new[i][j] = graph_1s[i][j]
    return new


# for i in range(R):
#     for j in range(C):
#         if (graph[i][j] != 0) and (graph[i][j] != -1):
#             spread(i,j)

# for i in range(R):
#     print(graph_1s[i])

up = 0
down = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            up = i-1
            down = up+1
            break

    # for r in range(R):
    #     print(graph_1s[i])



for t in range(T):
    graph_1s = []
    # print("T =", T)
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

dust = 0
for i in range(R):
    for j in range(C):
        if graph_1s[i][j] > 0: #and [i,j] not in air_con:
            dust += graph_1s[i][j]
print(dust)