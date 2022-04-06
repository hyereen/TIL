n, m = map(int, input().split())

pool = []
used = []

for i in range(1, n+1):
    pool.append(i)
    used.append(0)

chosen = []
# 중복순열 숫자는 중복되도 되는데, 순서가 다르면 다른 경우
# visit check 안함 => 한 케이스에서 같은 숫자 나옴
# 넘길때 숫자 전체를 넘김 => 순서가 다르면 다른 경우로 보니까
def perm(pool, r):
    global chosen
    print(chosen)
    if len(chosen) == r:
        for i in chosen:
            print(i, end=' ')
        print()
        return

    for i in range(len(pool)):
        chosen.append(pool[i])
        perm(pool, r)
        chosen.pop()

perm(pool, m)