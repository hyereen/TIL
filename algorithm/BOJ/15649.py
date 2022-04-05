n, m = map(int, input().split())

pool = []
used = []
for i in range(1, n+1):
    pool.append(i)
    used.append(0)

chosen = []
# 순열
# visit check 했음 => 한 케이스에서 같은 숫자가 나오면 안됨
# 넘길때 숫자 전체 넘김 => 순서가 다르면 다른 경우로 보니까 1,2도 나오고 2,1 도 나오도록
def dfs(list, r):
    global chosen, used
    print(chosen)
    if len(chosen) == r:
        for i in chosen:
            print(i, end=' ')
        print()
        return

    for i in range(len(list)):
        if not used[i]:
            chosen.append(list[i])
            used[i] = 1
            dfs(list, r)
            used[i] = 0
            chosen.pop()

dfs(pool, m)
