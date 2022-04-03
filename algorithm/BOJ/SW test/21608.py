from collections import deque
n = int(input())

student_info = deque()
for i in range(0, n*n):
    temp = list(map(int, input().split()))
    student_info.append(temp)

#print(student_info)
classroom = []
like_check = []
empty_check = []
satisfaction = []
for i in range(n):
    classroom.append([])
    like_check.append([])
    empty_check.append([])
    satisfaction.append([])
    for j in range(n):
        classroom[i].append(0)
        like_check[i].append(0)
        empty_check[i].append(0)
        satisfaction[i].append(0)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def get_likes(like_lst):
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 몇명 있는지 찾기
    for i in range(n):
        for j in range(n):
            if classroom[i][j] != 0:
                continue
            if j-1 >= 0 and classroom[i][j-1] in like_lst:
                like_check[i][j] = like_check[i][j] + 1
            if i+1 <n and classroom[i+1][j] in like_lst:
                like_check[i][j] = like_check[i][j] + 1
            if j+1 <n and classroom[i][j+1] in like_lst:
                like_check[i][j] = like_check[i][j] + 1
            if i-1 >=0 and classroom[i-1][j] in like_lst:
                like_check[i][j] = like_check[i][j] + 1

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 수 찾기
    likes = 0
    for i in range(n):
        for j in range(n):
            if like_check[i][j] > likes:
                likes = like_check[i][j]

    #print("likes", likes)
    # 남아있는 자리 중에서 주변에 좋아하는 친구가 없는 경우 => 주의!!
    # 남아있는 자리를 seat_list에 넣어줌
    seat_list = []
    if likes == 0:
        for i in range(n):
            for j in range(n):
                if classroom[i][j] == 0:
                    seat_list.append((i,j))
    else:
        for i in range(n):
            for j in range(n):
                if like_check[i][j] == likes:
                    seat_list.append((i,j))

    #print("seat_list", seat_list)

    if len(seat_list) == 1:
        return seat_list[0]

    # print("seat_list", seat_list)
    # 2. 인접한 칸 중에서 비어있는 칸이 가장 많은 칸 찾기
    for i,j in seat_list:
        # print("i, j", i, j)
        # print(empty_check)
        if j-1 >= 0 and classroom[i][j-1] == 0:
            empty_check[i][j] = empty_check[i][j] + 1
        if i+1 <n and classroom[i+1][j] == 0:
            empty_check[i][j] = empty_check[i][j] + 1
        if j+1 <n and classroom[i][j+1] == 0:
            empty_check[i][j] = empty_check[i][j] + 1
        if i-1 >=0 and classroom[i-1][j] == 0:
            empty_check[i][j] = empty_check[i][j] + 1

    #print("empty_check", empty_check)

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 수 찾기
    empties = 0
    for i in range(n):
        for j in range(n):
            if empty_check[i][j] > empties:
                empties = empty_check[i][j]

    #주변에 비어있는 칸이 없는 경우는 seat_list를 위에서 받은 그대로 가져간다. => 주의!!
    if empties != 0:
        seat_list = []
        for i in range(n):
            for j in range(n):
                if empty_check[i][j] == empties:
                    seat_list.append((i,j))

    if len(seat_list) == 1:
        return seat_list[0]

    # 3. 2을 만족하는 칸도 여러 개인 경우에는
    if len(seat_list) > 1:
        # 행의 번호가 가장 작은 칸으로,
        row_min = 20
        for i in seat_list:
            if i[0] < row_min:
                row_min = i[0]

        row_min_lst = []
        for i in seat_list:
            if i[0] == row_min:
                row_min_lst.append(i)

        if len(row_min_lst) == 1:
            return row_min_lst[0]
        # 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로 자리를 정한다
        else:
            col_min = 20
            for i in row_min_lst:
                if i[1] < col_min:
                    col_min = i[1]

            col_min_lst = []
            for i in row_min_lst:
                if i[1] == col_min:
                    return i

    else:  # 만족하는 칸이 하나인 경우
        return seat_list[0]

cnt = 0
student_info_copy = student_info.copy()
while student_info:
    student = student_info.popleft()
    #print(student)

        # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.

    seat_row, seat_col = get_likes(student[1:])
    classroom[seat_row][seat_col] = student[0]

    # 셀마다 계산을 새로 해야되는 계산용 그래프들은 반복이 끝날때마다 0으로 비워준다
    like_check = []
    empty_check = []
    for i in range(n):
        like_check.append([])
        empty_check.append([])
        for j in range(n):
            like_check[i].append(0)
            empty_check[i].append(0)
    #print(classroom)
# 만족도 구하기

for s in student_info_copy:
    like_lst = s[1:]
    for i in range(n):
        for j in range(n):
            if j - 1 >= 0 and classroom[i][j] == s[0] and classroom[i][j-1] in like_lst:
                satisfaction[i][j] = satisfaction[i][j] + 1
            if i + 1 < n and classroom[i][j] == s[0] and classroom[i+1][j] in like_lst:
                satisfaction[i][j] = satisfaction[i][j] + 1
            if j + 1 < n and classroom[i][j] == s[0] and classroom[i][j+1] in like_lst:
                satisfaction[i][j] = satisfaction[i][j] + 1
            if i - 1 >= 0 and  classroom[i][j] == s[0] and classroom[i-1][j] in like_lst:
                satisfaction[i][j] = satisfaction[i][j] + 1

satisfaction_score = 0
for i in range(n):
    for j in range(n):
        if satisfaction[i][j] == 1:
            satisfaction_score = satisfaction_score +1
        elif satisfaction[i][j] == 2:
            satisfaction_score = satisfaction_score + 10
        elif satisfaction[i][j] == 3:
            satisfaction_score = satisfaction_score + 100
        elif satisfaction[i][j] == 4:
            satisfaction_score = satisfaction_score + 1000

print(satisfaction_score)