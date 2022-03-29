import sys
input = sys.stdin.readline
n = int(input())

players = []
graph = []

# 팀원의 번호가 담긴 players 만들기
# 능력치 표 graph 저장하기
for i in range(n):
  players.append(i)
  line = list(map(int, input().split()))
  graph.append(line)


# 두 팀으로 나눌 경우의 수를 저장할 리스트
player_cases = []

# dfs로 조합구하기 => 기억하기 !! 
# idx: depth
# list: 하나의 경우의 조합을 저장해둘 리스트
# lst: 조합을 구할 리스트
# r: 몇개 뽑을지
# res: 조합의 경우들을 저장할 변수
def dfs(idx, list, lst, r, res):
    n = len(lst)
    if len(list) == r:
        res.append(list[:])
        return

    for i in range(idx, n):
        dfs(i+1,list+[lst[i]], lst, r, res)

# 두 팀으로 나눌 조합의 경우를 찾는다
dfs(0, [], players, len(players)//2, player_cases)

# 각 팀으로 나눌 조합별 능력치 차이를 저장할 변수, 최댓값으로 설정해둬서 보다 작은 차이가 나오면 갱신되도록
min_diff = 100

# 조합의 경우에 따라서 팀별 능력치를 계산할 반복문
# 이때 예를들어 start팀이 [1,2,3]인 경우랑, link팀이 [1,2,3]인 경우랑 같으므로 조합 리스트에서 반만 계산해도 된다.
# 조합을 만들기 위한 players가 오름차순이어서 조합의 결과도 오름차순이어서 그냥 반만 나눠도 된다. => 이부분을 찾는게 가장 어려웠다 ㅠ
for start in player_cases[:len(player_cases)//2]:
    start_twos = [] # 각 팀별 능력치를 구할 쌍을 저장해둘 리스트, 마찬가지로 위의 dfs 함수를 이용해서 조합을 구한다
    link_twos = []
    link = list(set(players) - set(start)) # set의 차집합을 이용해서 상대편 팀의 구성을 구한다
    dfs(0, [], start, 2, start_twos) # 각각의 능력치를 구할 쌍을 찾는다
    dfs(0, [], link, 2, link_twos)

    start_stats = 0 # 각 팀별 능력치를 저장해둘 변수
    link_stats = 0
    # print("start", start)
    # print("link", link)
   # print("start_twos", start_twos)
   # print("link_twos", link_twos)
    for i, j in zip(start_twos, link_twos): # 각 팀별 선수 쌍이 저장된 리스트를 동시에 돌면서
        # print("i", i)
        # print("j", j)
        start_stats = start_stats + graph[i[0]][i[1]]+graph[i[1]][i[0]] # 각 팀별 능력치의 합을 구해준다
        link_stats = link_stats + graph[j[0]][j[1]] + graph[j[1]][j[0]]

    # print("start_stats", start_stats)
    # print("link_stats", link_stats)
    diff = abs(start_stats - link_stats) # 그때 차이를 구하고

    if min_diff > diff: # 하나의 팀 구성 조합 케이스를 계산하고 나서 최솟값을 업데이트해준다
        min_diff = diff



print(min_diff)