t = int(input())

for i in range(t):
  case = list(map(int, input().split()))
  case.sort(reverse = True)
  print(case[2])