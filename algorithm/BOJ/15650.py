n, m = map(int, input().split())

pool = []
used = []

for i in range(1, n+1):
    pool.append(i)
    used.append(0)


chosen = []

def comb(pool, r):
    global chosen, used

    if len(chosen) == r:
        for i in chosen:
            print(i, end=' ')
        print()
        return

    for i in range(len(pool)):
        used[i] = 1
        chosen.append(pool[i])

        comb(pool[i+1:], r) # perm와 다른점!
        used[i] = 0
        chosen.pop()

comb(pool, m)