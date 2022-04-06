n, m = map(int, input().split())

pool = []

for i in range(1, n+1):
    pool.append(i)


# 한 케이스 안에 숫자 중복 가능 -> visit 체크 안함
# 순서가 달라도 숫자 구성이 같으면 같은 케이스 -> 넘길때 다음숫자부터
# 중복 조합
chosen = []
def comb(pool):
    global chosen

    if len(chosen) == m:
        for i in chosen:
            print(i, end=' ')
        print()
        return

    for i in range(len(pool)):
        chosen.append(pool[i])
        comb(pool[i:])
        chosen.pop()

comb(pool)