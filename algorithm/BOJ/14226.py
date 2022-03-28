from collections import deque

S = int(input())

queue = deque([[1, 0, 0]])  # 화면의 이모티콘 개수, 클립보드 이모티콘 개수, 연산 횟수

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

while queue:
    print(queue)

    screen, clipboard, cnt = queue.popleft()

    if screen == S:  # 만약 스크린의 개수와 S가 동일하다면
        print(cnt)  # 걸린 횟수를 출력 후
        break  # 탈출

    for i in range(3):  # 연산을 3번 수행한다.

        # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
        if i == 0:
            new_clipboard, new_screen = screen, screen

        # 화면에 클립보드에 있는 이모티콘 들을 추가
        elif i == 1:
            new_screen, new_clipboard = screen + clipboard, clipboard

        # 화면에 있는 이모티콘 개수 한개 빼기
        else:
            new_screen, new_clipboard = screen - 1, clipboard

        # 만약 새로 계산된 이모티콘과 클립보드의 개수가 범위를 벗어나거나 이미 방문한 적이 있다면 continue
        if new_screen >= 1001 or new_screen < 0 or new_clipboard >= 1001 or new_clipboard < 0 or visited[new_screen][
            new_clipboard]:
            continue

        # 방문처리 후 연산 횟수를 +1 하여 큐에 추가
        visited[new_screen][new_clipboard] = True
        queue.append([new_screen, new_clipboard, cnt + 1])