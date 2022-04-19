#

# 처음 풀이
# 시간초과 실패: 테케 2, 10

def solution(numbers):
    answer = 0

    num_list = list(numbers)

    # print(visited)
    for i in range(1, len(num_list) + 1):
        make_visited(len(num_list))  # visited 초기화
        comb(num_list, i)

    primes = []
    for i in cases:
        num = int(''.join(i))  # 리스트를 문자열로 합치기
        divisors = []  # 소수 구하기 위해 약수 리스트
        for j in range(1, num + 1):
            if num % j == 0:
                divisors.append(j)
        if len(divisors) == 2:
            primes.append(num)

    # 중복 제거
    primes = list(set(primes))
    answer = len(primes)
    return answer


chosen = []
cases = []
visited = []


def make_visited(n):
    global visited
    visited = [0] * n


def comb(lst, n):
    global chosen, cases, visited
    if len(chosen) == n:
        if chosen not in cases:
            cases.append(chosen[:])
            return

    for i in range(len(lst)):
        if visited[i] == 0:
            chosen.append(lst[i])
            visited[i] = 1
            comb(lst, n)  # 순서가 다르면 다른 케이스로 보니까 다 넘겨줘야 함, lst[i:]하면 n==3일때 visited == [1,1,1]인 경우 안나옴
            chosen.pop()
            visited[i] = 0


# 정답
# 차이점: 모든 숫자의 약수를 일일이 구하지 않고 2를 넘어가면 그 반복을 멈춤
def solution(numbers):
    answer = 0

    num_list = list(numbers)

    # print(visited)
    for i in range(1, len(num_list) + 1):
        make_visited(len(num_list))  # visited 초기화
        perm(num_list, i)  # 순열

    primes = []  # 소수인 숫자들을 저장, 리스트인 이유는 cases가 011, 11인 경우 숫자로 11이어서 같은 숫자를 저장할 수 있기 때문에 리스트로 넣어서 중복을 없애준 다음 개수를 세야 함
    for i in cases:
        num = int(''.join(i))  # 리스트를 문자열로 합쳐서 숫자로 만들기
        divisors = 0  # 약수 개수
        for j in range(1, num + 1):
            if num % j == 0:
                divisors += 1
                if divisors > 2:  # 약수 개수가 2 넘어가면 이미 소수가 아닌거니까
                    break  # 반복을 멈춤
        if divisors == 2:
            primes.append(num)

    # 중복 제거
    primes = list(set(primes))
    answer = len(primes)
    return answer


chosen = []
cases = []
visited = []


# visited를 글로벌 변수로 만들어서 크기를 조절하기 위한 함수
def make_visited(n):
    global visited
    visited = [0] * n


# 숫자 조합 경우의 수 만드는 함수
def perm(lst, n):
    global chosen, cases, visited
    if len(chosen) == n:
        if chosen not in cases:
            cases.append(chosen[:])
            return

    for i in range(len(lst)):
        if visited[i] == 0:
            chosen.append(lst[i])
            visited[i] = 1
            comb(lst, n)  # 순서가 다르면 다른 케이스로 보니까 다 넘겨줘야 함, lst[i:]하면 n==3일때 visited == [1,1,1]인 경우 안나옴
            chosen.pop()
            visited[i] = 0
