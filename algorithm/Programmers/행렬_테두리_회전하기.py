https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

def solution(rows, columns, queries):
    answer = []  # 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 담을 배열
    graph = []  # rows * columns 행열
    n = 1  # graph에 칸별 숫자 채울 변수

    # 그래프 그리기
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(n)
            n += 1
        graph.append(temp)

    # 회전 함수 -> 한번 실행마다 쿼리에 해당하는 테두리의 숫자들을 회전시킨 그래프를 리턴
    def rotate(graph, rotate_list, r1, r2, c1, c2):
        # 새로운 그래프 그리기
        new_graph = []
        for i in graph:
            new_graph.append(i[:])

        # 움직일 숫자들의 좌표를 저장할 리스트
        # 순서대로 오른쪽, 아래쪽, 왼쪽, 위쪽으로 움직일 숫자들의 좌표를 저장
        new_rotate_list = [[], [], [], []]
        for r, c in rotate_list:
            if r == r1:  # 오른쪽으로 움직일 숫자들의 공통점은 행이 r1
                new_rotate_list[0].append([r, c])
            if c == c2:  # 아래쪽으로 움직일 숫자들의 공통점은 열이 c2
                new_rotate_list[1].append([r, c])
            if r == r2:  # 왼쪽으로 움직일 숫자들의 공통점은 행이 r2
                new_rotate_list[2].insert(0, [r, c])  # 왼쪽으로 순서대로 움직여야 하므로 리스트의 앞에 저장
            if c == c1:  # 위쪽으로 움직일 숫자들의 공통점은 열이 c1
                new_rotate_list[3].insert(0, [r, c])  # 위쪽으로 순서대로 움직여야 하므로 리스트의 위에 저장

        # 움직일 숫자들의 개수는 보다 하나 작은 수들이 이동함
        # 왜냐면 가로로 오른쪽으로 한칸씩 움직인다고 가정하면, 가장 오른쪽 수는 테두리를 나가버리기 때문
        # 따라서 맨끝 하나를 제외한 나머지들을 ori(gin)으로 뽑는다

        # 반면 움직일 숫자들이 새로운 그래프(new_graph)에 위치할 좌표는 한칸씩 미뤄지므로
        # 마찬가지로 가로로 오른쪽으로 한칸씩 움직인다고 가정하면, 가장 왼쪽의 칸은 새로운 수가 위치되지 않음
        for lst in new_rotate_list:
            for ori, nw in zip(lst[:-1], lst[1:]):
                r = ori[0]
                c = ori[1]
                nr = nw[0]
                nc = nw[1]
                new_graph[nr][nc] = graph[r][c]
        return new_graph

    for q in queries:
        # 문제에서 말하는 좌표는 1부터 시작하므로 하나씩 빼줌
        r1 = q[0] - 1
        r2 = q[2] - 1
        c1 = q[1] - 1
        c2 = q[3] - 1
        rotate_list = []  # 회전할 좌표들을 저장하는 리스트
        rotate_list_value = []  # 회전할 좌표의 값(숫자)를 저장하는 리스트
        for i in range(rows):
            for j in range(columns):
                if r1 <= i <= r2 and c1 <= j <= c2:
                    if r1 < i < r2 and c1 < j < c2:  # 가운데부분은 회전되지 않음
                        pass
                    else:  # 가운데말고 테두리들은 회전되므로 좌표와 그 값을 저장
                        rotate_list.append([i, j])
                        rotate_list_value.append(graph[i][j])
        answer.append(min(rotate_list_value))  # 회전 될때 가장 작은 수
        graph = rotate(graph, rotate_list, r1, r2, c1, c2)  # 쿼리마다 회전해서 graph에 저장해줌
    return answer