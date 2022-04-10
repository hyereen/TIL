from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# d == 0: 북 1:동 2:남 3:서

visited = []
for i in range(n):
    temp = list(map(int, input().split()))
    visited.append(temp[:])

# i는 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
clean = 0 # 청소한 칸의 개수 카운트 변수

queue = deque()
queue.append((r,c)) # 시작점 입력은 그대로
visited[r][c] = 2 # 2로 초기화해서 벽인 1과 헷갈리지 않도록 만들어준다
clean = clean + 1 # 큐에 좌표를 넣을 때 청소한 칸의 개수도 +1
two_a = 0 # 2a번 단계가 몇번 실행되었는지 확인하는 변수
# d == 0: 북 1:동 2:남 3:서
# i == 0: 북 1:서 2:남 3:동
# confirm = 0 # 청소 어디까지 했는지 출력해보려고 만든 확인용 변수
i = 0 # 어차피 while문 들어가자마자 변경될거지만 일단 0으로 초기화해줌
while queue:
    # if confirm == 6:
    #     break
    cr, cc = queue.popleft() # current c, current r로, 현재 r,c값을 의미
    # print("cr,cc, d, i",cr, cc, d, i )

    if d == 0: # d가 0인 경우(북)
        i = 1 # 왼쪽인 1(서)부터 빈 공간인지 확인해야 함
    elif d == 1: # d가 1인 경우(동)
        i = 0 # 동쪽 방향의 왼쪽인 0(북)
    elif d == 2: # d가 2인 경우(남)
        i = 3 # 남쪽 방향의 왼쪽인 3(동)
    elif d == 3: # d가 3인 경우(서)
        i = 2 # 서쪽 방향의 왼쪽인 2(남)

    idx = 0 # 보통 bfs라면 for문으로 dx, dy를 순서대로 돌테지만, 이 경우 d 값에 따라 시작하는 i가 다르므로 개수 카운트를 해준다.
    while idx < 4: # 그래서 시작한 i부터 4번 확인하면 현재 위치의 사방은 다 확인한걸로 생각
        if d < 0: # 이걸 while문 안에서 해줘야 하는데, 이는 d가 서->남->동->북으로 돌아야 왼쪽 방향으로 회전하므로 뒤에서 d를 1씩 빼주는데,
            d = 3 # d가 0보다 작아지면 다시 3으로 만들어줘서 반복할 수 있도록 만들어준다
        nr = cr + dx[i]
        nc = cc + dy[i]
        # print("nr,nc, d, i", nr, nc, d, i)
        if nr >= n or nc >= m or nr < 0 or nc < 0: # 장소를 벗어난 경우
            continue
        # 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다.
        if visited[nr][nc] == 0 : # 청소가 안되어 있다면
            visited[nr][nc] = visited[cr][cc] + 1 # 방문 체크해주고
            queue.append((nr, nc))
            clean = clean + 1 # 청소한 개수 +1
            i = (i + 1) % 4 # i도 계속 커지면 안되니까 4로 나눠주어서 0~3을 만복할 수 있도록 만들어준다
            d = d - 1 # 방향은 왼쪽으로 회전해야 하므로 1씩 빼준다
            idx += 1 # 반복이 4번 되었을 경우, 현재 반복을 끝내야 하므로 1씩 더해줌
            break # 맨 처음 왼쪽이 빈 공간을 발견한 경우, 그 위치에서의 반복을 멈춰줘야 함
        else: # 그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
            two_a +=1 # 사방이 다 청소되어있거나 벽인 경우를 카운트하는 변수
            d = d - 1 # 사방이 다 청소되어있거나 벽인 경우에도 왼쪽 방향으로 회전하면서 확인해줘야하므로 방향은 계속 돌려준다
            idx += 1 # 이 경우도 반복에 포함되어야 하므로
            i = (i + 1) % 4

    #print("two_a", two_a)
    # 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
    if two_a == 4: # 2a번 단계가 연속으로 네 번 실행되었을 경우
        # print("cr, cc, d, i", cr, cc, d, i)
        if d < 0: # 이걸 여기서 또 안해주면, 틀렸습니다가 뜨는데!
            d = 3 # 이미 위에서 else인 경우에 d를 계속 1씩 빼주는데 만약 0보다 작아진 경우, 아래의 조건문에 걸리지 않기때문..따라서 또 체크해줘야 한다
        if d == 0: # 방향이 북쪽일때
            if visited[cr+1][cc] == 1: # 남쪽이 벽이면
                break # 작동을 멈춘다
            else: # 벽이 아니라면, -> 이미 청소한 경우라면
                queue.append((cr+1, cc)) # 후진해야되니까 남쪽을 큐에 넣어줌
        elif d == 1: # 동
            if visited[cr][cc-1] == 1:
                break
            else:
                queue.append((cr, cc-1))
        elif d == 2: # 남
            if visited[cr-1][cc] == 1:
                break
            else:
                queue.append((cr-1, cc))
        elif d == 3: # 서
            if visited[cr][cc+1] == 1:
                break
            else:
                queue.append((cr, cc+1))
    #print("queue", queue)
    two_a = 0 # 확인하는 위치마다 2a번 단계가 연속으로 네 번 실행되었는지 확인해야되서 0으로 초기화해준다




print(clean)
