import sys

# input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
# 각각의 갯수를 저장
add, sub, mul, div = map(int, input().split())
max_num, min_num = -100000000, 1000000000


def dfs(i, res, add, sub, mul, div):
    global max_num, min_num
    if i == n:
        if res > max_num:
            max_num = res
        if res < min_num:
            min_num = res
        return

    else:
        if add:
            dfs(i + 1, res + numbers[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, res - numbers[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, res * numbers[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(res / numbers[i]), add, sub, mul, div - 1)


dfs(1, numbers[0], add, sub, mul, div)
print(max_num, min_num, sep='\n')
