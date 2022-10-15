# https://www.acmicpc.net/problem/16234

# pypy3

from collections import deque
import sys

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


# bfs를 이용해서, 연결되어 있는 모든 나라를 찾음
def bfs(q):
    global visited, n, r, l, a, temp, sum_people
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0:
                    if l <= abs(a[y][x] - a[ny][nx]) <= r:
                        visited[ny][nx] = 1
                        temp.append([ny, nx])
                        q.append([ny, nx])
                        sum_people += a[ny][nx]


# 입력
n, l, r = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# 해결
days = 0
while True:
    visited = [[0] * n for _ in range(n)]
    q = deque()
    opened_nations = []

    # 나라들을 순회하면서, bfs로 가능한 연결되어있는 모든 나라들의 조합을 구해서
    # opened_nations에 인구수와 함께 넣는다
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = []
                sum_people = a[i][j]
                visited[i][j] = 1
                temp.append([i, j])
                q.append([i, j])
                bfs(q)
                if 1 < len(temp):
                    opened_nations.append((temp, sum_people))

    # 만약 국경이 열려있지 않으면 인구이동이 일어나지 않는 것이니까 break
    if len(opened_nations) == 0:
        break

    # 인구 이동
    for nations, peoples in opened_nations:
        cnt_people = peoples // len(nations)
        for y, x in nations:
            a[y][x] = cnt_people

    days += 1
    # 문제 조건에서 반복이 2000회 이상 수행되지 않는다고 했으니까
    # 2000이 넘어가면 코드가 이상하다는 것을 알려주고 stop
    if 2000 < days:
        print("something error!")
        sys.exit()

print(days)