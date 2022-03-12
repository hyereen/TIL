# 테스트 케이스 개수

def get_median(tlist, n):
  medians = []
  for i in range(n):
    if i%2 == 0:
      temp = sorted(tlist[0:i+1])
      medians.append(temp[i//2])
  return medians

t = int(input())

for i in range(t):
  n = int(input()) # 수열의 크기
  tlist = []
  # 수열의 원, 10개씩 끊어받기 -> 안그러면 value error 뜸
  if n <= 10:
    tlist= tlist+ list(map(int, input().split()))
  else:
    for i in range(n//10 +1):
      tlist = tlist + list(map(int, input().split()))

  # 중앙값의 개수
  n_med = n//2 + 1
  print(n_med)
  # 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력
  ans = get_median(tlist, n)

  if n_med <= 10:
    for j in ans:
      print(j, end=' ')
  else:
    cnt = 0
    for k in range(len(ans)):
      if cnt == 10:
        print()
      print(ans[k], end=' ')
      cnt +=1
