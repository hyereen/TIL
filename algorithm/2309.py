nine = []

for i in range(9):
    h = int(input())
    nine.append(h)

nine.sort()

# dfs로 조합 구하기
answer = []

def dfs(lst, idx):
    global answer
    if len(lst) == 7 and sum(lst) == 100: # 9개중에 7개 뽑기 and 합이 100인 조건
        answer.append(lst[:])
        return

    for i in range(idx, 9):
        dfs(lst+[nine[i]], i+1)


dfs([], 0)

for i in answer[0]:
    print(i)