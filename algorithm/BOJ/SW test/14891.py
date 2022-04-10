from collections import deque

queue = deque()
op = [0,0,0,0,0]
visited = [0,0,0,0,0]

# d 1시계 -1 반시계 2 움직임 없음
# 톱니바퀴별 회전 방향을 결정해주는 함수
def make_op(n, d):
    global op, visited
    queue.append(n)
    visited[n] = 1
    op[n] = d

    while queue: # 맨 처음 회전시키는 톱니바퀴에 의해 주변 톱니바퀴들이 영향을 받는다고 생각해서 큐로 주변 바퀴들을 넣어줌
        cn = queue.popleft()
        #print("cn, queue", cn, queue)

        if cn == 1: # 바퀴1이 회전하면
            if visited[2] == 0: # 바퀴2가 영향을 받는데, 바퀴가 여러번 영향을 받지는 않으므로, 방문체크를 해줘야 함
                #print(wheels[cn][2], wheels[2][6])
                if wheels[cn][2] == wheels[2][6] or op[cn] == 3:
                    # 서로 맞닿아있는 바퀴들의 상태가 같으면 바퀴를 회전시키지 않고 그대로 (3)
                    # 또는 영향을 주는 바퀴(여기서는 바퀴 1)가 회전하지 않고 그대로라면, 영향을 받는 바퀴(여기서는 2)도 그대로 (3)
                    op[2] = 3
                else: # 다르거나 그대로가 아니라면,
                    op[2] = -op[cn] # 영향을 주는 바퀴의 방향의 반대로 회전해야 함
                queue.append(2) # 2 옆에 있는 1 또는 3이 영향을 받을 수 있도록 2를 큐에 넣어줌
                visited[2] = 1 # 방문체크도 해줌
        elif cn == 2:
            if visited[1] == 0:
                #print(wheels[cn][6], wheels[1][2], op[cn])
                if wheels[cn][6] == wheels[1][2] or op[cn] == 3:
                    op[1] = 3
                else: # 다르면
                    op[1] = -op[cn]
                queue.append(1)
                visited[1] = 1
            if visited[3] == 0: # elif가 아니고 if여야함 1, 3 둘다 큐에 들어가야하기때문
                #print(wheels[cn][2], wheels[3][6])
                if wheels[cn][2] == wheels[3][6] or op[cn] == 3:
                    op[3] = 3
                else: # 다르면
                    op[3] = -op[cn]
                queue.append(3)
                visited[3] = 1
        elif cn == 3:
            if visited[2] == 0:
                #print(wheels[cn][6], wheels[2][2])
                if wheels[cn][6] == wheels[2][2] or op[cn] == 3: #같으면
                    op[2] = 3 # 2번 바퀴가 안바뀌어야 함
                else: # 다르면
                    op[2] = -op[cn] # 영향을 받은 바퀴의 반대 방향으로 돌아야 함
                queue.append(2)
                visited[2] = 1
            if visited[4] == 0:
                #print(wheels[cn][2], wheels[4][6])
                if wheels[cn][2] == wheels[4][6] or op[cn] == 3:
                    op[4] = 3
                else: # 다르면
                    op[4] = -op[cn]
                queue.append(4)
                visited[4] = 1
        elif cn == 4:
            if visited[3] == 0:
                #print(wheels[cn][6], wheels[3][2])
                if wheels[cn][6] == wheels[3][2] or op[cn] == 3:
                    op[3] = 3
                else: # 다르면
                    op[3] = -op[cn]
                queue.append(3)
                visited[3] = 1
        #print(op)

# 회전시키기
# q 회전시킬 큐, d 방향: 1 시계 -1 반시계 3 그대로

def rotate(q, d):
    if d == 1: # 시계방향이면
        temp = q.pop() # 맨 오른쪽꺼 뽑아서
        q.appendleft(temp) # 맨 앞에 넣어줌
    elif d == -1: # 반시계 방향이면
        temp = q.popleft() # 맨 왼쪽꺼 뽑아서
        q.append(temp) # 맨 뒤에 넣어줌
    # d == 3 이면 그대로 리턴
    return q


wheels = deque()
wheels.append([])

for i in range(4):
    wheels.append(deque(map(int, input()))) # 입력받는 방법 맨날 헷갈림 ㅠㅠ

K = int(input())


for j in range(K):
    num, dir = map(int, input().split())
    make_op(num, dir)
    #print(op)
    for i in range(1, 5):
        #print("wheels[i], op[i]")
        #print(wheels[i], op[i])
        wheels[i] = rotate(wheels[i], op[i])
        #print(wheels[i])
    # 초기화, 다음 회전에서 새로 op, visited 체크를 해야 하므로!
    op = [0, 0, 0, 0, 0]
    visited = [0, 0, 0, 0, 0]

#print(wheels)

# 점수 계산 -> 인덱스 유의!
score = 0
for i in range(1,5):
    if i == 1:
        if wheels[i][0] == 1:
            score = score + 1
    if i == 2:
        if wheels[i][0] == 1:
            score = score + 2
    if i == 3:
        if wheels[i][0] == 1:
            score = score + 4
    if i == 4:
        if wheels[i][0] == 1:
            score = score + 8

print(score)