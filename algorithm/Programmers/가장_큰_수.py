# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# 첫번째 풀이 순열 이용
# 런타임 에러: 테케 1~6
# 시간 초과: 테케 7~11
# 시간 복잡도가 너무 큼!

def solution(numbers):
    answer = ''
    dfs(numbers, len(numbers))
    nums = []
    temp = ""
    for i in cases:
        for j in i:
            temp = temp + str(j)
        nums.append(temp)
        temp = ""
    nums.sort(reverse=True)
    answer = nums[0]
    return answer


chosen = []
cases = []
visited = [0] * 100000  # 한 케이스에서 같은 숫자가 나오면 안되니까 필요함


def dfs(lst, n):
    global chosen, visited

    if len(chosen) == n:
        cases.append(chosen[:])  # 그냥 chosen이면 cases가 빈칸 됨
        return

    for i in range(len(lst)):
        if visited[i] == 0:
            chosen.append(lst[i])
            visited[i] = 1
            dfs(lst, n)
            chosen.pop()
            visited[i] = 0

# 정답

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))