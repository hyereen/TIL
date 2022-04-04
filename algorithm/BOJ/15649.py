n, m = map(int, input().split())

pool = []
used = []
for i in range(1, n+1):
    pool.append(i)
    used.append(0)

chosen = []

def dfs(list, r):
    global chosen, used
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
