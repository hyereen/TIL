# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=581

N, M, K = map(int, input().split())
posts = list(map(int, input().split()))

used = [0] * N # 순열을 구할때 필요한 방문체크
chosen = [] # 순열을 만들기 위한 선택한 숫자를 담는 변수
carrying_sum_min = sum(posts) * K # 최소한의 택배 무게를 저장할 변수


# 순열 구하기
def dfs(list, r):
    global chosen, used, carrying_sum_min
    if len(chosen) == r: # 순열 케이스 구했을 때
        # print(chosen)
        carrying = 0 # 현재 k번째 수행에서 들고 있는 무게의 합
        carrying_sum = 0 # 현재 순열 케이스에서 K번동안 총 들어야하는 무게의 합
        k = 0 # 일을 시행한 횟수
        i = 0 # 택배 인덱스
        while k < K: # 시행 횟수가 K보다 작은 동안
            if carrying + chosen[i] <= M: # 현재 들고 있는 무게에 다음 택배를 더한게 택배 바구니보다 작으면
                carrying = carrying + chosen[i] # 현재 무게에 다음 택배 무게를 더해주고
                i += 1 # 그 다음 택배의 무게를 알기 위해 인덱스를 더해줌
            else: # 현재 들고 있는 무게에 다음 택배를 더한게 택배 바구니보다 크면
                carrying_sum = carrying_sum + carrying # 현재 순열 케이스에서 들어야하는 무게에 더해주고
                carrying = 0 # k번째 수행에서 들고 있는 무게는 리셋이 됨
                k += 1 # 대신 수행 횟수는 늘어남
            if i == len(chosen): # 택배 무게를 계속 더하기 위해 레일 개수보다 커지면 0으로 리셋
                i = 0

        carrying_sum_min = min(carrying_sum_min, carrying_sum) # 순열 케이스를 반복하면서 최솟값을 찾는다

        return

    for i in range(len(list)):
        if not used[i]:
            chosen.append(list[i])
            used[i] = 1
            dfs(list, r)
            used[i] = 0
            chosen.pop()


dfs(posts, N)

print(carrying_sum_min)