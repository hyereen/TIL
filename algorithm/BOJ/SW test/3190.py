from collections import deque

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for i in range(k)]
tl = int(input())
ti, turn = 0, [list(input().split()) for i in range(tl)]

for i in turn:
    i[0] = int(i[0])

snake, t, direction = deque(), 0, 0
snake.append([1, 1])

head = [1, 1]

while True:
    t += 1

    # 이동
    if direction == 0:
        head[1] += 1
    elif direction == 1:
        head[0] += 1
    elif direction == 2:
        head[1] -= 1
    else:
        head[0] -= 1

    # 부딪힘
    if head in snake:
        print(t)
        break
    if head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1:
        print(t)
        break

    # 사과
    if head not in apple:
        snake.popleft()
    else:
        apple.remove(head)

    # 머리 위치 저장
    snake.append([head[0], head[1]])

    # 방향 전환
    if ti < tl and t == turn[ti][0]:
        if turn[ti][1] == "D":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        ti += 1